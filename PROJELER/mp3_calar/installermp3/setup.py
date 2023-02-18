import sys
from cx_Freeze import setup, Executable


## mp3 örneğinde kullanılan
build_exe_options = {'packages':['os'], 'excludes':['tkinter']}

base = None
if sys.platform == 'win32' :
    base = 'Win32GUI'

setup(
    name = 'Müzik Çalar',
    version = '0.1',
    description = "MP3 Player",
    options = {"build_exe":build_exe_options},
    executables = [
        Executable(
            'mp3player.py', 
            copyright="Copyright (C) 2023 cx_Freeze",
            base = base, 
            icon='mp3.ico'
        )]
)

## cx-freeze .readthedocs.io daki örnek

# directory_table = [
#     ("ProgramMenuFolder", "TARGETDIR", "."),
#     ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
# ]

# msi_data = {
#     "Directory": directory_table,
#     "ProgId": [
#         ("Prog.Id", None, None, "This is a description", "IconId", None),
#     ],
#     "Icon": [
#         ("IconId", "mp3player.png"),
#     ],
# }

# build_exe_options = {'packages':['os'], "excludes": ["tkinter"], "include_msvcr": True}

# base = None
# if sys.platform == 'win32' :
#    base = 'Win32GUI'

# executables = [
#         Executable(
#             "mp3player.py",
#             copyright="Copyright (C) 2023 cx_Freeze",
#             base=base,
#             icon="mp3player.png",
#             shortcutName="My Program Name",
#             shortcutDir="MyProgramMenu",
#         ),
#     ]


# setup(
#     name="hello",
#     version="0.1",
#     description="Sample cx_Freeze script to test MSI arbitrary data stream",
#     executables=executables,
#     options={
#         "build_exe": build_exe_options,
#     },
# )

