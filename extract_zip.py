# This program can be used to extract some specific folders / files 
# from inside a zip file (or a large number of zip files).
# The folder where the files need to be extracted would be created if it does not exist
# This is a branch off from the zip_compact_main.py method

# Import for zip & os functionality
import zipfile
import os

# Path where the zipped files are
zipped_folder_path = "C:/Users/Kapil/Desktop/Zippy/"

# pick up 1 zip file at a time form the folder to work with
for zfile in os.listdir(zipped_folder_path):
	
	# Initialiallize the input zipfile to read mode
	zip_in = zipfile.ZipFile (zipped_folder_path + zfile, 'r')
	    
	# Find the folder name as string - from the reverse -> -4 = '.zip' removed
	folder_name = (zipped_folder_path + zfile)[-12:-4]
	print folder_name
	
	#Initialize the output file to write mode - create if does not exist - Not reqd in this case
    #zout = 'C:/Users/Kapil/Desktop/Zippy/%s(1 min)' % folder_name
	
	# Make the directory - check if it exists before that
	directory = 'C:/Users/Kapil/Desktop/Test/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	# Work with all folders & files in the ziparchive 1 by 1
	for item in zip_in.infolist():
		
		# Read the zip file and put it in memory
        #buffer = zip_in.read(item.filename)
		
		# If the folder name is '1' - extract it with folder name. 
		# Donot extract other files / folders
		if (item.filename[0:2] == '1/'):
			zip_in.extract(item, directory + folder_name)
    		
	
# close the zip archives when done
    
zip_in.close()
	
