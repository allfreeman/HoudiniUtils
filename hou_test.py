import hou
import os
import sys

default_path = hou.pwd().parm("file").evalAsString()
print(default_path)
