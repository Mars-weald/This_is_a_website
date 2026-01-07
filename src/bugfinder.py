from main import *
import sys

if len(sys.argv) >= 2:
    basepath = sys.argv[1]
else:
    basepath = "/"
print(basepath)