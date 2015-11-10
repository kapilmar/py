import zipfile
import os

def unzip(from_path, to_path):

    zip_ref = zipfile.ZipFile(from_path, 'r')
    zip_ref.extractall(to_path)
    zip_ref.close()
	
for zip_file in input_eod_list:

    zip_file = ("D:/Python - Stuff/IEOD Project/Input/EOD/%s" % zip_file)
    print zip_file

    unzip(zip_file, zip_output_eod_path)	
	
zin = zipfile.ZipFile ('archive.zip', 'r')
zout = zipfile.ZipFile ('archve_new.zip', 'w')
for item in zin.infolist():
    buffer = zin.read(item.filename)
    if (item.filename[-4:] != '.exe'):
        zout.writestr(item, buffer)
zout.close()
zin.close()	
