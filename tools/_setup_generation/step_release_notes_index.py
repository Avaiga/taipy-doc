# ################################################################################
# Release notes index page generation step.
#
# ################################################################################
import os

from .setup import Setup
from .step_file_injection import FileInjectionStep


class ReleaseNotesIndexPageStep(FileInjectionStep):

    def __init__(self):
        super().__init__(
            "release_notes_index",
            "Injecting links to the various release note pages.",
            "[RELEASE_NOTES_INDEX_CONTENT]",
            "",
            "",
        )

    def enter(self, setup: Setup):
        self.src_path = os.path.join(setup.docs_dir, "release-notes")
        self.dst_path = os.path.join(self.src_path, "index.md")
        self.dst_tpl_path = self.dst_path + "_template"

    def setup(self, setup: Setup) -> None:
        try:
            content = self._get_content()
            self._replace(self.dst_tpl_path, self.pattern, content, self.dst_path)
        except Exception as e:
            print(f"ERROR - Cannot generate page: {e}")

    def _get_content(self) -> str:
        versions = sorted(
            [d for d in os.listdir(self.src_path) if os.path.isdir(os.path.join(self.src_path, d))],
            reverse=True,
        )
        print(f"{len(versions)} versions processed.")
        return "\n".join(
            f"- [Release notes for version {version}](./{version}/index.md)" for version in versions
        )
