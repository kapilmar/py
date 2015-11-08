#   A .Import necessary libraries
#import zipfile
import os
import csv

#   B. method to unzip files with a from to path


# def unzip(from_path, to_path):

    # zip_ref = zipfile.ZipFile(from_path, 'r')
    # zip_ref.extractall(to_path)
    # zip_ref.close()

#   Make this folder - Input folder zip - Format - yyyymmdd(EOD).zip
input_ieod_path = "D:/Project Add on folder/i-darts/IEOD/"
input_ieod_list = os.listdir(input_ieod_path)

def nxt(accessCode, stock):
	
	with open((final_ieod_path + '/' + stock), 'rb') as day:
		allRowsList = csv.reader(day)# delimiter = ',')
		finalFile = 'D:/Project Add on folder/i-darts/Output/' + stock
		with open(finalFile, accessCode) as out:
			finale = csv.writer(out)#, delimiter =',')
			for row in allRowsList:
				finale.writerow(row)
ieod_list = []

for folder in input_ieod_list:
	print folder
	final_ieod_path = input_ieod_path + folder + '/1/Equity'
	ieod_path_list = os.listdir(final_ieod_path)
	#ieod_list.append(ieod_path_list)
	for stock in ieod_path_list:
		if os.path.isfile(final_ieod_path + '/' + stock) :
			nxt('ab', stock)
		else:		
			nxt('wb', stock)


				

