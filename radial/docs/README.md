###### *PySide marking menu style layered ui and toolkit for maya and max.
*work in progress..*

## Design:
######
*This is a cross-platform, modular, marking menu style ui based on a QStackedWidget. Constructed dynamically for minimal overhead, naming convention and directory structure allows for a stacked ui to be constructed, signals added/removed as needed, and a master dictionary (switchboard module) to be created, which provides convenience methods that allow for getting/setting of relevant data across modules.*

![alt text](https://raw.githubusercontent.com/m3trik/radial/docs/toolkit_demo.gif)
*Example re-opening the last scene, renaming a material, and selecting geometry by that material.


##
-----------------------------------------------
 Structure:
-----------------------------------------------

![alt text](https://raw.githubusercontent.com/m3trik/radial/docs/dependancy_graph.jpg)


#### main:
###### *handles main gui construction.*

#### childEvents:
###### *event handling for child widgets.*

#### overlay:
###### *tracks cursor position and ui hierarchy to generate paint events that overlay the main widget.*

#### switchboard:
###### *contains a master dictionary for widget related info as well as convienience classes for interacting with the dict.*

#### slots:
###### *parent class holding methods that are inherited across all app specific slot class modules.*



##
-----------------------------------------------
 Installation:
-----------------------------------------------
######
(Assuming the default windows directory structure).

In maya:
* add \apps\maya\slots directory to maya.env
 (MAYA_SCRIPT_PATH=<dir>)
 
In 3ds Max:
* add \apps\max\startup directory to system path by navigating in app to:
 main menu> customize> additional startup scripts


Launching the menu:
The default hotkey for launching the menu set is f12. (I remap f12 to the windows key) 
This can be changed by passing the desired key value to the 'key_show" argument when calling an instance of the main module:
ex. call:
```
	from PySide2 import QtCore
	def hk_main_show():
		'''
		hk_main_show
		Display main marking menu.
		'''
		if 'main' not in locals() and 'main' not in globals():
			from main_maya import Instance
			main = Instance(key_show=QtCore.Qt.Key_Z) #holding the Z key will show the menu.

		main.show_()
```

Adding additional ui's:
* Drop a qt designer ui file into the ui folder.
* Add a shortcut somewhere in the 'main' ui (with the ui name in the 'whats this' attribute).
* Create corresponding class of the same name following the naming convention and inheritance of existing slot modules.  
