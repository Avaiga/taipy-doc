# ################################################################################
# Taipy Contributor section generation setup step.
#
# A contributor section is generated based on internal and external contributors
# retrieved using GitHub REST APIs.
# ################################################################################
import os

import requests

from .setup import SetupStep, Setup


class ContributorStep(SetupStep):

    def __init__(self):
        self.BASE_URL = "https://api.github.com"
        self.ORGANIZATION_URL = f"{self.BASE_URL}/orgs/avaiga/members"
        self.REPOSITORIES = [
            "taipy-config",
            "taipy-core",
            "taipy-gui",
            "taipy-rest",
            # "taipy-auth",
            # "taipy-enterprise",
        ]
        self.REPO_URLS = list(map(lambda _: f"{self.BASE_URL}/repos/avaiga/" + _ + "/contributors", self.REPOSITORIES))
        self.PATH = ""
        self.ANONYMOUS = ["dependabot[bot]"]
        self.content = ""

    def enter(self, setup: Setup):
        self.PATH = os.path.join(setup.docs_dir, "credits", "contributors.md")

    def get_id(self) -> str:
        return "contributors"

    def get_description(self) -> str:
        return "Generating the contributors"

    def setup(self, setup: Setup) -> None:
        avaiga_members = self.get_avaiga_members()
        contributors = self.get_contributors(avaiga_members)
        self.build_content(contributors)

    def get_avaiga_members(self):
        members = requests.get(self.ORGANIZATION_URL).json()
        return list(map(lambda _: _['login'], members))

    def get_contributors(self, avaiga_members):
        contributors = {}
        for url in self.REPO_URLS:
            response = requests.get(url)
            for c in response.json():
                # print(c)
                login = c['login']
                contributors[login] = {"avatar_url": c['avatar_url'],
                                       "html_url": c['html_url'],
                                       "avaiga_member": True if login in avaiga_members else False}
        return contributors

    def build_content(self, contributors):
        self.content = """# Contributors

A special thanks go to our contributors:\n"""
        for login, contributor_info in contributors.items():
            if login not in self.ANONYMOUS:
                self.content += f"\n- [<img src='{contributor_info['avatar_url']}' alt='avatar' width='20'/>" \
                                f" {login}]" \
                                f"({contributor_info['html_url']})"
        self.content += "\n"

    def exit(self, setup: Setup):
        with open(self.PATH, "w") as f:
            f.write(self.content)
