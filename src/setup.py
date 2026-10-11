# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
                         "packages":['computer','configs','gameboard','gui_tools','handledico','human'],
                         "include_files":["..\data","..\images","../audio","..\README.md","Licence_gpl-3.0.txt"],
                         "excludes": ["..\old_files","..\bin","..\src","setup.py","motus_v3.0.00.py","configs.py",
                                      'computer.py','gameboard.py','gui_tools.py','handledico.py','human.py']
                     }

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Projet MOTUS",
    version = "3.0",
    description = "Un dérivé du jeu télévisé de France Télévision 'MOTUS'",
    options = {"build_exe": build_exe_options},
    executables = [Executable(  script = "motus_v3.0.00.py",
                                icon = "../images/motus.ico",
                                copyright="(c) AMOUROUX Bernard 06/2025",
                                target_name="motus_v3.exe",
                                base = base)]
      )
