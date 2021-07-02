# !/usr/bin/python
# coding=utf-8
import os.path, sys

import bpy



#blender python path----------------------------------------------------
# file_path = bpy.context.space_data.text.filepath.replace(r'\userSetup.py', '')
file_path = r'O:\Cloud\Code\_scripts\radial\radial\apps\blender\startup'
root_dir = file_path.replace(r'\apps\blender\startup', '', 1)
parent_dir = root_dir.replace(r'\radial', '', 1)

app_scripts_dir = os.path.join(root_dir, 'apps', 'blender')
app_slots_dir = os.path.join(app_scripts_dir, 'slots')

#append to system path:
paths = [file_path, root_dir, parent_dir, app_scripts_dir, app_slots_dir]
for path in paths:
	sys.path.append(path)
# for p in sys.path: print (p) #list all directories on the system environment path.






#--------------------------------------------------------------------

def register():
	bpy.app.handlers.load_post.append(None)

# -------------------------------------------------------------------


# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
# from time import sleep, time

# def party_later(kind='', n=''):
#     sleep(3)
#     return kind + n + ' party time!: ' + __name__

# def main():
#     with ProcessPoolExecutor() as proc_executor:
#         with ThreadPoolExecutor() as thread_executor:
#             start_time = time()
#             proc_future1 = proc_executor.submit(party_later, kind='proc', n='1')
#             proc_future2 = proc_executor.submit(party_later, kind='proc', n='2')
#             thread_future1 = thread_executor.submit(party_later, kind='thread', n='1')
#             thread_future2 = thread_executor.submit(party_later, kind='thread', n='2')
#             for f in as_completed([
#               proc_future1, proc_future2, thread_future1, thread_future2,]):
#                 print(f.result())
#             end_time = time()
#     print('total time to execute four 3-sec functions:', end_time - start_time)

# if __name__ == '__main__':
#     main()



def evalDeferred():
	'''Defer evaluation for the given amount of time.
	Runs as a separate process.
	'''
	import userSetup





from threading import Timer
t = Timer(3, evalDeferred, args=None, kwargs=None)
t.start()






#--------------------------------------------------------------------
# Notes:
#--------------------------------------------------------------------