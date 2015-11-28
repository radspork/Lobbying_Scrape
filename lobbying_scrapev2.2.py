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
		self.ryan = ""
	def input(self):
		#Ask for overall path and year
		year = input('Enter the year to be parsed: ')
		print "year: %s" %(year)
		self.ryan = raw_input("Ryan? (y/n) ")
		if str(self.ryan) == "y":
			path = "/Users/Ryan/Documents/Research/Raw senate data/"
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
		print "Number of files:", len(self.filelist)
		self.scrape(year)
	def scrape(self, year):
		#Start Time Stamp
		start = datetime.datetime.now()
		#Set writing path
		if str(self.ryan) == "y":
			DumpDir = "/Users/Ryan/Documents/Research/DO_IT_ALL2/"
		else:
			DumpDir = str(raw_input("Output directory:"))
		CompleteName = str(str(DumpDir) + str(year) + ".csv")
		#Open writer
		with open(CompleteName, 'a') as f:
			#Header
			f.write("FILING_ID" + "," + "YEAR" + "," + "TYPE" + "," + "AMOUNT" + "," + "REG_NAME" + "," + "REG_ID"+ "," + "CONTACT_NAME" + "," + "CLIENT_ID" + "," + "CLIENT_NAME" + "," + "SELF_FILER" + "," + "LOBBYIST_NAME_1" + "," + "LOBBYIST_NAME_2" + "," + "LOBBYIST_NAME_3" + "," + "LOBBYIST_NAME_4" + "," + "LOBBYIST_NAME_5" + "," + "LOBBYIST_NAME_6" + "," + "LOBBYIST_NAME_7" + "," + "LOBBYIST_NAME_8" + "," + "LOBBYIST_NAME_9" + "," + "LOBBYIST_NAME_10" + "," + "CODE_1" + "," + "CODE_2" + "," + "CODE_3" + "," + "CODE_4" + "," + "CODE_5" + "," + "CODE_6" + "," + "CODE_7" + "," + "CODE_8" + "," + "CODE_9" + "," + "CODE_10" + "," + "GOV_ENTITY_NAME_1" + "," + "GOV_ENTITY_NAME_2" + "," + "GOV_ENTITY_NAME_3" + "," + "GOV_ENTITY_NAME_4" + "," + "GOV_ENTITY_NAME_5" + "," + "GOV_ENTITY_NAME_6" + "," + "GOV_ENTITY_NAME_7" + "," + "GOV_ENTITY_NAME_8" + "," + "GOV_ENTITY_NAME_9" + "," + "GOV_ENTITY_NAME_10" + '\n')
			writer = csv.writer(f)
			#loop for each file
			number = 0 
			for targetFile in self.filelist:
				tree = ET.parse(targetFile)
				root = tree.getroot()
				for element in root:
					all_tags = element.findall('.//')
					##Record the multiples to lists for writing
					#Lobbyist names
					LOBBYIST_ls = []
					for tags in all_tags:
						if str(tags.tag) == 'Lobbyist':
							LOBBYIST_ls.append(tags.attrib['LobbyistName'].encode('utf-8').strip())
					#Issue Codes
					CODE_ls = []
					for tags in all_tags:
						if str(tags.tag) == 'Issue':
							CODE_ls.append(tags.attrib['Code'].encode('utf-8').strip())
					#Specific Issues
					SPECIFIC_ls = []
					for tags in all_tags:
						if str(tags.tag) == 'Issue':
							SPECIFIC_ls.append(tags.attrib['SpecificIssue'].encode('utf-8').strip())
					#Gov entity names
					GOV_ENTITY_ls = []
					for tags in all_tags:
						if str(tags.tag) == 'GovernmentEntity':
							GOV_ENTITY_ls.append(tags.attrib['GovEntityName'].encode('utf-8').strip())

					#Lets keep count shall we
					number += 1

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
					LOBBYIST={}
					for x in range(0,10):
						LOBBYIST["_NAME_{0}".format(x)] = 0
					for x in range(len(LOBBYIST_ls)):
						LOBBYIST["_NAME_{0}".format(x)] = LOBBYIST_ls[x]
					
					#Issue Codes
					CODE={}
					for x in range(0,10):
						CODE["_{0}".format(x)] = 0
					for x in range(len(CODE_ls)):
						CODE["_{0}".format(x)] = CODE_ls[x]
					
					#Specific Issues
					SPECIFIC={}
					for x in range(0,10):
						SPECIFIC["_ISSUE_{0}".format(x)] = 0
					for x in range(len(SPECIFIC_ls)):
						SPECIFIC["_ISSUE_{0}".format(x)] = SPECIFIC_ls[x]
					
					#Gov entity names
					GOV_ENTITY={}
					for x in range(0,10):
						GOV_ENTITY["_NAME_{0}".format(x)] = 0
					for x in range(len(GOV_ENTITY_ls)):
						GOV_ENTITY["_NAME_{0}".format(x)] = GOV_ENTITY_ls[x]

					##Writer
					#Write each entry to CSV
					row_write = [FILING_ID, YEAR, TYPE, AMOUNT, REG_NAME, REG_ID, CONTACT_NAME, CLIENT_ID, CLIENT_NAME, SELF_FILER, LOBBYIST['_NAME_0'], LOBBYIST['_NAME_1'], LOBBYIST['_NAME_2'], LOBBYIST['_NAME_3'], LOBBYIST['_NAME_4'], LOBBYIST['_NAME_5'], LOBBYIST['_NAME_6'], LOBBYIST['_NAME_7'], LOBBYIST['_NAME_8'], LOBBYIST['_NAME_9'], CODE['_0'], CODE['_1'], CODE['_2'], CODE['_3'], CODE['_4'], CODE['_5'], CODE['_6'], CODE['_7'], CODE['_8'], CODE['_9'], GOV_ENTITY['_NAME_0'], GOV_ENTITY['_NAME_1'], GOV_ENTITY['_NAME_2'], GOV_ENTITY['_NAME_3'], GOV_ENTITY['_NAME_4'], GOV_ENTITY['_NAME_5'], GOV_ENTITY['_NAME_6'], GOV_ENTITY['_NAME_7'], GOV_ENTITY['_NAME_8'], GOV_ENTITY['_NAME_9']]
					writer.writerow(row_write)
		end = datetime.datetime.now()
		print "Entries Processed:", number
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