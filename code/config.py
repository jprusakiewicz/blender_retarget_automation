from pydantic import BaseSettings


class Settings(BaseSettings):
    import_scale: int = 1

    core_path: str = 'core.py'
    target_file_path_bake: str = r"../target/target_bake.blend"
    target_file_path_no_bake: str = r"../target/target_no_bake.blend"
    source_fbx_directory_path: str = r"../source/"
    export_directory_path: str = r'../exports'
    export_suffix: str = '_DONE'
    better_fbx_install_global_path: str = r"C://Users//Python//Desktop//better-fbx-addon//addon//2.8//fbx.zip"


settings = Settings()
