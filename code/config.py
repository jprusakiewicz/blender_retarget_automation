from pydantic import BaseSettings


class Settings(BaseSettings):
    # source_animation_suffix = '_Wiktor' #useless
    import_scale: int = 1

    core_path = 'core.py'
    target_file_path = r"../target/target.blend"
    source_fbx_directory_path = r"../source/"
    export_directory_path = r'../exports'


settings = Settings()
