import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\theja\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\theja\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="face1.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face1.ico",'tcl86t.dll','tk86t.dll', 'college_images','data','database','attendance_report']}},
    version = "2.0",
    description = "Face Recognition Automatic Attendance System | Developed By Thejas M and S Kumar Dhananjaya",
    executables = executables
    )