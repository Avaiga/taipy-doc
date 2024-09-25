import os
import shutil

from ..setup import Setup


class ConfigHandler:

    def __init__(self, setup: Setup):
        self.tools_dir = setup.tools_dir

    def restore_config_module(self):
        taipy_config_dir = os.path.join(self.tools_dir, "taipy", "config")
        config_backup_path = os.path.join(taipy_config_dir, "config.py.bak")
        if os.path.exists(config_backup_path):
            shutil.move(config_backup_path, os.path.join(taipy_config_dir, "config.py"))

    def add_external_methods(self):
        if not os.path.exists("config_doc.txt"):
            print("WARNING - No methods found to inject to Config documentation")
            return

        # Get code of methods to inject
        with open("config_doc.txt", "r") as f:
            print("INFO - Injecting methods to Config documentation.")
            methods_to_inject = f.read()

        # Delete temporary file
        if os.path.exists("config_doc.txt"):
            os.remove("config_doc.txt")

        # Backup file taipy/config/config.py
        taipy_config_dir = os.path.join(self.tools_dir, "taipy", "config")
        config_path = os.path.join(taipy_config_dir, "config.py")
        shutil.copyfile(config_path, os.path.join(taipy_config_dir, "config.py.bak"))

        # Read config.py file
        with open(config_path, "r") as f:
            contents = f.readlines()

        # Inject imports and code
        imports_to_inject = """
    from types import NoneType
    from typing import Any, Callable, Dict, List, Union, Optional
    import json
    from .common.scope import Scope
    from .common.frequency import Frequency
    from taipy.core.common.mongo_default_document import MongoDefaultDocument
    from taipy.core.config.job_config import JobConfig
    from taipy.core.config.data_node_config import DataNodeConfig
    from taipy.core.config.task_config import TaskConfig
    from taipy.core.config.scenario_config import ScenarioConfig
    from taipy.core.config.sequence_config import SequenceConfig\n"""
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
                "taipy.config.common.scope.Scope", "Scope"
            )
            new_content = new_content.replace("<Scope.SCENARIO: 2>", "Scope.SCENARIO")
            new_content = new_content.replace(
                "taipy.core.config.data_node_config.DataNodeConfig", "DataNodeConfig"
            )
            new_content = new_content.replace(
                "taipy.core.config.task_config.TaskConfig", "TaskConfig"
            )
            new_content = new_content.replace(
                "taipy.core.config.sequence_config.SequenceConfig", "SequenceConfig"
            )
            new_content = new_content.replace(
                "taipy.config.common.frequency.Frequency", "Frequency"
            )
            f.write(new_content)
