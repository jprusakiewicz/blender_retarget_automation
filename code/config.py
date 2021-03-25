from pydantic import BaseSettings


class Settings(BaseSettings):
    # source_animation_suffix = '_Wiktor' #useless
    import_scale: int = 1

    core_path: str = 'core.py'
    target_file_path: str = r"../target/target.blend"
    source_fbx_directory_path: str = r"../source/"
    export_directory_path: str = r'../exports'
    export_suffix: str = '_DONE'
    better_fbx_install_global_path: str = r"C://Users//Python//Desktop//better-fbx-addon//addon//2.8//fbx.zip"


settings = Settings()
