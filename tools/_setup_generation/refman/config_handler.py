import os
import shutil

from ..setup import Setup


class ConfigHandler:
    REPL_STR = "sections (Dict[str, Dict[str, Section]]): A dictionary containing all non-unique sections.\n"
    METHODS_FILE = "config_doc.txt"

    def __init__(self, setup: Setup):
        self.tools_dir = setup.tools_dir

    def restore_config_module(self):
        taipy_config_dir = os.path.join(self.tools_dir, "taipy", "common", "config")
        config_backup_path = os.path.join(taipy_config_dir, "config.py.bak")
        if os.path.exists(config_backup_path):
            shutil.move(config_backup_path, os.path.join(taipy_config_dir, "config.py"))

    def inject_documentation(self):
        methods_to_inject = self._read_file(self.METHODS_FILE)
        self._backup()
        self._inject_documentation(methods_to_inject)

    @staticmethod
    def _read_file(file):
        if not os.path.exists(file):
            print("WARNING - Nothing found to inject to Config documentation")
            return

        # Get code of methods to inject
        with open(file, "r") as f:
            content = f.read()

        # Delete temporary file
        if os.path.exists(file):
            os.remove(file)
        return content

    def _backup(self):
        # Backup file taipy/common/config/config.py
        taipy_config_dir = os.path.join(self.tools_dir, "taipy", "common", "config")
        config_path = os.path.join(taipy_config_dir, "config.py")
        shutil.copyfile(config_path, os.path.join(taipy_config_dir, "config.py.bak"))

    def _inject_documentation(self, methods_to_inject):
        config_path = os.path.join(self.tools_dir, "taipy", "common", "config", "config.py")

        # Read config.py file
        with open(config_path, "r") as f:
            contents = f.readlines()

        # Inject imports and code
        imports_to_inject = """
from datetime import datetime
from types import NoneType
from typing import Any, Callable, Dict, List, Union, Optional
import json
from .common.scope import Scope
from .common.frequency import Frequency
from taipy.auth.config import AuthenticationConfig
from taipy.common.config.section import Section
from taipy.core.common.mongo_default_document import MongoDefaultDocument
from taipy.core.config.core_section import CoreSection
from taipy.core.config.job_config import JobConfig
from taipy.core.config.data_node_config import DataNodeConfig
from taipy.core.config.task_config import TaskConfig
from taipy.core.config.scenario_config import ScenarioConfig
from taipy.enterprise.core.config import MigrationConfig
from taipy.gui import _GuiSection
from taipy.enterprise.core.config import TelemetrySection\n"""

        contents.insert(11, imports_to_inject)
        contents.insert(len(contents) - 2, methods_to_inject)

        # Fix code injection
        with open(config_path, "w") as f:
            new_content = "".join(contents)
            new_content = new_content.replace(
                "custom_document: Any = <class 'taipy.core.common.mongo_default_document.MongoDefaultDocument'>",
                "custom_document: Any = MongoDefaultDocument",
            )
            new_content = new_content.replace(
                "taipy.common.config.common.scope.Scope", "Scope"
            )
            new_content = new_content.replace("<Scope.SCENARIO: 2>", "Scope.SCENARIO")
            new_content = new_content.replace(
                "taipy.core.config.data_node_config.DataNodeConfig", "DataNodeConfig"
            )
            new_content = new_content.replace("taipy.core.config.task_config.TaskConfig", "TaskConfig")
            new_content = new_content.replace("taipy.common.config.common.frequency.Frequency", "Frequency")
            new_content = new_content.replace("taipy.common.config.section.Section", "Section")
            new_content = new_content.replace("@_Classproperty", "@property")
            f.write(new_content)
