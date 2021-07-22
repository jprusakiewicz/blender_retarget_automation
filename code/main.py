import os
import subprocess
import sys
from typing import List

from config import settings


def get_all_fbx_files(dir_path: str) -> List[str]:
    fbx_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".fbx")]
    return fbx_files


def log_subprocess_output(subproces_result: subprocess.CompletedProcess, encoding='utf-8'):
    for line in subproces_result.stdout.splitlines():  # feel free changing to logging.log()
        print(str(line, encoding))  # feel free changing to logging.log()


if __name__ == "__main__":
    source_files = get_all_fbx_files(settings.source_fbx_directory_path)
    argv = sys.argv

    if len(argv) > 2:
        print("To many script parameters!")
    if len(source_files) == 0:
        print("No source fbx files!")
    for file in source_files:
        if argv[-1] == "--bake" or argv[-1] == "-b":
            command = ['Blender', settings.target_file_path_bake, '--background', '--python',
                       settings.core_path, "--",
                       str(settings.import_scale), file, settings.export_directory_path, settings.export_suffix,
                       settings.better_fbx_install_global_path]
        else:
            command = ['Blender', settings.target_file_path_no_bake, '--background', '--python',
                       settings.core_path, "--",
                       str(settings.import_scale), file, settings.export_directory_path, settings.export_suffix,
                       settings.better_fbx_install_global_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                cwd=os.path.dirname(os.path.realpath(__file__)))
        log_subprocess_output(result)
