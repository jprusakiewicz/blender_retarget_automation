# Blender retarget automation using python API

## How to use

Add Blender to env path 
https://docs.blender.org/manual/en/2.79/advanced/command_line/introduction.html

Add _.blend_ file to **target** folder  
add (one or many) _.fbx_ files to **source** folder  
Go to **code** folder  
Run `pip install -r requirements.txt`to install dependencies  
Run `python main.py `in console.  

## Going short with only one _.fbx_ file
###(optional)
If you want to process only one .fbx file you can use `core.py` file with _Blender_ command.
It takes 3 arguments: import_scale, source fbx file path, export directory path,  
example:  
`Blender ../target/target.blend --background --python core.py -- 1 ../source/ ../exports`


## Retarget and burnout process step by step  
1. set object mode  
2. import fbx with scale=x using better fbx  
3. select collection "Armature"  
4. Open Action Editor  
5.Select animation from imported fbx  
-retarget and root burn goes automatically-  
6.select collection  "armature_NEW_Default"  
7.export fbx with preset, export_name = animation_name with suffix  

## Blender env path troubleshooting
Depending how you set your _blenderpath_ you may want to change first capital letter in Blender command.
To do this replace it in main.py:22  
In my case it works with both '**blender**' and '**Blender**' (big and small letter)


