import sys
import maya.OpenMaya as om
import maya.OpenMayaMPx as omMPx



kPluginCmdName = "Radial_Maya_plugin"


class Radial_Maya_plugin(omMPx.MPxCommand):
	'''Command
	'''
	def __init__(self):
		omMPx.MPxCommand.__init__(self)
		
	def doIt(self,argList):
		'''Invoked when the command is run.
		'''
		print("Radial_Maya_plugin")
		path = r'O:\Cloud\Code\_scripts\radial\radial\apps\maya'
		exec(open(path+'/userSetup.py').read())
		# pm.mel.evalDeferred('"python (\"exec(open(path+\'/userSetup.py\').read())\")" -lowestPriority;')


def cmdCreator():
	'''Creator
	'''
	return omMPx.asMPxPtr(Radial_Maya_plugin())


def initializePlugin(mobject):
	'''Initialize the script plug-in.
	'''
	mplugin = omMPx.MFnPlugin(mobject)
	try:
		mplugin.registerCommand(kPluginCmdName, cmdCreator)
	except:
		sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
		raise


def uninitializePlugin(mobject):
	'''Uninitialize the script plug-in.
	'''
	mplugin = omMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand( kPluginCmdName )
	except:
		sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)