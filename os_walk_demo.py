import os
from builtins import print

for root, dirs, files in os.walk(os.curdir):
    print("{0} has {1} files".format(os.path.abspath(root), len(files)))
    if ".idea" in dirs:
        dirs.remove(".idea")
    if ".git" in dirs:
        dirs.remove(".git")

