
IF EXIST C:\Python31\pythonw.exe GOTO PYTHON31
IF EXIST C:\Python32\pythonw.exe GOTO PYTHON32
IF EXIST C:\Python33\pythonw.exe GOTO PYTHON33
IF EXIST C:\Python34\pythonw.exe GOTO PYTHON34
IF EXIST C:\Python35\pythonw.exe GOTO PYTHON35
IF EXIST C:\Python36\pythonw.exe GOTO PYTHON36
IF EXIST C:\Python37\pythonw.exe GOTO PYTHON37
IF EXIST C:\Python38\pythonw.exe GOTO PYTHON38
IF EXIST C:\Python39\pythonw.exe GOTO PYTHON39
IF EXIST C:\Python3\pythonw.exe GOTO PYTHON3
IF EXIST C:\Python\pythonw.exe GOTO PYTHON


python ohmterm.py %*
GOTO END

:PYTHON31
start C:\Python31\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON32
start C:\Python32\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON33
start C:\Python33\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON34
start C:\Python34\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON35
start C:\Python35\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON36
start C:\Python36\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON37
start C:\Python37\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON38
start C:\Python38\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON39
start C:\Python39\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON3
start C:\Python3\pythonw.exe ohmterm.py %*
GOTO END

:PYTHON
start C:\Python\pythonw.exe ohmterm.py %*
GOTO END





:END