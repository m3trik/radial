# !/usr/bin/python
# coding=utf-8
from __future__ import print_function, absolute_import
from builtins import super
import os.path

from max_init import *



class Editors(Init):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.dynLayout_ui = self.sb.getUi('dynLayout')
		self.stackedWidget = self.dynLayout_ui.stackedWidget

		self.editors_ui.v000.setText('')
		self.editors_ui.v001.setText('Scene Explorer')
		self.editors_ui.v002.setText('')
		self.editors_ui.v003.setText('Layer Manager')
		self.editors_ui.v004.setText('')
		self.editors_ui.v005.setText('Schematic View')
		self.editors_ui.v006.setText('Asset Tracking')


	def draggable_header(self, state=None):
		'''Context menu
		'''
		draggable_header = self.editors_ui.draggable_header

		if state is 'setMenu':
			draggable_header.contextMenu.add(wgts.ComboBox, setObjectName='cmb000', setToolTip='')
			return


	def tree000(self, wItem=None, column=None):
		''''''
		tree = self.editors_ui.tree000

		if wItem is 'setMenu':
			tree.expandOnHover = True
			# tree.convert(tree.getTopLevelItems(), 'QLabel') #construct the tree using the existing contents.

			l = ['General Editors', 'Modeling Editors', 'Animation Editors', 'Rendering Editors', 'Relationship Editors']
			[tree.add('QLabel', childHeader=s, setText=s) for s in l] #root

			l = ['Attribute Editor', 'Channel Box', 'Layer Editor', 'Content Browser', 'Tool Settings', 'Hypergraph: Hierarchy', 'Hypergraph: Connections', 'Viewport', 'Adobe After Effects Live Link', 'Asset Editor', 'Attribute Spread Sheet', 'Component Editor', 'Channel Control', 'Display Layer Editor', 'File Path Editor', 'Namespace Editor', 'Script Editor', 'Command Shell', 'Profiler', 'Evaluation Toolkit']
			[tree.add('QLabel', 'General Editors', setText=s) for s in l]

			l = ['Modeling Toolkit', 'Paint Effects', 'UV Editor', 'XGen Editor', 'Crease Sets']
			[tree.add('QLabel', 'Modeling Editors', setText=s) for s in l]
			
			l = ['Graph Editor', 'Time Editor', 'Trax Editor', 'Camera Sequencer', 'Dope Sheet', 'Quick Rig', 'HumanIK', 'Shape Editor', 'Pose Editor', 'Expression Editor']
			[tree.add('QLabel', 'Animation Editors', setText=s) for s in l]

			l = ['Render View', 'Render Settings', 'Hypershade', 'Render Setup', 'Light Editor', 'Custom Stereo Rig Editor', 'Rendering Flags', 'Shading Group Attributes']
			[tree.add('QLabel', 'Rendering Editors', setText=s) for s in l]

			l = ['Animation Layers', 'Camera Sets', 'Character Sets', 'Deformer Sets', 'Display Layers', 'Dynamic Relationships', 'Light Linking: Light Centric','Light Linking: Object Centric', 'Partitions', 'Render Pass Sets', 'Sets', 'UV Linking: Texture-Centric', 'UV Linking: UV-Centric', 'UV Linking: Paint Effects/UV', 'UV Linking: Hair/UV']
			[tree.add('QLabel', 'Relationship Editors', setText=s) for s in l]

			return

		if not any([wItem, column]): #refresh list items -----------------------------

			return

		widget = tree.getWidget(wItem, column)
		text = tree.getWidgetText(wItem, column)
		header = tree.getHeaderFromColumn(column)

		self.main.hide() #hide the menu before opening an external editor.

		if header=='General Editors':
			if text=='Attribute Editor':
				pm.mel.AttributeEditor()
			if text=='Channel Box':
				pm.mel.OpenChannelBox()
			if text=='Layer Editor':
				pm.mel.OpenLayerEditor()
			if text=='Content Browser':
				pm.mel.OpenContentBrowser()
			if text=='Tool Settings':
				pm.mel.ToolSettingsWindow()
			if text=='Hypergraph: Hierarchy':
				pm.mel.HypergraphHierarchyWindow()
			if text=='Hypergraph: Connections':
				pm.mel.HypergraphDGWindow()
			if text=='Viewport':
				pm.mel.DisplayViewport()
			if text=='Adobe After Effects Live Link':
				pm.mel.OpenAELiveLink()
			if text=='Asset Editor':
				pm.mel.AssetEditor()
			if text=='Attribute Spread Sheet':
				pm.mel.SpreadSheetEditor()
			if text=='Component Editor':
				pm.mel.ComponentEditor()
			if text=='Channel Control':
				pm.mel.ChannelControlEditor()
			if text=='Display Layer Editor':
				pm.mel.DisplayLayerEditorWindow()
			if text=='File Path Editor':
				pm.mel.FilePathEditor()
			if text=='Namespace Editor':
				pm.mel.NamespaceEditor()
			if text=='Script Editor':
				pm.mel.ScriptEditor()
			if text=='Command Shell':
				pm.mel.CommandShell()
			if text=='Profiler':
				pm.mel.ProfilerTool()
			if text=='Evaluation Toolkit':
				pm.mel.EvaluationToolkit()

		if header=='Modeling Editors':
			if text=='Modeling Toolkit':
				pm.mel.OpenModelingToolkit()
			if text=='Paint Effects':
				pm.mel.PaintEffectsWindow()
			if text=='UV Editor':
				pm.mel.TextureViewWindow()
			if text=='XGen Editor':
				pm.mel.OpenXGenEditor()
			if text=='Crease Sets':
				pm.mel.OpenCreaseEditor()

		if header=='Animation Editors':
			if text=='Graph Editor':
				pm.mel.GraphEditor()
			if text=='Time Editor':
				pm.mel.TimeEditorWindow()
			if text=='Trax Editor':
				pm.mel.CharacterAnimationEditor()
			if text=='Camera Sequencer':
				pm.mel.SequenceEditor()
			if text=='Dope Sheet':
				pm.mel.DopeSheetEditor()
			if text=='Quick Rig':
				pm.mel.QuickRigEditor()
			if text=='HumanIK':
				pm.mel.HIKCharacterControlsTool()
			if text=='Shape Editor':
				pm.mel.ShapeEditor()
			if text=='Pose Editor':
				pm.mel.PoseEditor()
			if text=='Expression Editor':
				pm.mel.ExpressionEditor()

		if header=='Rendering Editors':
			if text=='Render View':
				pm.mel.RenderViewWindow()
			if text=='Render Settings':
				pm.mel.RenderGlobalsWindow()
			if text=='Hypershade':
				pm.mel.HypershadeWindow()
			if text=='Render Setup':
				pm.mel.RenderSetupWindow()
			if text=='Light Editor':
				pm.mel.OpenLightEditor()
			if text=='Custom Stereo Rig Editor':
				pm.mel.OpenStereoRigManager()
			if text=='Rendering Flags':
				pm.mel.RenderFlagsWindow()
			if text=='Shading Group Attributes':
				pm.mel.ShadingGroupAttributeEditor()

		if header=='Relationship Editors':
			if text=='Animation Layers':
				pm.mel.AnimLayerRelationshipEditor()
			if text=='Camera Sets':
				pm.mel.CameraSetEditor()
			if text=='Character Sets':
				pm.mel.CharacterSetEditor()
			if text=='Deformer Sets':
				pm.mel.DeformerSetEditor()
			if text=='Display Layers':
				pm.mel.LayerRelationshipEditor()
			if text=='Dynamic Relationships':
				pm.mel.DynamicRelationshipEditor()
			if text=='Light Linking: Light Centric':
				pm.mel.LightCentricLightLinkingEditor()
			if text=='Light Linking: Object Centric':
				pm.mel.ObjectCentricLightLinkingEditor()
			if text=='Partitions':
				pm.mel.PartitionEditor()
			if text=='Render Pass Sets':
				pm.mel.RenderPassSetEditor()
			if text=='Sets':
				pm.mel.SetEditor()
			if text=='UV Linking: Texture-Centric':
				pm.mel.TextureCentricUVLinkingEditor()
			if text=='UV Linking: UV-Centric':
				pm.mel.UVCentricUVLinkingEditor()
			if text=='UV Linking: Paint Effects/UV':
				pm.mel.PFXUVSetLinkingEditor()
			if text=='UV Linking: Hair/UV':
				pm.mel.HairUVSetLinkingEditor()


	def cmb000(self, index=None):
		'''Editors
		'''
		cmb = self.editors_ui.cmb000
		
		if index is 'setMenu':
			list_ = ['']
			cmb.addItems_(list_, '')
			return

		if index>0:
			if index==cmb.items.index(''):
				pass
			cmb.setCurrentIndex(0)


	def getEditorWidget(self, name):
		'''Get a maya widget from a given name.

		:Parameters:
			name (str) = name of widget
		'''
		_name = '_'+name
		if not hasattr(self, _name):
			w = self.convertToWidget(name)
			self.stackedWidget.addWidget(w)
			setattr(self, _name, w)

		return getattr(self, _name)


	def showEditor(self, name, width=640, height=480):
		'''Show, resize, and center the given editor.

		:Parameters:
			name (str) = The name of the editor.
			width (int) = The editor's desired width.
			height (int) = The editor's desired height.

		:Return:
			(obj) The editor as a QWidget.
		'''
		w = self.getEditorWidget(name)

		self.main.setUi('dynLayout')
		self.stackedWidget.setCurrentWidget(w)
		self.main.resize(width, height)
		self.main.move(QtGui.QCursor.pos() - self.main.rect().center()) #move window to cursor position and offset from left corner to center

		return w


	def v000(self):
		'''Attributes
		'''
		maxEval('')


	def v001(self):
		'''Outliner
		'''
		maxEval('macros.run "Scene Explorer" "SESceneExplorer"')


	def v002(self):
		'''Tool
		'''
		maxEval('')


	def v003(self):
		'''Layers
		'''
		maxEval('macros.run "Layers" "LayerManager"')


	def v004(self):
		'''Channels
		'''
		maxEval('')


	def v005(self):
		'''Node Editor
		'''
		maxEval('schematicView.Open "Schematic View 3"')


	def v006(self):
		'''Dependancy Graph
		'''
		maxEval('macros.run "Asset Tracking System" "AssetTrackingSystemToggle"')








#module name
print(os.path.splitext(os.path.basename(__file__))[0])
# -----------------------------------------------
# Notes
# -----------------------------------------------