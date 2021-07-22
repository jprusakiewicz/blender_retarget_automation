# Blender retarget automation using python API 🐍

## How to use

Add Blender to env path 
https://docs.blender.org/manual/en/2.93/advanced/command_line/launch/windows.html

Add _.blend_ file to **target** folder  
add (one or many) _.fbx_ files to **source** folder  
Go to **code** folder  
Run `pip install -r requirements.txt`to install dependencies  
Run `python main.py` or `python main.py --bake`in console.  

## `--bake` parameter
use --bake or -b parameter for baking mode
use --nobake or run main.py script without parameter for no-baking mode

## user configuration 
####There are several parameters user can set in config.py file:

* import_scale - imported _.fbx_ object scale

##### All of the following paths are referenced starting from code directory
* core_path - core.py file path  
* target_file_path - .blend file with target object path 
* source_fbx_directory_path - directory path where will be preplaced source .fbx files  
* export_directory_path - directory where will be exported processed .fbx files  
* export_suffix - every exported .fbx file name suffix
   

## Going short with only one _.fbx_ file  
 ####(optional)
If you want to process only one .fbx file you can use `core.py` file with _Blender_ command.
It takes 4 arguments: import scale, source fbx file path, export directory path, export suffix  
example:  
`Blender ../target/target.blend --background --python core.py -- 1 ../source/ ../exports _DONE`


## Retarget and burnout process step by step  
1. set object mode  
2. import fbx with scale=x using better fbx  
3. select collection "Armature"  
4. Open Action Editor  
5. Select animation from imported fbx  
-retarget and root burn goes automatically-  
6. select collection  "armature_NEW_Default"  
7. export fbx with preset, export_name = animation_name with suffix  

## Blender env path troubleshooting
Depending how you set your _blenderpath_ you may want to change first capital letter in Blender command.
To do this replace it in main.py:22  
In my case it works with both '**blender**' and '**Blender**' (big and small letter)

## Error logs
If there is any error produced by user, preventing code to work properly 
(e.g. wrong user configuration) message will be logged.
Be aware that it doesn't have to lie at the end of output.  
![](https://imgur.com/eDaJ04t)


1.1 version tested on 2.91.0 Blender version  
Made with 🧠 by Jakub Prusakiewicz

Changelog:  
-additional parameter while running main.py file for baking/no-baking mode  
-target_file_path in config.py split into target_file_path_bake and target_file_path_no_bake 