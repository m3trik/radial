# !/usr/bin/python
# coding=utf-8
import os.path

from maya_init import *



class Animation(Init):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def draggable_header(self, state=None):
		'''Context menu
		'''
		dh = self.animation_ui.draggable_header

		if state is 'setMenu':
			dh.contextMenu.add(wgts.ComboBox, setObjectName='cmb000', setToolTip='')
			return


	def cmb000(self, index=-1):
		'''Editors
		'''
		cmb = self.animation_ui.cmb000
		
		if index is 'setMenu':
			list_ = ['']
			cmb.addItems_(list_, '')
			return

		if index>0:
			text = cmb.items[index]
			if text=='':
				mel.eval('')
			cmb.setCurrentIndex(0)


	def tb000(self, state=None):
		'''Set Current Frame
		'''
		tb = self.current_ui.tb000
		if state is 'setMenu':
			tb.menu_.add('QSpinBox', setPrefix='Frame: ', setObjectName='s000', setMinMax_='0-10000 step1', setValue=1, setToolTip='')
			tb.menu_.add('QCheckBox', setText='Relative', setObjectName='chk000', setChecked=True, setToolTip='')
			tb.menu_.add('QCheckBox', setText='Update', setObjectName='chk001', setChecked=True, setToolTip='')
			return

		frame = self.invertOnModifier(tb.menu_.s000.value())
		relative = tb.menu_.chk000.isChecked()
		update = tb.menu_.chk001.isChecked()

		Animation.setCurrentFrame(frame, relative=relative, update=update)


	def b000(self):
		''''''
		pass


	def b001(self):
		''''''
		pass


	def b002(self):
		''''''
		pass


	def b003(self):
		''''''
		pass


	def b004(self):
		''''''
		pass


	def b005(self):
		''''''
		pass


	def b006(self):
		''''''
		pass


	def b007(self):
		''''''
		pass


	def b008(self):
		''''''
		mel.eval("")


	def b009(self):
		''''''
		pass


	@staticmethod
	def setCurrentFrame(frame=1, relative=False, update=True):
		'''Set the current frame on the timeslider.

		:Parameters:
		frame (int) = Desired from number.
		relative (bool) = If True; the frame will be moved relative to 
			it's current position using the frame value as a move amount.
		update (bool) = Change the current time, but do not update the world. (default=True)

		ex. call:
			setCurrentFrame(24, relative=True, update=1)
		'''
		currentTime=0
		if relative:
			currentTime = pm.currentTime(query=True)

		pm.currentTime(currentTime+frame, edit=True, update=update)








#module name
print(os.path.splitext(os.path.basename(__file__))[0])
# -----------------------------------------------
# Notes
# -----------------------------------------------