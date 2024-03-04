import hou
import os
import sys

load_path = hou.pwd().parm("Loaded_File").evalAsString()
print(load_path)
