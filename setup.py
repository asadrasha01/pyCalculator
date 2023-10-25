from setuptools import setup

APP = ['interface.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'plist': {
        'CFBundleName': "Calculator",
        'CFBundleDisplayName': "Calculator",
        'CFBundleGetInfoString': "Calculator",
        'CFBundleIdentifier': "com.yourname.calculator",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
