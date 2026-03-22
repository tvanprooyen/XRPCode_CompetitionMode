# XRPCode

A web code editor for the XRP using Blockly and micropython

Features:
* Code editor with Python syntax highlighting
* Shell for interacting with the XRP MicroPython REPL
* Output from running programs shown in shell
* Filesystem panel for observing and modifying files on the XRP's flash filesystem
* File upload and REPL interaction through webSerial
* All work immediately saved to page in case of accidental page refresh or browser exit
* Import and export files to and from the web IDE and PC
* Easy connect and disconnect of XRP
    * Automatically connects XRP if it has connected to the page before

Recent updates (v1.2.3):
* Added Competition Mode workspace with Control and Joystick tabs
* Competition action buttons are automatically disabled when XRP is not connected
* RUN button is disabled while Competition Mode is open to prevent conflicting runs
* Added bottom notification bar for important notices (including BLE MicroPython update notices)
* Header gamepad icon now uses Font Awesome and turns green while a mapped button is pressed

Compatibility notes:
* Project scripts are compatible with Python 3.12+

Only Google Chrome and Microsoft Edge are officially supported by the WebSerial JavaScript API

https://xrp.wpsrobotics.org/