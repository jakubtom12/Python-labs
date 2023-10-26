import os

root = 'c:/Users/kubat/.vscode/repo/Python-labs'

for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))