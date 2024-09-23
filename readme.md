https://mkvtoolnix.download/downloads.html#ubuntu

```shell
// Add repo first

apt-get update
sudo apt install apt-transport-https mkvtoolnix mkvtoolnix-gui
```


```shell
py -m venv .venv

.venv\Scripts\activate.bat


pip install setuptools 

pypiwin32 
# Need to run as admin
python .venv/Scripts/pywin32_postinstall.py -install
(.venv) c:\Sandbox\test>python .venv/Scripts/pywin32_postinstall.py -install
Parsed arguments are: Namespace(install=True, remove=False, wait=None, silent=False, quiet=False, destination='c:\\Sandbox\\test\\.venv\\Lib\\site-packages')
Copied pythoncom312.dll to C:\WINDOWS\system32\pythoncom312.dll
Copied pywintypes312.dll to C:\WINDOWS\system32\pywintypes312.dll
Registered: Python.Interpreter
Registered: Python.Dictionary
Registered: Python
-> Software\Python\PythonCore\3.12\Help[None]=None
-> Software\Python\PythonCore\3.12\Help\Pythonwin Reference[None]='c:\\Sandbox\\test\\.venv\\Lib\\site-packages\\PyWin32.chm'
Registered help file
Pythonwin has been registered in context menu
Shortcut for Pythonwin created
Shortcut to documentation created
The pywin32 extensions were successfully installed.
```


links
- https://stackoverflow.com/questions/31507038/python-how-to-read-windows-media-created-date-not-file-creation-date
- https://stackoverflow.com/questions/61713787/reading-and-writing-windows-tags-with-python-3