import xml.etree.ElementTree as ET
import os
import csv
import os.path
import datetime

##                                                                                   ##
#      Program to scrape lobbying data from downloaded senate lobbying database       #
#                                  By: Ryan Duecker                                   #
#                                                                                     #
#      http://www.senate.gov/legislative/Public_Disclosure/database_download.htm      #
##                                                                                   ##

class scrapper(object):
	def __init__(self):
		self.filelist = []
	def input(self):
		#Ask for overall path and year
		year = input('Enter the year to be parsed: ')
		print year
		#Directory where downloaded senate data is stored <-------------------------- alter if needed
		Ryan = raw_input("Ryan? (y/n) ")
		if str(Ryan) == "y":
			path = "/Users/Ryan/Desktop/Research/Raw senate data/"
		else:
			path = raw_input('Path of Downloaded Senate Data: ')
			str(path)
		print "Path: %s" %(path)
		#Start time stamp
		start = datetime.datetime.now()
		#Finding all called files in directory
		for root, dirs, files in os.walk(path):
			for file in files:
				if file.endswith(".xml"):
					if str(year) in file:
						self.filelist.append(os.path.join(root, file))
		print len(self.filelist)
		self.scrape(year)
	def scrape(self, year):
		#Start Time Stamp
		start = datetime.datetime.now()
		#Set writing path
		#Directory where the the csv's are to be saved <-------------------------- alter if needed
		DumpDir = "/Users/Ryan/Desktop/Research/DO_IT_ALL/"
		CompleteName = str(str(DumpDir) + str(year) + ".csv")
		#Open writer
		with open(CompleteName, 'a') as f:
			#Header
			f.write("FILING_ID" + "," + "YEAR" + "," + "TYPE" + "," + "AMOUNT" + "," + "REG_NAME" + "," + "REG_ID"+ "," + "CONTACT_NAME" + "," + "CLIENT_ID" + "," + "CLIENT_NAME" + "," + "SELF_FILER" + "," + "LOBBYIST_NAME_1" + "," + "LOBBYIST_NAME_2" + "," + "LOBBYIST_NAME_3" + "," + "LOBBYIST_NAME_4" + "," + "LOBBYIST_NAME_5" + "," + "LOBBYIST_NAME_6" + "," + "LOBBYIST_NAME_7" + "," + "LOBBYIST_NAME_8" + "," + "LOBBYIST_NAME_9" + "," + "LOBBYIST_NAME_10" + "," + "CODE_1" + "," + "CODE_2" + "," + "CODE_3" + "," + "CODE_4" + "," + "CODE_5" + "," + "CODE_6" + "," + "CODE_7" + "," + "CODE_8" + "," + "CODE_9" + "," + "CODE_10" + "," + "GOV_ENTITY_NAME_1" + "," + "GOV_ENTITY_NAME_2" + "," + "GOV_ENTITY_NAME_3" + "," + "GOV_ENTITY_NAME_4" + "," + "GOV_ENTITY_NAME_5" + "," + "GOV_ENTITY_NAME_6" + "," + "GOV_ENTITY_NAME_7" + "," + "GOV_ENTITY_NAME_8" + "," + "GOV_ENTITY_NAME_9" + "," + "GOV_ENTITY_NAME_10" + '\n')
			writer = csv.writer(f)
			#loop for each file
			for targetFile in self.filelist:
				tree = ET.parse(targetFile)
				print targetFile
				print tree
				root = tree.getroot()
				for element in root:
					all_tags = element.findall('.//')
					##Record the multiples to lists for writing
					#Lobbyist names
					LOBBYIST_NAME = []
					for tags in all_tags:
						if str(tags.tag) == 'Lobbyist':
							LOBBYIST_NAME.append(tags.attrib['LobbyistName'].encode('utf-8').strip())
					#Issue Codes
					CODE = []
					for tags in all_tags:
						if str(tags.tag) == 'Issue':
							CODE.append(tags.attrib['Code'].encode('utf-8').strip())
					#Specific Issues
					SPECIFIC_ISSUE = []
					for tags in all_tags:
						if str(tags.tag) == 'Issue':
							SPECIFIC_ISSUE.append(tags.attrib['SpecificIssue'].encode('utf-8').strip())
					#Gov entity names
					GOV_ENTITY_NAME = []
					for tags in all_tags:
						if str(tags.tag) == 'GovernmentEntity':
							GOV_ENTITY_NAME.append(tags.attrib['GovEntityName'].encode('utf-8').strip())

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
					for x in range(len(LOBBYIST_NAME)):
						LOBBYIST_NAME_[x] = LOBBYIST_NAME[[x]]
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
					for x in range(len(CODE)):
						CODE_[x] = CODE[x]
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
					for x in range(len(SPECIFIC_ISSUE)):
						SPECIFIC_ISSUE_[x] = SPECIFIC_ISSUE[[x]]
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
					for x in range(len(SPECIFIC_ISSUE)):
						GOV_ENTITY_NAME_[x] = GOV_ENTITY_NAME[[x]]
					##Writer
					#Write each entry to CSV
					row_write = [FILING_ID, YEAR, TYPE, AMOUNT, REG_NAME, REG_ID, CONTACT_NAME, CLIENT_ID, CLIENT_NAME, SELF_FILER, LOBBYIST_NAME_1, LOBBYIST_NAME_2, LOBBYIST_NAME_3, LOBBYIST_NAME_4, LOBBYIST_NAME_5, LOBBYIST_NAME_6, LOBBYIST_NAME_7, LOBBYIST_NAME_8, LOBBYIST_NAME_9, LOBBYIST_NAME_10, CODE_1, CODE_2, CODE_3, CODE_4, CODE_5, CODE_6, CODE_7, CODE_8, CODE_9, CODE_10, GOV_ENTITY_NAME_1, GOV_ENTITY_NAME_2, GOV_ENTITY_NAME_3, GOV_ENTITY_NAME_4, GOV_ENTITY_NAME_5, GOV_ENTITY_NAME_6, GOV_ENTITY_NAME_7, GOV_ENTITY_NAME_8, GOV_ENTITY_NAME_9, GOV_ENTITY_NAME_10]
					writer.writerow(row_write)
		end = datetime.datetime.now()
		print end-start
		multiple = raw_input('Another year?(y/n): ')
		if str(multiple) == "y":
			self.input()
		else:
			merge = raw_input('Merge CSVs?(y/n): ')
			if str(merge) == "y":
				self.merger(DumpDir)
			else:
				pass
	def merger(self, DumpDir):
		os.system(str("cat " + str(DumpDir) + "*.csv >merged.csv"))

CurrentScrape = scrapper()
CurrentScrape.input()
