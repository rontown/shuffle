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
		
		filters_list = ['*.png','*.jpg','*.img']
		# Create widgets
		self.pb_Browse = QPushButton("Open Directory")  
		self.pb_Browse.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		self.pb_Close = QPushButton("Close")
		self.pb_Close.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		self.treeViewLeft = QTreeView()	
		self.modelLeft = QFileSystemModel()
		self.modelLeft.setNameFilters(filters_list)
		self.treeViewLeft.setModel(self.modelLeft)
		self.treeViewRight = QTreeView()
		self.proxyModelRight = QSortFilterProxyModel()
		self.proxyModelRight.setSourceModel(self.modelLeft)


		# Create layout and add widgets
		layout_main = QGridLayout()
		#First Line
			#First Column
		layout_main.addWidget(self.pb_Browse,0,0)
		#Second Line
			#First Column
		layout_main.addWidget(self.treeViewLeft,1,0)
			#SecondColumn (3rd in fact)
		layout_main.addWidget(self.treeViewRight,1,1)
		#Third Line
			#Second Column
		layout_main.addWidget(self.pb_Close,2,1,Qt.AlignRight)
		
		# Set dialog layout
		self.setLayout(layout_main)

		# Add buttons
		self.pb_Browse.clicked.connect(self.browseDir)
		self.pb_Close.clicked.connect(self.close)
	
	def browseDir(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.Directory)
		dialog.setOption(QFileDialog.ShowDirsOnly)
		result = dialog.exec_()
		
		if result:
			self.modelLeft.setRootPath(dialog.selectedFiles()[0])
			self.treeViewLeft.setRootIndex(self.modelLeft.index(dialog.selectedFiles()[0]))
			print (dialog.selectedFiles())
    


 
 
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    interface = OrganizerInterface()
    interface.show()
    # Run the main Qt loop
    sys.exit(app.exec_())