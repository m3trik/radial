-- 3ds Max startup script-------------------------------------------------------

-- Maxscipt startup order:
-- MacroScript (MCR) files in ui\macroscripts --not compiled at this time; rather they are just scanned to identify the MacroScripts that have been defined.

-- MAXScript (MS, MSE, and MZP) in the plug-in path directories/subdirectories, and compiles these files. (specified in the Configure System Paths dialog and Configure User Paths dialog)
-- The base scene and user interface have not been created at this point, so no viewport or scene commands should be executed in these files.

-- You can prevent a nested directory from being scanned by placing its name in parentheses, for example "(old-versions)"

-- 3ds Max creates the base scene and user interface. Any macro scripts used by buttons in the user interface are compiled at this time.

-- The automatic loading of the following startup script files can be deactivated by turning off the Auto Start MAXScript option in the MAXScript page of the Preferences dialog



--------------------------------------------------------------------------------
-- MAXScript searches for startup.ms in this order: (stop searching when found)

-- The Scripts directory (defined on the Configure User Paths dialog  File I/O panel)
-- The Startup Scripts directory (defined on the Configure System Paths dialog)
-- The 3ds Max executable main directory
-- The Windows system directory (system32)
-- The Windows directory
-- The directories that are listed in the PATH environment variable

-- MAXScript then recursively scans the Startup Scripts directory (defined on the Configure System Paths dialog) and any nested directories for .ms, .mse, and .mzp script files and loads them.

-- If you specify a script to run in the command line (-U MAXScript script_name)

--------------------------------------------------------------------------------
-- 3ds Max looks for the Python script under the following directories:

-- User Scripts directory
-- User Startup Scripts directory
-- Scripts directory
-- Startup Scripts
-- Windows paths specified by the Path environment variable.

--------------------------------------------------------------------------------


-- initalize python
python.Init()
python.Execute("import sys, os")

-- get directory paths
file_path = getSourceFileName() --ie. "C:\__portable\_scripts\apps\max\startup\startup.ms"
startup_dir = getFilenamePath(file_path) --ie. "C:\__portable\_scripts\apps\max\startup"

root_dir = substring startup_dir 1 (findString startup_dir ("apps")-2) --take substring from index 1 to the index of max in file string. ie. "O:\Cloud\Code\_scripts\radial\radial"

app_scripts_dir	= root_dir+"/apps/max" --ie. "O:\Cloud\Code\_scripts\radial\radial/apps/max"
app_slots_dir = app_scripts_dir+"/slots" --ie. "O:\Cloud\Code\_scripts\radial\radial/apps/max/slots"


-- exec userSetup.py
python.ExecuteFile(startup_dir+"/userSetup.py") --3ds Max looks for the Python script under: User Scripts directory, User Startup Scripts directory, Scripts directory, Startup Scripts, Windows paths specified by the Path environment variable.


-- -----------------------------------------------------------------------------

-- fn replace_ mStream mFromStr mToStr mIgnoreCase:false =
-- (
-- 	regex = dotnetclass "system.text.regularexpressions.regex"
-- 	pattern = "\b" + mFromStr + "\b"
-- 	if mIgnoreCase do pattern = "(?i)" + pattern
	
-- 	result = regex.replace mStream pattern mToStr
-- 	return (result as stringstream)
-- )



-- -----------------------------------------------------------------------------

