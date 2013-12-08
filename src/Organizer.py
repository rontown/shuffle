#!/usr/bin/python
# -*- coding: utf-8 -*-

# Photos Organizer
# alpha version
# 07/12/2013

import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
class OrganizerInterface(QDialog):
	
	#Constructor
	def __init__(self, parent=None):
		super(OrganizerInterface, self).__init__(parent)
		self.setWindowTitle('Organizer')
		self.setMinimumSize(700,500)
		#self.resize(700, 500)
		# Create widgets
		self.pb_Browse = QPushButton("Open Directory")  
		self.pb_Browse.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		self.pb_Close = QPushButton("Close")
		self.pb_Close.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		self.treeViewLeft = QTreeView()	
		self.modelLeft = QFileSystemModel()
		self.treeViewLeft.setModel(self.modelLeft)
		


		# Create layout and add widgets
		layout_main = QGridLayout()
		#First Line
			#First Column
		layout_main.addWidget(self.pb_Browse,0,0)
		#Second Line
			#First Column
		layout_main.addWidget(self.treeViewLeft,1,0)
		#Third Line
			#First Column
		layout_main.addWidget(self.pb_Close,2,0,Qt.AlignRight)
		
		# Set dialog layout
		self.setLayout(layout_main)

		# Add button signal to greetings slot
		self.pb_Browse.clicked.connect(self.browseDir)
		self.pb_Close.clicked.connect(self.close)
	# Greets the user
	def browseDir(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.Directory)
		dialog.setOption(QFileDialog.ShowDirsOnly)
		result = dialog.exec_()
		
		if result:
			self.modelLeft.setRootPath(dialog.selectedFiles()[0])
			self.treeViewLeft.setRootIndex(self.modelLeft.index(dialog.selectedFiles()[0]))
			self.modelLeft.setRootPath("D:/Photos")
			print (dialog.selectedFiles())
    


 
 
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    interface = OrganizerInterface()
    interface.show()
    # Run the main Qt loop
    sys.exit(app.exec_())