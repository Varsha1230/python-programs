import os

oldname = "filename.txt"
newname = "renamed_by_pyhton.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)
