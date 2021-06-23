@echo off

echo This file creates a folder named 'radial' in the Blender scripts/startup directory 
echo that is symlinked to the radial Blender startup folder so that it is read each time Blender starts.
echo This file must be executed from the radial blender startup dir.



:setvars
echo.
echo "Enter the directory location to Blenders 'scripts/startup' folder"
echo "(ie. C:\Program Files\Blender Foundation\Blender 2.93\2.93\scripts)"
set /p from=
setlocal
set to=%~dp0

goto main




:main
echo.
echo	1- Create junction: %from% %to%.
echo	2- Reset link directory locations.
echo	3- Exit

CHOICE /C:123

IF ERRORLEVEL 3 goto exit_
IF ERRORLEVEL 2 goto setvars
IF ERRORLEVEL 1 goto create




:create
ECHO/
mklink /J "%from%/radial" "%to%"

goto setvars



:exit_