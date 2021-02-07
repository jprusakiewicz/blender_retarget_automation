from pydantic import BaseSettings

class Settings(BaseSettings):
    # source_animation_suffix = '_Wiktor' #useless

    target_file_path = r"C:\Users\jakub.prusakiewicz\blender_retarget_automation\target\target.blend"
    source_fbx_directory_path = "../source/"
    export_directory_path = "../exports/"
    BLENDER_PATH = r"C:/Program Files/Blender Foundation\Blender 2.91"
    IMPORT_SCALE = 1

settings = Settings()