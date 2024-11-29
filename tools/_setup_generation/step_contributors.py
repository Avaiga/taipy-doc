# ################################################################################
# Taipy Contributor list generation setup step.
#
# A contributors list is generated based on internal and external contributors
# retrieved using GitHub REST APIs.
# ################################################################################
import base64
import os
import random
import requests

from .setup import SetupStep, Setup


class ContributorsStep(SetupStep):
    def __init__(self):
        self.GH_TOKEN = os.getenv("GITHUB_TOKEN", None)
        self.BASE_URL = "https://api.github.com"
        self.ORGANIZATION_URL = f"{self.BASE_URL}/orgs/Avaiga"
        self.MEMBERS_URL = f"{self.ORGANIZATION_URL}/members"
        self.REPOS = f"{self.ORGANIZATION_URL}/repos"
        self.CONTRIBUTORS_URL = f"{self.BASE_URL}/Avaiga/taipy/contributors"
        self.REPO_URLS = []
        self.MEMBERS = {}
        self.CONTRIBUTORS = {}
        self.ANONYMOUS = ["dependabot[bot]", "infrastructure-management[bot]"]
        self.PATH = ""
        self.TEMPLATE_SUFFIX = "_template"

    def enter(self, setup: Setup):
        self.PATH = os.path.join(setup.docs_dir, "contributing", "contributors.md")

    def get_id(self) -> str:
        return "contributors"

    def get_description(self) -> str:
        return "Generating the contributors list."

    def setup(self, setup: Setup) -> None:
        try:
            self.get_repo_urls()
            self.get_avaiga_members()
            self.get_contributors()
            self.build_content((self.MEMBERS, "[AVAIGA_TEAM_MEMBERS]"), (self.CONTRIBUTORS, "[TAIPY_CONTRIBUTORS]"))
        except Exception as e:
            print(f"WARNING - Exception raised while listing contributors:\n{e}")

    def get_repo_urls(self):
        response = self.__get(self.REPOS)
        if response.status_code != 200:
            #print(f"WARNING - Couldn't get repositories. response.status_code: {response.status_code}", flush=True)
            return
        repos = response.json()
        self.REPO_URLS = list(map(lambda _: _["url"], repos))

    def get_avaiga_members(self):
        response = self.__get(self.MEMBERS_URL)
        if response.status_code != 200:
            #print(f"WARNING - Couldn't get members. response.status_code: {response.status_code}", flush=True)
            return
        members = response.json()
        for member in members:
            login = member["login"]
            if login not in self.MEMBERS and login not in self.ANONYMOUS:
                self.MEMBERS[login] = {"avatar_url": member["avatar_url"], "html_url": member["html_url"]}

    def get_contributors(self):
        for url in self.REPO_URLS:
            response = self.__get(url + "/contributors")
            if response.status_code != 200:
                #print(f"WARNING - Couldn't get contributors. response.status_code: {response.status_code}", flush=True)
                return
            contributors = response.json()
            for contrib in contributors:
                login = contrib["login"]
                if login not in self.CONTRIBUTORS and login not in self.ANONYMOUS:
                    self.CONTRIBUTORS[login] = {"avatar_url": contrib["avatar_url"], "html_url": contrib["html_url"]}

    def build_content(self, *members_pattern_tuples):
        pattern_content_tuples = []
        for member_pattern in members_pattern_tuples:
            members = member_pattern[0]
            pattern = member_pattern[1]
            content = ""
            members_list = list(members.items())
            random.shuffle(members_list)
            for login, member_info in members_list:
                if login not in self.ANONYMOUS:
                    content += (
                        f"\n- [<img src='{member_info['avatar_url']}' alt='{login} GitHub avatar' width='20'/>"
                        f"{login}]"
                        f"({member_info['html_url']})"
                    )
            content += "\n"
            pattern_content_tuples.append((pattern, content))

        self._replace(self.PATH, *pattern_content_tuples)

    def _replace(self, path, *pattern_content_tuples):
        # Read in the file
        with open(path + self.TEMPLATE_SUFFIX, "r") as file:
            file_data = file.read()

        # Replace the patterns by the contents
        for pattern_content in pattern_content_tuples:
            pattern = pattern_content[0]
            content = pattern_content[1]
            file_data = file_data.replace(pattern, content)

        # Write the file out without the template suffix
        with open(path, "w") as file:
            file.write(file_data)

    def __get(self, url, with_token=True):
        if with_token and self.GH_TOKEN:
            return requests.get(
                url, headers={"Accept": "application/vnd.github+json", "Authorization": "Bearer " + self.GH_TOKEN}
            )
        else:
            return requests.get(url)

    def exit(self, setup: Setup):
        pass
