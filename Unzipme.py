#Recursively find specific files in
#directory tree and unzip them

import os, zipfile

for root, dirs, files in os.walk(".", topdown=True):

    for name in files:

        if '.zip' in name:

            a=os.path.join(root,name)

            z=zipfile.ZipFile(a)

            for name in z.namelist():

                z.extract(name, root)

            z.close()

            os.remove(a)    
