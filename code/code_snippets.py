import bpy
import os

source_fbx_file_path = "/Users/kuba/Downloads/blender_automation/source/source.fbx"
export_directory_path="/Users/kuba/Downloads/blender_automation/exports/"
IMPORT_SCALE = 1
# source_animation_suffix = 'Wiktor'
# set mode
bpy.ops.object.mode_set(mode='OBJECT')


#select armature
target = bpy.context.scene.collection.all_objects["Armature"]

#in order that theres no import name parameter, we have to change imported object name afterwards.
#fortunatley imported object is beeing selected after import.
# we deselect all first
bpy.ops.object.select_all(action='DESELECT') 


#better import fbx
bpy.ops.better_import.fbx(filepath = source_fbx_file_path, my_scale=IMPORT_SCALE, use_auto_bone_orientation=False, use_optimize_for_blender=True)
bpy.ops.object.mode_set(mode='OBJECT')

#IMPORTANT: import must be preceded with ALL OBJECTS DESELECT 
imported_objects = [o for o in bpy.context.selected_objects if o.type =='ARMATURE']

if len(imported_objects) > 1:
    print("imported more than one armature!")

source = imported_objects[0]

source_animation_name = source.animation_data.action.name

# target.animation_data.action = source.animation_data.action
target.animation_data.action = bpy.data.actions.get(source_animation_name)
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')

bpy.data.objects["armature_NEW_Default"].select_set(True)

full_export_path = os.path.join(export_directory_path, source_animation_name + ".fbx")
bpy.ops.export_scene.fbx(filepath=full_export_path, use_selection=True, apply_scale_options="FBX_SCALE_UNITS" ,object_types={'ARMATURE', 'MESH'}, apply_unit_scale=True,use_mesh_modifiers=True, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_force_startend_keying=False)


# UNUSED SNIPPETS
# #select object
# armature.select_set(True)

# #deselect all
# for obj in bpy.data.objects:
#     obj.select_set(False)

#deselect all v2
# bpy.ops.object.select_all(action='DESELECT')

#find object with name "source"
#source = bpy.context.scene.collection.all_objects["Source"]

#bpy.data.objects["Armature"].select_set(True)
#source = bpy.context.scene.collection.all_objects["Armature.001"]

