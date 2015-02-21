"""
Usage:
    cd to it's directory
    python mac_setup.py py2app
"""
# How to get the app bundle to work:
# Once you run this file (as seen above), go to the dist folder -> Reggie Next.app and show the package contents. Inside the Contents folder, paste the PlugIns and Frameworks folders included in the APP-Package-Stuff folder. Next, open the Info.plist in the Contents folder with Xcode and open the PyMainFileNames array, and change the Item 0 String from '__boot__' to 'reggie'. The app bundle should now work. Enjoy!

from setuptools import setup
import os, sys, shutil


NAME = 'Assemble Next'
VERSION = '0.01 Private Beta'

plist = dict(
    CFBundleIconFile=NAME,
    CFBundleName=NAME,
    CFBundleShortVersionString=VERSION,
    CFBundleGetInfoString=' '.join([NAME, VERSION]),
    CFBundleExecutable=NAME,
    CFBundleIdentifier='RoadrunnerWMCAssemble',
)



APP = ['an.py']
DATA_FILES = ['an.ui', 'fth.py', 'an.xml', 'riivoxml.ui']
OPTIONS = {
 'argv_emulation': True,
# 'graph': True,
 'iconfile': 'assemble.icns',
 'plist': plist,
# 'xref': True,
 'includes': ['PyQt5', 'PyQt5.QtWidgets', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.uic', 'codecs', 'binascii', 'traceback', 'sys', 'os', 'struct', 'sip', 'PyQt5.QtDesigner'],
 'excludes': ['PyQt5.QtWebKit', 'PyQt5.QtNetwork', 'PyQt5.QtOpenGL',
            'PyQt5.QtScript', 'PyQt5.QtSql', 'PyQt5.QtTest', 'PyQt5.QtXml', 'PyQt5.phonon'],
 'compressed': 0,
 'optimize': 0
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
# (1) remove build files

# (2)  issue setup command

# (3) copy plugin
#plugin
"""print("copy plugins")
os.system("cp -r plugins dist/test.app/Contents/PlugIns")
os.system("cp qt.conf dist/test.app/Contents/Resources/qt.conf")

# (4) correct dylib references

appPath = "/Users/Malcolm/Documents/Reggie Next for Mac/Reggie-Next-master/dist/ReggieNext!.app"
qtPath = "/Applications/Qt/5.4/clang_64/lib"
pythonPath = "/Library/Frameworks/Python.framework/Versions/3.4/Resources/Python.app"

def iid(dylib):
    command = "install_name_tool -id @executable_path/../PlugIns/{dylib} {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath)
    os.system(command)

def icPython(dylib):
    command = "install_name_tool -change {pythonPath}/Python.framework/Versions/3.3/Python @executable_path/../Frameworks/Python.framework/Versions/3.3/Python {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath, pythonPath=pythonPath)
    os.system(command)

def icCore(dylib):
    command = "install_name_tool -change {qtPath}/lib/QtCore.framework/Versions/5/QtCore @executable_path/../Frameworks/QtCore.framework/Versions/5/QtCore {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath, qtPath=qtPath)
    os.system(command)

def update(dylib):
    iid(dylib)
    icPython(dylib)
    icCore(dylib)

#accessible
print("# update accessible")
update("accessible/libqtaccessiblequick.dylib")
update("accessible/libqtaccessiblewidgets.dylib")

#bearer
print("# update bearer")
update("bearer/libqcorewlanbearer.dylib")

#platform
print("# update platforms")
update("platforms/libqcocoa.dylib")   ## <-- you need it
update("platforms/libqminimal.dylib")"""



