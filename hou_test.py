import hou
import os
import sys

default_path = hou.pwd().part("file").evalAsString()
print(default_path)
