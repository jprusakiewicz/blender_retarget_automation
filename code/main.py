import os
import logging

from . import core

# source_animation_suffix = '_Wiktor' #useless
source_fbx_file_path = "../source/source.fbx"
export_directory_path = "../exports/"
BLENDER_PATH = "C:\Program Files\Blender Foundation\Blender 2.91"
IMPORT_SCALE = 1


if __name__ == "__main__":
    core.retarget_animation(IMPORT_SCALE, source_fbx_file_path, export_directory_path)

