# !/usr/bin/python
# coding=utf-8
import os.path

from max_init import *



class Rigging(Init):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def draggable_header(self, state=None):
		'''Context menu
		'''
		dh = self.rigging_ui.draggable_header

		if state is 'setMenu':
			dh.contextMenu.add(wgts.ComboBox, setObjectName='cmb000', setToolTip='')
			return


	def cmb000(self, index=-1):
		'''Editors
		'''
		cmb = self.rigging_ui.cmb000

		if index is 'setMenu':
			list_ = ['Bone Tools','Parameter Editor','Parameter Collector','Parameter Wire Dialog']
			cmb.addItems_(list_, 'Rigging Editors')
			return

		if index>0:
			text = cmb.items[index]
			if text=='Bone Tools':
				maxEval('macros.run "Animation Tools" "BoneAdjustmentTools"')
			elif text=='Parameter Editor':
				maxEval('macros.run "Customize User Interface" "Custom_Attributes"')
			elif text=='Parameter Collector':
				maxEval('macros.run "Parameter Collector" "ParamCollectorShow"')
			elif text=='Parameter Wire Dialog':
				maxEval('macros.run "Parameter Wire" "paramWire_dialog"')
			cmb.setCurrentIndex(0)


	def cmb001(self, index=-1):
		'''Create
		'''
		cmb = self.rigging_ui.cmb001

		if index is 'setMenu':
			list_ = ['Bones IK Chain','Point','Dummy','Grid','Expose Transform','Lattice','Biped']
			cmb.addItems_(list_, "Create")
			return

		if index>0:
			text = cmb.items[index]
			if text=='Bones IK Chain':
				maxEval('macros.run "Inverse Kinematics" "Bones"') #create joint tool
			elif text=='Point':
				maxEval('macros.run "Objects Helpers" "Point"') #Point pos:[46.5545,-11.1098,0] isSelected:on #locator
			elif text=='Dummy':
				maxEval('macros.run "Objects Helpers" "Dummy"')
			elif text=='Grid':
				maxEval('macros.run "Objects Helpers" "Grid"') #grid pos:[14.957,-79.0478,0] isSelected:on width:49.0621 length:51.0787
			elif text=='Expose Transform':
				maxEval('macros.run "Objects Helpers" "ExposeTM"') #ExposeTm pos:[1.12888,-35.9943,0] isSelected:on
			elif text=='Lattice':
				maxEval('modPanel.addModToSelection (Lattice ()) ui:on') #create lattice
			elif text=='macros.run "Objects Systems" "Biped"':
				maxEval('macros.run "Objects Systems" "Biped"')
			cmb.setCurrentIndex(0)


	def chk000(self, state=None):
		'''Scale Joint
		'''
		self.toggleWidgets(setUnChecked='chk001-2')
		# self.rigging_ui.tb000.menu_.s000.setValue(pm.jointDisplayScale(query=1)) #init global joint display size


	def chk001(self, state=None):
		'''Scale IK
		'''
		self.toggleWidgets(setUnChecked='chk000, chk002')
		# self.rigging_ui.s000.setValue(pm.ikHandleDisplayScale(query=1)) #init IK handle display size
		

	def chk002(self, state=None):
		'''Scale IK/FK
		'''
		self.toggleWidgets(setUnChecked='chk000-1')
		# self.rigging_ui.s000.setValue(pm.jointDisplayScale(query=1, ikfk=1)) #init IKFK display size


	def s000(self, value=None):
		'''Scale Joint/IK/FK
		'''
		value = self.rigging_ui.s000.value()

		# if self.rigging_ui.chk000.isChecked():
		# 	pm.jointDisplayScale(value) #set global joint display size
		# elif self.rigging_ui.chk001.isChecked():
		# 	pm.ikHandleDisplayScale(value) #set global IK handle display size
		# else: #self.rigging_ui.chk002.isChecked():
		# 	pm.jointDisplayScale(value, ikfk=1) #set global IKFK display size


	@Slots.message
	def tb000(self, state=None):
		'''Toggle Display Local Rotation Axes
		'''
		tb = self.current_ui.tb000
		if state is 'setMenu':
			tb.menu_.add('QCheckBox', setText='Joints', setObjectName='chk000', setChecked=True, setToolTip='Display Joints.')
			tb.menu_.add('QCheckBox', setText='IK', setObjectName='chk001', setChecked=True, setToolTip='Display IK.')
			tb.menu_.add('QCheckBox', setText='IK\\FK', setObjectName='chk002', setChecked=True, setToolTip='Display IK\\FK.')
			tb.menu_.add('QDoubleSpinBox', setPrefix='Tolerance: ', setObjectName='s000', setMinMax_='0.00-10 step.5', setValue=1.0, setToolTip='Global Display Scale for the selected type.')
			
			self.chk000() #init scale joint value
			return

		# joints = pm.ls(type="joint") #get all scene joints

		# state = pm.toggle(joints[0], query=1, localAxis=1)
		# if tb.menu_.isChecked():
		# 	if not state:
		# 		toggle=True
		# else:
		# 	if state:
		# 		toggle=True

		# if toggle:
		# 	pm.toggle(joints, localAxis=1) #set display off

		# return 'Display Local Rotation Axes:<hl>'+str(state)+'</hl>'


	def tb001(self, state=None):
		'''Orient Joints
		'''
		tb = self.current_ui.tb001
		if state is 'setMenu':
			tb.menu_.add('QCheckBox', setText='Align world', setObjectName='chk003', setToolTip='Align joints with the worlds transform.')
			return

		# orientJoint = 'xyz' #orient joints
		# if tb.menu_.isChecked():
		# 	orientJoint = 'none' #orient joint to world

		# pm.joint(edit=1, orientJoint=orientJoint, zeroScaleOrient=1, ch=1)


	def tb002(self, state=None):
		'''Constraint: Parent
		'''
		tb = self.current_ui.tb002
		if state is 'setMenu':
			tb.menu_.add('QCheckBox', setText='Template Child', setObjectName='chk004', setChecked=False, setToolTip='Template child object(s) after parenting.')		
			return

		template = tb.menu_.chk004.isChecked()

		objects = list(Init.bitArrayToArray(rt.selection))

		for obj in objects[:-1]:
			obj.parent = objects[-1]

			if template:
				obj.isFrozen = True


	@Slots.message
	def tb003(self, state=None):
		'''Create Locator at Selection
		'''
		tb = self.current_ui.tb003
		if state is 'setMenu':
			tb.menu_.add('QLineEdit', setPlaceholderText='Suffix:', setText='', setObjectName='t000', setToolTip='A string appended to the end of the created locators name.')
			tb.menu_.add('QCheckBox', setText='Strip Digits', setObjectName='chk005', setChecked=True, setToolTip='Strip numeric characters from the string. If the resulting name is not unique, maya will append a trailing digit.')
			tb.menu_.add('QLineEdit', setPlaceholderText='Strip:', setText='_GEO', setObjectName='t001', setToolTip='Strip a specific character set from the locator name. The locators name is based off of the selected objects name.')
			tb.menu_.add('QCheckBox', setText='Parent', setObjectName='chk006', setChecked=True, setToolTip='Parent to object to the locator.')
			tb.menu_.add('QDoubleSpinBox', setPrefix='Scale: ', setObjectName='s001', setMinMax_='.000-1000 step1', setValue=1, setToolTip='The scale of the locator.')
			tb.menu_.add('QCheckBox', setText='Freeze Child Transforms', setObjectName='chk010', setChecked=True, setToolTip='Freeze transforms on the child object. (Valid only with parent flag).')
			tb.menu_.add('QCheckBox', setText='Bake Child Pivot', setObjectName='chk011', setChecked=True, setToolTip='Bake pivot positions on the child object. (Valid only with parent flag).')
			tb.menu_.add('QCheckBox', setText='Lock Child Translate', setObjectName='chk007', setChecked=True, setToolTip='Lock the translate values of the child object.')
			tb.menu_.add('QCheckBox', setText='Lock Child Rotation', setObjectName='chk008', setChecked=True, setToolTip='Lock the rotation values of the child object.')
			tb.menu_.add('QCheckBox', setText='Lock Child Scale', setObjectName='chk009', setChecked=False, setToolTip='Lock the scale values of the child object.')
			return

		suffix = tb.menu_.t000.text()
		stripDigits = tb.menu_.chk005.isChecked()
		strip = tb.menu_.t001.text()
		parent = tb.menu_.chk006.isChecked()
		scale = tb.menu_.s001.value()
		lockTranslate = tb.menu_.chk007.isChecked()
		lockRotation = tb.menu_.chk008.isChecked()
		lockScale = tb.menu_.chk009.isChecked()
		freezeChildTransforms = tb.menu_.chk010.isChecked()
		bakeChildPivot = tb.menu_.chk011.isChecked()

		Rigging.createLocatorAtSelection(suffix=suffix, stripDigits=stripDigits, strip=strip, scale=scale, parent=parent, bakeChildPivot=bakeChildPivot, freezeChildTransforms=freezeChildTransforms, lockTranslate=lockTranslate, lockRotation=lockRotation, lockScale=lockScale)


	def b001(self):
		'''Connect Joints
		'''
		pm.connectJoint(cm=1)


	def b002(self):
		'''Insert Joint Tool
		'''
		pm.setToolTo('insertJointContext') #insert joint tool


	def b004(self):
		'''Reroot
		'''
		pm.reroot() #re-root joints


	def b006(self):
		'''Constraint: Point
		'''
		pm.pointConstraint(offset=[0,0,0], weight=1)


	def b007(self):
		'''Constraint: Scale
		'''
		pm.scaleConstraint(offset=[1,1,1], weight=1)


	def b008(self):
		'''Constraint: Orient
		'''
		pm.orientConstraint(offset=[0,0,0], weight=1)


	def b009(self):
		'''Constraint: Aim
		'''
		pm.aimConstraint(offset=[0,0,0], weight=1, aimVector=[1,0,0], upVector=[0,1,0], worldUpType="vector", worldUpVector=[0,1,0])


	def b010(self):
		'''Constraint: Pole Vector
		'''
		pm.orientConstraint(offset=[0,0,0], weight=1)


	@staticmethod
	def createLocatorAtSelection(suffix='_LOC', stripDigits=False, strip='', parent=False, freezeChildTransforms=False, bakeChildPivot=False, scale=1, lockTranslate=False, lockRotation=False, lockScale=False, _fullPath=False):
		'''Create locators with the same transforms as any selected object(s).
		If there are vertices selected it will create a locator at the center of the selected vertices bounding box.

		:Parameters:
			suffix (str) = A string appended to the end of the created locators name. (default: '_LOC') '_LOC#'
			stripDigits (bool) = Strip numeric characters from the string. If the resulting name is not unique, maya will append a trailing digit. (default=False)
			strip (str) = Strip a specific character set from the locator name. The locators name is based off of the selected objects name. (default=None)
			scale (float) = The scale of the locator. (default=1)
			parent (bool) = Parent to object to the locator. (default=False)
			freezeChildTransforms (bool) = Freeze transforms on the child object. (Valid only with parent flag) (default=False)
			bakeChildPivot (bool) = Bake pivot positions on the child object. (Valid only with parent flag) (default=False)
			lockTranslate (bool) = Lock the translate values of the child object. (default=False)
			lockRotation (bool) = Lock the rotation values of the child object. (default=False)
			lockScale (bool) = Lock the scale values of the child object. (default=False)
			_fullPath (bool) = Internal use only (recursion). Use full path names for Dag objects. This can prevent naming conflicts when creating the locator. (default=False)

		ex. call:
			createLocatorAtSelection(strip='_GEO', suffix='', stripDigits=1, freezeChildTransforms=1, bakeChildPivot=1, parent=1, lockTranslate=1, lockRotation=1)
		'''
		import pymel.core as pm
		sel = pm.ls(selection=True, long=_fullPath)
		sel_verts = pm.filterExpand(sm=31)

		if not sel:
			error = '# Error: Nothing Selected. #'
			print (error)
			return error

		def _formatName(name, stripDigits=stripDigits, strip=strip, suffix=suffix):
			if stripDigits:
				name_ = ''.join([i for i in name if not i.isdigit()])	
			return name_.replace(strip, '')+suffix

		def _parent(obj, loc, parent=parent, freezeChildTransforms=freezeChildTransforms, bakeChildPivot=bakeChildPivot):
			if parent: #parent
				if freezeChildTransforms:
					pm.makeIdentity(obj, apply=True, t=1, r=1, s=1, normal=2) #normal parameter: 1=the normals on polygonal objects will be frozen. 2=the normals on polygonal objects will be frozen only if its a non-rigid transformation matrix.
				if bakeChildPivot:
					pm.select(obj); pm.mel.BakeCustomPivot() #bake pivot on child object.
				objParent = pm.listRelatives(obj, parent=1)
				pm.parent(obj, loc)
				pm.parent(loc, objParent)

		def _lockChildAttributes(obj, lockTranslate=lockTranslate, lockRotation=lockRotation, lockScale=lockScale):
			if lockTranslate: #lock translation values
				[pm.setAttr('{}.{}'.format(obj, attr), lock=True) for attr in ('tx','ty','tz')]

			if lockRotation: #lock rotation values
				[pm.setAttr('{}.{}'.format(obj, attr), lock=True) for attr in ('rx','ry','rz')]
					
			if lockScale: #lock scale values
				[pm.setAttr('{}.{}'.format(obj, attr), lock=True) for attr in ('sx','sy','sz')]

		_fullPath = lambda: Rigging.createLocatorAtSelection(suffix=suffix, stripDigits=stripDigits, 
					strip=strip, parent=parent, scale=scale, _fullPath=True, 
					lockTranslate=lockTranslate, lockRotation=lockRotation, lockScale=lockScale)

		pm.undoInfo(openChunk=1)

		if sel_verts: #vertex selection

			objName = sel_verts[0].split('.')[0]
			locName = _formatName(objName, stripDigits, strip, suffix)

			loc = pm.spaceLocator(name=locName)
			if not any([loc, _fullPath]): #if locator creation fails; try again using the objects full path name.
				_fullPath()

			pm.scale(scale, scale, scale)

			bb = pm.exactWorldBoundingBox(sel_verts)
			pos = ((bb[0] + bb[3]) / 2, (bb[1] + bb[4]) / 2, (bb[2] + bb[5]) / 2)
			pm.move(pos[0], pos[1], pos[2], loc)

			_parent(objName, loc)
			_lockChildAttributes(objName)

		else: #object selection
			for obj in sel:

				objName = obj.name()
				locName = _formatName(objName, stripDigits, strip, suffix)

				loc = pm.spaceLocator(name=locName)
				if not any([loc, _fullPath]): #if locator creation fails; try again using the objects fullpath name.
					_fullPath()

				pm.scale(scale, scale, scale)

				tempConst = pm.parentConstraint(obj, loc, mo=False)
				pm.delete(tempConst)
				pm.select(clear=True)

				_parent(obj, loc)
				_lockChildAttributes(obj)

		pm.undoInfo(closeChunk=1)









#module name
print(os.path.splitext(os.path.basename(__file__))[0])
# -----------------------------------------------
# Notes
# -----------------------------------------------