function PerformDelayedTasks sender evt = (
	/*
	Delayed Tasks:

	Any commands within this function body will be delayed by the set amount.

	ex. usage:
	delayTimer = dotnetobject "Windows.Forms.Timer"
	delayTimer.Interval=5000

	dotnet.AddEventHandler delayTimer "Tick" PerformDelayedTasks

	delayTimer.enabled = true
	*/

	sender.enabled = false --important: don't repeat this timer event
	dotnet.RemoveEventHandler sender "Elapsed" PerformDelayedTasks --for sanity and cleanup

	-- commands --

	-- user macros:
	FileIn (app_scripts_dir+"/macros.ms")

	-- statusPanel
	statusPanel.visible = true

-- 	-- open the layer explorer
-- 	if sceneexplorermanager.ExplorerExists "Layer Explorer" then
-- 	(
-- 		if (not sceneexplorermanager.ExplorerIsOpen "Layer Explorer") then
-- 			sceneexplorermanager.OpenExplorer "Layer Explorer"
-- 	)
-- 	else
-- 	(
-- 		sceneexplorermanager.CreateExplorerFromDefault "Layer Explorer"
-- 	)


	-- hotkeys:
	kbdx = actionMan.getKeyboardFile()	--get current keyboard file
	actionMan.loadKeyboardFile (kbdx)		--loadKeyboardFile()
	-- actionMan.saveKeyboardFile		--saveKeyboardFile()
)



delayTimer = dotnetobject "Windows.Forms.Timer"
delayTimer.Interval=5000

dotnet.AddEventHandler delayTimer "Tick" PerformDelayedTasks

delayTimer.enabled = true


-- -----------------------------------------------------------------------------

















-- -----------------------------------------------------------------------------
-- Notes:
-- -----------------------------------------------------------------------------


-- -----------------------------------------------------------------------------
-- depricated:

--get current dir path:
-- filePath = getThisScriptFilename() --ie. "C:\__portable\_scripts\apps\max\startup\startup.ms"
-- root_dir = substring filePath 1 (findString filePath ("apps")-2) --take substring from index 1 to the index of max in file string

-- ui_dir = root_dir+"/ui"
-- app_scripts_dir	= root_dir+"/apps/max"
-- app_slots_dir = app_scripts_dir+"/slots"
-- startup_dir = app_scripts_dir+"/startup"

-- --append to system path:
-- paths = #(root_dir, ui_dir, app_scripts_dir, app_slots_dir, startup_dir)


-- python.Execute "import sys"
-- for path_ in paths do (
-- 	python.Execute ("sys.path.append('"+path_+"')")
-- )
-- -- python.Execute("print 'system paths:'; for p in sys.path: print p") --print system paths



--absolute path:
-- USERPROFILE = systemTools.getEnvVariable("USERPROFILE")
-- path_ = USERPROFILE+"\\Documents\\_portable\\_scripts\\__path\\max\\"
-- if not (doesFileExist path_) do
-- (
-- 	CLOUD = systemTools.getEnvVariable("CLOUD")
-- 	path_ = CLOUD+"\\____Graphics\\__general\\_portable\\_scripts\\__path\\max\\"
-- )


-- # ------------------------------------------------
-- # Get the main Max window as a QtGui.QMainWindow instance.
-- # ------------------------------------------------
-- # mainWindow = MaxPlus.GetQMaxMainWindow()


-- # ------------------------------------------------
-- # MaxPlus.FileManager.Reset(True)



-- #Append directory to system path -----------------

-- #add absolute paths:
-- # paths = [
-- # r'%CLOUD%/____Graphics/__general/_portable/_scripts/__path',
-- # r'%CLOUD%/____Graphics/__general/_portable/_scripts/__path/ui',
-- # r'%CLOUD%/____Graphics/__general/_portable/_scripts/__path/max',
-- # r'%CLOUD%/____Graphics/__general/_portable/_scripts/__path/max/slots',

-- # r'%USERPROFILE%/Documents/_portable/_scripts/__path',
-- # r'%USERPROFILE%/Documents/_portable/_scripts/__path/ui',
-- # r'%USERPROFILE%/Documents/_portable/_scripts/__path/max',
-- # r'%USERPROFILE%/Documents/_portable/_scripts/__path/max/slots'
-- # ]

-- # for path in paths:
-- # 	sys.path.append(os.path.expandvars(path)); #print '%PYTHONPATH%:', path


-- # for s in  sys.path: print s




-- #load main_max ------------------------------------

-- # if 'main_max' not in sys.modules:
-- # 	import main_max
-- # else:
-- # 	print "reload: main_max"
-- # 	reload(main_max)



-- #------------------------------------------------------------------------------