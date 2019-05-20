import os


html = os.subprocess("rst2html5 notes.rst")

with open(output, 'w+') as ofile:
    ofile.write(html)
