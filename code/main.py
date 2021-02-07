import os
from os.path import isfile, join
from typing import List
import logging
import subprocess

from config import settings


def get_all_fbx_files(source_path: str) -> List[str]:
    source_files = [f for f in os.listdir(source_path) if f.endswith(".fbx")]
    return source_files


def get_core_path():
    main_path = os.path.abspath(__file__)
    core_path = main_path.split("\\")[:-1] + ["core.py"]
    return os.path.join(*core_path)


if __name__ == "__main__":
    source_files = get_all_fbx_files(settings.source_fbx_directory_path)

    for file in source_files:
        core_path = get_core_path()
        print(core_path)
        #command = ['blender', settings.target_file_path, '--background', '--python', core_path, str(settings.IMPORT_SCALE), file, settings.export_directory_path]
        command = ['blender', settings.target_file_path, '--background', '--python', core_path]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  shell=True)
        print(result.returncode, result.stdout, result.stderr)

    # core.retarget_animation(IMPORT_SCALE, source_fbx_file_path, export_directory_path)
