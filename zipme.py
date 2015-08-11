#Recursively find specific files in
#directory tree and zip them

import os, zipfile

for root, dirs, files in os.walk(".", topdown=True):

    for name in files:

        if '.txt' in name: #specify what file you want to get zipped

            a='zipp.zip'   #name the zip file

            a=os.path.join(root,a)

            z=zipfile.ZipFile(a,"w")

            for name in files:

                z.write(a,name)

            break

z.close()   
