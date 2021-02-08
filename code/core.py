import logging
import os
import sys

import bpy


def retarget_animation(import_scale: str, source_fbx_file_path: str, export_directory_path: str):
    bpy.ops.object.mode_set(mode='OBJECT')
    target = bpy.context.scene.collection.all_objects["Armature"]
    bpy.ops.object.select_all(action='DESELECT')

    bpy.ops.better_import.fbx(filepath=source_fbx_file_path, my_scale=int(import_scale),
                              use_auto_bone_orientation=False,
                              use_optimize_for_blender=True)
    bpy.ops.object.mode_set(mode='OBJECT')

    imported_objects = [o for o in bpy.context.selected_objects if o.type == 'ARMATURE']

    if len(imported_objects) > 1:
        logging.error("imported more than one armature!")
        exit()

    source = imported_objects[0]

    source_animation_name = source.animation_data.action.name

    frame_range = source.animation_data.action.frame_range
    last_frame = frame_range[1]
    bpy.context.scene.frame_end = last_frame

    target.animation_data.action = bpy.data.actions.get(source_animation_name)
    export_name = source_animation_name + '_DONE'
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.data.objects["armature_NEW_Default"].select_set(True)

    full_export_path = os.path.join(export_directory_path, export_name + ".fbx")
    bpy.ops.export_scene.fbx(filepath=full_export_path, use_selection=True, apply_scale_options="FBX_SCALE_UNITS",
                             object_types={'ARMATURE', 'MESH'}, apply_unit_scale=True, use_mesh_modifiers=True,
                             add_leaf_bones=False, use_armature_deform_only=True,
                             bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=False,
                             bake_anim_use_all_actions=False, bake_anim_force_startend_keying=False)


if __name__ == "__main__":
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--"

    if len(argv) != 3:
        logging.critical("wrong parameters count")
        exit()

    retarget_animation(*argv)
