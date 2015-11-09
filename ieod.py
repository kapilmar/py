#import zipfile
import os
import csv

#   B. method to unzip files with a from to path
# def unzip(from_path, to_path):

    # zip_ref = zipfile.ZipFile(from_path, 'r')
    # zip_ref.extractall(to_path)
    # zip_ref.close()

#   Make this folder - Input folder zip - Format - yyyymmdd(EOD).zip
#Home - Sony - Vaio - PC
#input_ieod_path = "D:/Project Add on folder/i-darts/IEOD/"
#Office - Main - HDD
input_ieod_path = "F:/1. with_date/"
input_ieod_list = os.listdir(input_ieod_path)

# Function to read from the single csvs and to write to one main 
def nxt(accessCode, stock): # passing access code to append 'ab' if file already present & write 'wb' if no such csv exists 
	
	# open source ieod file to read - making path and reading
	with open((final_ieod_path + '/' + stock), 'rb') as day:
		
		#read all rows of the file using csv.reader
		allRowsList = csv.reader(day)# delimiter = ',')
		
		#destination file - open and write / append using access code
		#finalFile = 'D:/Project Add on folder/i-darts/Output/' + stock
		finalFile = 'F:/Output/' + stock
		with open(finalFile, accessCode) as out:
			
			#Return a writer object responsible for converting the read data into delimited strings on the given file-like object.
			finale = csv.writer(out)#, delimiter =',')
			
			# write each row one by one
			for row in allRowsList:
				finale.writerow(row)

for folder in input_ieod_list:
	print folder
	#final_ieod_path = input_ieod_path + folder + '/1/Equity'
	final_ieod_path = input_ieod_path + folder + '/Equity/1'
	ieod_path_list = os.listdir(final_ieod_path)
	#ieod_list.append(ieod_path_list)
	for stock in ieod_path_list:
		if os.path.isfile(final_ieod_path + '/' + stock) :
			nxt('ab', stock)
		else:		
			nxt('wb', stock)


				
