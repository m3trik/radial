# !/usr/bin/python
from __future__ import print_function, absolute_import
import os.path, sys



#max python path----------------------------------------------------
import inspect
file_path = inspect.getfile(lambda: None)
root_dir = file_path.replace('\\apps\\max\\startup\\userSetup.py', '', 1)
parent_dir = root_dir.replace('\\radial', '', 1)

app_scripts_dir	= os.path.join(root_dir, 'apps', 'max')
app_slots_dir = os.path.join(app_scripts_dir, 'slots')

#append to system path:
paths = [root_dir, parent_dir, app_scripts_dir, app_slots_dir]
for path in paths:
	sys.path.append(path)

# debug:
# for p in sys.path: print (p) #list all directories on the system environment path.
# print ('root_dir:		', root_dir)
# print ('parent_dir:		', parent_dir)
# print ('app_scripts_dir:', app_scripts_dir)
# print ('app_slots_dir:	', app_slots_dir)






# ------------------------------------------------
# Notes:
# ------------------------------------------------



# ------------------------------------------------
# deprecated: