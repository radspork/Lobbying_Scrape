import xml.etree.ElementTree as ET
import os
import csv
import os.path
import datetime

##                                                                                    ##
#  Program to scrape a year of lobbying data from downloaded senate lobbying database  #
#                                  By: Ryan Duecker                                    #
#                                                                                      #
#      http://www.senate.gov/legislative/Public_Disclosure/database_download.htm       #
##                                                                                    ##

#Ask for overall path and year
year = input('Enter the year to be parsed: ')
print year
path = "/Users/Ryan/Desktop/Research/Raw senate data/"
#Start time stamp
start = datetime.datetime.now()

#Finding all called files in directory
filelist = []
for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(".xml"):
			if str(year) in file:
				filelist.append(os.path.join(root, file))
print len(filelist)
number = 0
#Set writing path path
CompleteName = "/Users/Ryan/Desktop/Research/DO_IT_ALL/" + str(year) + ".csv"
CompleteName = str(CompleteName)
#Open writer
with open(CompleteName, 'a') as f:
	#Header
	f.write("FILING_ID" + "," + "YEAR" + "," + "TYPE" + "," + "AMOUNT" + "," + "REG_NAME" + "," + "REG_ID"+ "," + "CONTACT_NAME" + "," + "CLIENT_ID" + "," + "CLIENT_NAME" + "," + "SELF_FILER" + "," + "LOBBYIST_NAME_1" + "," + "LOBBYIST_NAME_2" + "," + "LOBBYIST_NAME_3" + "," + "LOBBYIST_NAME_4" + "," + "LOBBYIST_NAME_5" + "," + "LOBBYIST_NAME_6" + "," + "LOBBYIST_NAME_7" + "," + "LOBBYIST_NAME_8" + "," + "LOBBYIST_NAME_9" + "," + "LOBBYIST_NAME_10" + "," + "CODE_1" + "," + "CODE_2" + "," + "CODE_3" + "," + "CODE_4" + "," + "CODE_5" + "," + "CODE_6" + "," + "CODE_7" + "," + "CODE_8" + "," + "CODE_9" + "," + "CODE_10" + "," + "GOV_ENTITY_NAME_1" + "," + "GOV_ENTITY_NAME_2" + "," + "GOV_ENTITY_NAME_3" + "," + "GOV_ENTITY_NAME_4" + "," + "GOV_ENTITY_NAME_5" + "," + "GOV_ENTITY_NAME_6" + "," + "GOV_ENTITY_NAME_7" + "," + "GOV_ENTITY_NAME_8" + "," + "GOV_ENTITY_NAME_9" + "," + "GOV_ENTITY_NAME_10" + '\n')
	writer = csv.writer(f)
	#loop for each player
	for targetFile in filelist:
		tree = ET.parse(targetFile)
		print targetFile
		print tree
		root = tree.getroot()
		for element in root:
#			print element.tag, '|', element.attrib
	#		for all_tags in element.findall('.//'):
	#			print all_tags.tag, '|', all_tags.attrib
			all_tags = element.findall('.//')
			##Record the multiples to lists for writing
			#Lobbyist names
			LOBBYIST_NAME = []
			for tags in all_tags:
				if str(tags.tag) == 'Lobbyist':
					LOBBYIST_NAME.append(tags.attrib['LobbyistName'].encode('utf-8').strip())
#			print LOBBYIST_NAME
			#Issue Codes
			CODE = []
			for tags in all_tags:
				if str(tags.tag) == 'Issue':
					CODE.append(tags.attrib['Code'].encode('utf-8').strip())
#			print CODE
			#Specific Issues
			SPECIFIC_ISSUE = []
			for tags in all_tags:
				if str(tags.tag) == 'Issue':
					SPECIFIC_ISSUE.append(tags.attrib['SpecificIssue'].encode('utf-8').strip())
#			print SPECIFIC_ISSUE
			#Gov entity names
			GOV_ENTITY_NAME = []
			for tags in all_tags:
				if str(tags.tag) == 'GovernmentEntity':
					GOV_ENTITY_NAME.append(tags.attrib['GovEntityName'].encode('utf-8').strip())
#			print GOV_ENTITY_NAME

			#Lets keep count shall we
			number = number + 1
			print number


			#Set variables = to their attributes
			
			FILING_ID = element.attrib['ID'].encode('utf-8').strip()
			YEAR = element.attrib['Year'].encode('utf-8').strip()
			TYPE = element.attrib['Type'].encode('utf-8').strip()
			AMOUNT = element.attrib['Amount'].encode('utf-8').strip()
			for tags in all_tags:
				if str(tags.tag) == 'Registrant':
					REG_NAME = tags.attrib['RegistrantName'].encode('utf-8').strip()
					REG_ID = tags.attrib['RegistrantID'].encode('utf-8').strip()
			for tags in all_tags:
				if str(tags.tag) == 'Client':
					CONTACT_NAME = tags.attrib['ContactFullname'].encode('utf-8').strip()
					CLIENT_ID = tags.attrib['ClientID'].encode('utf-8').strip()
					CLIENT_NAME = tags.attrib['ClientName'].encode('utf-8').strip()
					SELF_FILER = tags.attrib['SelfFiler'].encode('utf-8').strip()
			#Lobbyist names
			LOBBYIST_NAME_1 = 0
			LOBBYIST_NAME_2 = 0
			LOBBYIST_NAME_3 = 0
			LOBBYIST_NAME_4 = 0
			LOBBYIST_NAME_5 = 0
			LOBBYIST_NAME_6 = 0
			LOBBYIST_NAME_7 = 0
			LOBBYIST_NAME_8 = 0
			LOBBYIST_NAME_9 = 0
			LOBBYIST_NAME_10 = 0
			for names in LOBBYIST_NAME:
				#print len(LOBBYIST_NAME)
				if len(LOBBYIST_NAME) == 0:
					LOBBYIST_NAME_1 = 0
				elif len(LOBBYIST_NAME) == 1:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
				elif len(LOBBYIST_NAME) == 2:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
				elif len(LOBBYIST_NAME) == 3:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
				elif len(LOBBYIST_NAME) == 4:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
				elif len(LOBBYIST_NAME) == 5:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
				elif len(LOBBYIST_NAME) == 6:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
					LOBBYIST_NAME_6 = LOBBYIST_NAME[5]
				elif len(LOBBYIST_NAME) == 7:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
					LOBBYIST_NAME_6 = LOBBYIST_NAME[5]
					LOBBYIST_NAME_7 = LOBBYIST_NAME[6]
				elif len(LOBBYIST_NAME) == 8:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
					LOBBYIST_NAME_6 = LOBBYIST_NAME[5]
					LOBBYIST_NAME_7 = LOBBYIST_NAME[6]
					LOBBYIST_NAME_8 = LOBBYIST_NAME[7]
				elif len(LOBBYIST_NAME) == 9:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
					LOBBYIST_NAME_6 = LOBBYIST_NAME[5]
					LOBBYIST_NAME_7 = LOBBYIST_NAME[6]
					LOBBYIST_NAME_8 = LOBBYIST_NAME[7]
					LOBBYIST_NAME_9 = LOBBYIST_NAME[8]
				else:
					LOBBYIST_NAME_1 = LOBBYIST_NAME[0]
					LOBBYIST_NAME_2 = LOBBYIST_NAME[1]
					LOBBYIST_NAME_3 = LOBBYIST_NAME[2]
					LOBBYIST_NAME_4 = LOBBYIST_NAME[3]
					LOBBYIST_NAME_5 = LOBBYIST_NAME[4]
					LOBBYIST_NAME_6 = LOBBYIST_NAME[5]
					LOBBYIST_NAME_7 = LOBBYIST_NAME[6]
					LOBBYIST_NAME_8 = LOBBYIST_NAME[7]
					LOBBYIST_NAME_9 = LOBBYIST_NAME[8]
					LOBBYIST_NAME_10 = LOBBYIST_NAME[9]
			#Issue Codes
			CODE_1 = 0
			CODE_2 = 0
			CODE_3 = 0
			CODE_4 = 0
			CODE_5 = 0
			CODE_6 = 0
			CODE_7 = 0
			CODE_8 = 0
			CODE_9 = 0
			CODE_10 = 0
			for codes in CODE:
				#print len(CODE)
				if len(CODE) == 0:
					CODE_1 = 0
				elif len(CODE) == 1:
					CODE_1 = CODE[0]
				elif len(CODE) == 2:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
				elif len(CODE) == 3:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
				elif len(CODE) == 4:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
				elif len(CODE) == 5:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
				elif len(CODE) == 6:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
					CODE_6 = CODE[5]
				elif len(CODE) == 7:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
					CODE_6 = CODE[5]
					CODE_7 = CODE[6]
				elif len(CODE) == 8:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
					CODE_6 = CODE[5]
					CODE_7 = CODE[6]
					CODE_8 = CODE[7]
				elif len(CODE) == 9:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
					CODE_6 = CODE[5]
					CODE_7 = CODE[6]
					CODE_8 = CODE[7]
					CODE_9 = CODE[8]
				else:
					CODE_1 = CODE[0]
					CODE_2 = CODE[1]
					CODE_3 = CODE[2]
					CODE_4 = CODE[3]
					CODE_5 = CODE[4]
					CODE_6 = CODE[5]
					CODE_7 = CODE[6]
					CODE_8 = CODE[7]
					CODE_9 = CODE[8]
					CODE_10 = CODE[9]
			#Specific Issues
			SPECIFIC_ISSUE_1 = 0
			SPECIFIC_ISSUE_2 = 0
			SPECIFIC_ISSUE_3 = 0
			SPECIFIC_ISSUE_4 = 0
			SPECIFIC_ISSUE_5 = 0
			SPECIFIC_ISSUE_6 = 0
			SPECIFIC_ISSUE_7 = 0
			SPECIFIC_ISSUE_8 = 0
			SPECIFIC_ISSUE_9 = 0
			SPECIFIC_ISSUE_10 = 0
			for specific_issues in SPECIFIC_ISSUE:
				#print len(SPECIFIC_ISSUE)
				if len(SPECIFIC_ISSUE) == 0:
					SPECIFIC_ISSUE_1 = 0
				elif len(SPECIFIC_ISSUE) == 1:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
				elif len(SPECIFIC_ISSUE) == 2:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
				elif len(SPECIFIC_ISSUE) == 3:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
				elif len(SPECIFIC_ISSUE) == 4:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
				elif len(SPECIFIC_ISSUE) == 5:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
				elif len(SPECIFIC_ISSUE) == 6:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
					SPECIFIC_ISSUE_6 = SPECIFIC_ISSUE[5]
				elif len(SPECIFIC_ISSUE) == 7:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
					SPECIFIC_ISSUE_6 = SPECIFIC_ISSUE[5]
					SPECIFIC_ISSUE_7 = SPECIFIC_ISSUE[6]
				elif len(SPECIFIC_ISSUE) == 8:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
					SPECIFIC_ISSUE_6 = SPECIFIC_ISSUE[5]
					SPECIFIC_ISSUE_7 = SPECIFIC_ISSUE[6]
					SPECIFIC_ISSUE_8 = SPECIFIC_ISSUE[7]
				elif len(SPECIFIC_ISSUE) == 9:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
					SPECIFIC_ISSUE_6 = SPECIFIC_ISSUE[5]
					SPECIFIC_ISSUE_7 = SPECIFIC_ISSUE[6]
					SPECIFIC_ISSUE_8 = SPECIFIC_ISSUE[7]
					SPECIFIC_ISSUE_9 = SPECIFIC_ISSUE[8]
				else:
					SPECIFIC_ISSUE_1 = SPECIFIC_ISSUE[0]
					SPECIFIC_ISSUE_2 = SPECIFIC_ISSUE[1]
					SPECIFIC_ISSUE_3 = SPECIFIC_ISSUE[2]
					SPECIFIC_ISSUE_4 = SPECIFIC_ISSUE[3]
					SPECIFIC_ISSUE_5 = SPECIFIC_ISSUE[4]
					SPECIFIC_ISSUE_6 = SPECIFIC_ISSUE[5]
					SPECIFIC_ISSUE_7 = SPECIFIC_ISSUE[6]
					SPECIFIC_ISSUE_8 = SPECIFIC_ISSUE[7]
					SPECIFIC_ISSUE_9 = SPECIFIC_ISSUE[8]
					SPECIFIC_ISSUE_10 = SPECIFIC_ISSUE[9]
			#Gov entity names
			GOV_ENTITY_NAME_1 = 0
			GOV_ENTITY_NAME_2 = 0
			GOV_ENTITY_NAME_3 = 0
			GOV_ENTITY_NAME_4 = 0
			GOV_ENTITY_NAME_5 = 0
			GOV_ENTITY_NAME_6 = 0
			GOV_ENTITY_NAME_7 = 0
			GOV_ENTITY_NAME_8 = 0
			GOV_ENTITY_NAME_9 = 0
			GOV_ENTITY_NAME_10 = 0
			for entitynames in GOV_ENTITY_NAME:
				#print len(GOV_ENTITY_NAME)
				if len(GOV_ENTITY_NAME) == 0:
					GOV_ENTITY_NAME_1 = 0
				elif len(GOV_ENTITY_NAME) == 1:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
				elif len(GOV_ENTITY_NAME) == 2:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
				elif len(GOV_ENTITY_NAME) == 3:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
				elif len(GOV_ENTITY_NAME) == 4:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
				elif len(GOV_ENTITY_NAME) == 5:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
				elif len(GOV_ENTITY_NAME) == 6:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
					GOV_ENTITY_NAME_6 = GOV_ENTITY_NAME[5]
				elif len(GOV_ENTITY_NAME) == 7:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
					GOV_ENTITY_NAME_6 = GOV_ENTITY_NAME[5]
					GOV_ENTITY_NAME_7 = GOV_ENTITY_NAME[6]
				elif len(GOV_ENTITY_NAME) == 8:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
					GOV_ENTITY_NAME_6 = GOV_ENTITY_NAME[5]
					GOV_ENTITY_NAME_7 = GOV_ENTITY_NAME[6]
					GOV_ENTITY_NAME_8 = GOV_ENTITY_NAME[7]
				elif len(GOV_ENTITY_NAME) == 9:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
					GOV_ENTITY_NAME_6 = GOV_ENTITY_NAME[5]
					GOV_ENTITY_NAME_7 = GOV_ENTITY_NAME[6]
					GOV_ENTITY_NAME_8 = GOV_ENTITY_NAME[7]
					GOV_ENTITY_NAME_9 = GOV_ENTITY_NAME[8]
				else:
					GOV_ENTITY_NAME_1 = GOV_ENTITY_NAME[0]
					GOV_ENTITY_NAME_2 = GOV_ENTITY_NAME[1]
					GOV_ENTITY_NAME_3 = GOV_ENTITY_NAME[2]
					GOV_ENTITY_NAME_4 = GOV_ENTITY_NAME[3]
					GOV_ENTITY_NAME_5 = GOV_ENTITY_NAME[4]
					GOV_ENTITY_NAME_6 = GOV_ENTITY_NAME[5]
					GOV_ENTITY_NAME_7 = GOV_ENTITY_NAME[6]
					GOV_ENTITY_NAME_8 = GOV_ENTITY_NAME[7]
					GOV_ENTITY_NAME_9 = GOV_ENTITY_NAME[8]
					GOV_ENTITY_NAME_10 = GOV_ENTITY_NAME[9]
			##Writer
			#Write each entry to CSV
			row_write = [FILING_ID, YEAR, TYPE, AMOUNT, REG_NAME, REG_ID, CONTACT_NAME, CLIENT_ID, CLIENT_NAME, SELF_FILER, LOBBYIST_NAME_1, LOBBYIST_NAME_2, LOBBYIST_NAME_3, LOBBYIST_NAME_4, LOBBYIST_NAME_5, LOBBYIST_NAME_6, LOBBYIST_NAME_7, LOBBYIST_NAME_8, LOBBYIST_NAME_9, LOBBYIST_NAME_10, CODE_1, CODE_2, CODE_3, CODE_4, CODE_5, CODE_6, CODE_7, CODE_8, CODE_9, CODE_10, GOV_ENTITY_NAME_1, GOV_ENTITY_NAME_2, GOV_ENTITY_NAME_3, GOV_ENTITY_NAME_4, GOV_ENTITY_NAME_5, GOV_ENTITY_NAME_6, GOV_ENTITY_NAME_7, GOV_ENTITY_NAME_8, GOV_ENTITY_NAME_9, GOV_ENTITY_NAME_10]
			writer.writerow(row_write)
end = datetime.datetime.now()
print end-start
