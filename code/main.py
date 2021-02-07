import os
import subprocess
from typing import List

from config import settings


def create_local_file_path(file_name: str) -> str:
    return os.path.join("../source/", file_name)


def get_all_fbx_files(source_path: str) -> List[str]:
    source_files = [create_local_file_path(f) for f in os.listdir(source_path) if f.endswith(".fbx")]
    return source_files


CORE_PATH = 'core.py'

if __name__ == "__main__":
    source_files = get_all_fbx_files(settings.source_fbx_directory_path)

    for file in source_files:
        command = ['blender', settings.target_file_path, '--background', '--python', CORE_PATH, "--",
                   str(settings.IMPORT_SCALE), file, settings.export_directory_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                cwd=os.path.dirname(os.path.realpath(__file__)))
        print(result.returncode, result.stderr, result.stdout)
