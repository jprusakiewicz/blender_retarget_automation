from pydantic import BaseSettings


class Settings(BaseSettings):
    # source_animation_suffix = '_Wiktor' #useless
    IMPORT_SCALE = 1

    target_file_path = r"../target/target.blend"
    source_fbx_directory_path = "../source/"
    export_directory_path = '../exports'


settings = Settings()
