import bpy



bl_info = {
	"name": "Radial-blender",
	"blender": (2, 80, 0),
	"category": "UI",
}


class Radial_Blender_plugin(bpy.types.Operator):
	'''Radial plugin for Blender.
	'''
	bl_idname = bl_info['name'] # Unique identifier for buttons and menu items to reference.
	bl_label = "Radial plugin" # Display name in the interface.
	bl_options = {'REGISTER', 'UNDO'} # Enable undo for the operator.

	def execute(self, context): # execute() is called when running the operator.
		'''Invoked when the command is run.
		'''
		print("Radial_Maya_plugin")
		path = r'O:\Cloud\Code\_scripts\radial\radial\apps\blender'
		exec(open(path+'/userSetup.py').read())

		return {'FINISHED'} # Lets Blender know the operator finished successfully.


def menu_func(self, context):
	'''
	'''
	self.layout.operator(Radial_Blender_plugin.bl_idname)


def register():
	'''Initialize the script plug-in.
	'''
	bpy.utils.register_class(Radial_Blender_plugin)
	bpy.types.VIEW3D_MT_object.append(menu_func) # Adds the new operator to an existing menu.


def unregister():
	'''Uninitialize the script plug-in.
	'''
	bpy.utils.unregister_class(Radial_Blender_plugin)






if __name__ == "__main__":
	# This allows you to run the script directly from Blender's Text editor
	# to test the add-on without having to install it.
	register()