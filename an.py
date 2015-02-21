# A window test.

import os
import struct
import sys
import traceback
import binascii
import codecs
import fth
from xml.etree import ElementTree as etree
global self
global cats

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QGuiApplication, QClipboard
Qt = QtCore.Qt


class Window(QtWidgets.QMainWindow):
    global cats
    """
    Main Window
    """
    
    def __init__(self, parent=None):
        global cats
        """
        The initializer
        """
        super().__init__(parent)
        uic.loadUi('an.ui', self)
        self.valueslide.setTickInterval(0.25)
        # self.preLoaded.hide()
        

        self.loadXML()
        self.addHacks()

        return
    

    def loadXML(self):
        global cats
        """
        Loads the xml
        """
        tree = etree.parse('an.xml')
        root = tree.getroot()
        if root.tag.lower() != 'hacks': raise ValueError

        cats = {}
        for categoryTag in root:
            if categoryTag.tag.lower() != 'category': raise ValueError
            catName = categoryTag.attrib['name']

            cat = {}
            for hackTag in categoryTag:
                if hackTag.tag.lower() != 'hack': raise ValueError
                h = Hack(hackTag)
                cat[h.name] = h

            cats[catName] = cat

        self.categories = cats
        # print(cats) dev poop
        # print(riivoxmltemplate) even MORE dev poop

    def addHacks(self):
        '''
        Updates our list widget with the hacks in the XML.
        '''
        for hack in self.categories:
            for mod in self.categories[hack]:
                item = QtWidgets.QListWidgetItem(mod)
                item.setData(QtCore.Qt.UserRole, self.categories[hack][mod])
                self.listWidget.addItem(item)


    
        # Also setting self.currentlySelected to our currently selected item (duh)
        self.currentlySelected = self.listWidget.currentItem()

        '''
        Changing the info on the right when a hack is selected...
        '''
        self.listWidget.itemSelectionChanged.connect(self.changeHackModifier)
        self.valuespin.valueChanged.connect(self.valueModifiersChangedSpin)
        self.valueslide.valueChanged.connect(self.valueModifiersChangedSlide)
        self.hexarea.textChanged.connect(self.valueModifiersChangedHex)
        self.riiexport.clicked.connect(self.generateRiivoXML)
        self.to0.clicked.connect(self.toZeroPress)

    
    def changeHackModifier(self):
        global modvalue
        global addressntsc
        global addresspal
        global currentmodname
		# global original
        # Update our title and description
        self.memtitle.setText(self.listWidget.currentItem().text())
        self.memdescription.setText(self.listWidget.currentItem().data(QtCore.Qt.UserRole).desc)
        currentmodname = self.listWidget.currentItem().text()
        
        # Update our offset
        addressntsc = self.listWidget.currentItem().data(QtCore.Qt.UserRole).modifiers[0].addrNTSC
        addresspal = self.listWidget.currentItem().data(QtCore.Qt.UserRole).modifiers[0].addrPAL
		# original = self.listWidget.currentItem().data(QtCore.Qt.UserRole).modifiers[0].orig
        print(addressntsc)
        
        # Enable all of our buttons
        self.valuespin.setEnabled(True)
        self.value.setEnabled(True)
        self.valueslide.setEnabled(True)
        self.riiexport.setEnabled(True)
        self.hexvalue.setEnabled(True)
        self.hexarea.setEnabled(True)
        self.to0.setEnabled(True)
        
        # Default the slider/spinner to 0
        self.valueslide.setValue(0.00)
        self.valuespin.setValue(0.00)
        self.hexarea.setText("0x00000000")
        modvalue = 0

    def valueModifiersChangedSpin(self):
        global modvalue
        modvalue = self.valuespin.value()
        modvaluehex = fth.floattohex(self.valuespin.value())
        self.valueslide.setValue(modvalue)
        self.hexarea.setText(modvaluehex)
        if modvaluehex == "0x0":
            self.hexarea.setText("0x00000000")

    def valueModifiersChangedSlide(self):
        global modvalue
        modvalue = self.valueslide.value()
        modvaluehex = fth.floattohex(self.valueslide.value())
        self.valuespin.setValue(modvalue)
        self.hexarea.setText(modvaluehex)
        if modvaluehex == "0x0":
            self.hexarea.setText("0x00000000")

    def valueModifiersChangedHex(self):
        global modvalue
        modvalue = int(fth.hextofloat(self.hexarea.text()))
        self.valuespin.setValue(float(modvalue))
        self.valueslide.setValue(int(modvalue))
    
    def toZeroPress(self):
        self.valueslide.setValue(0)
        self.valuespin.setValue(0.00)
        self.hexarea.setText("0x00000000")
        modvalue = 0

    def generateRiivoXML(self):
        global modvaluehex
        global riivoxmltemplate
        print("The Riivo XML button was pressed!")
        riivoxmltemplate = "<!--" + currentmodname + "-->\n<!--NTSC--><memory offset=\"%s\" value=\"%s\" />\n<!--PAL--><memory offset=\"%s\" value=\"%s\" />\n"
        # riivoxmltemplate = "<memory offset=\"%s\" value=\"%s\" />" old
        modvaluehex = fth.floattohex(modvalue)
        print(modvaluehex)
        popup = PopUp()
        popup.setWindowFlags(QtCore.Qt.Sheet)
        if popup.exec_() == QtWidgets.QDialog.Rejected:
            return



class Hack:
    """
    Defines a hack that can be toggled on or off.
    """
    def __init__(self, xmlTag):
        """
        Initializes the hack
        """
        self.name = xmlTag.attrib['name']
        self.desc = xmlTag.attrib['description']

        self.modifiers = []
        for modifierTag in xmlTag:
            if modifierTag.tag.lower() != 'modifier': raise ValueError
            self.modifiers.append(Modifier(modifierTag))
        '''for hackdesc in self.desc:
            for desc in self.desc[hackdesc]:
                print(desc)'''
        #print(self.desc) lotsa dev poop


class Modifier:
    """
    Defines a specific modification.
    """
    def __init__(self, xmlTag):
        """
        Initializes the modifier
        """
        self.type = xmlTag.attrib['type']
        self.name = xmlTag.attrib['name']
		# self.orig = xmlTag.attrib['original']
        self.addrNTSC = xmlTag.attrib['addressntsc']
        self.addrPAL = xmlTag.attrib['addresspal']

class PopUp(QtWidgets.QDialog):
    
    # Handles the pop-up window for when a code is exported to Riivo XML.
    
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('riivoxml.ui', self)
        self.codeout.setText(riivoxmltemplate % (addressntsc, modvaluehex, addresspal, modvaluehex))
        self.toclipboard.clicked.connect(self.copyToClipboard)
        return

    def copyToClipboard(self):
        print("Copied. (Not really.)")
        self.clipboardText = riivoxmltemplate % (addressntsc, modvaluehex, addresspal, modvaluehex)
        QGuiApplication.clipboard().setText(self.clipboardText)

def main():
    """
    Main
    """
    global app, window
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__': main()