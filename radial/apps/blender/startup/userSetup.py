# !/usr/bin/python
# coding=utf-8
import os.path, sys

import bpy



#blender python path----------------------------------------------------
import inspect
file_path = inspect.getfile(lambda: None)
root_dir = file_path.replace('/apps/blender/startup', '', 1)
parent_dir = root_dir.replace('/radial', '', 1)

app_scripts_dir	= os.path.join(root_dir, 'apps', 'blender')
app_slots_dir = os.path.join(app_scripts_dir, 'slots')

#append to system path:
paths = [root_dir, parent_dir, app_scripts_dir, app_slots_dir]
for path in paths:
	sys.path.append(path)
# for p in sys.path: print (p) #list all directories on the system environment path.


#macros--------------------------------------------------------------
from macros import Macros
Macros().setMacros()






#--------------------------------------------------------------------





#--------------------------------------------------------------------
# Notes:
#--------------------------------------------------------------------

