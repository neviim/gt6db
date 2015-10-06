#!/usr/bin env python3

import os
import csv

import json
import pymongo
from pymongo import MongoClient

# mongodb
def get_db():
    client = MongoClient('localhost:27017')
    db = client.gt6db
    return db

def add_dados(db, data):
    db.countries.insert(data)

def get_country(db):
    return db.countries.find_one()
# ---

def readMyFiles(filePath):
    # abre banco gt6db
    db = get_db()

    #get all files in the given folder
    fileListing = os.listdir(filePath)
    for myFile in fileListing:
        #create the file path
        myFilePath = os.path.join(filePath, myFile)

        #check to make sure its a file not a sub folder
        if (os.path.isfile(myFilePath) and myFilePath.endswith(".csv")):

            # gera arquivo csv
            # with open(myFilePath, 'r', encoding='utf-8') as csvfile:
            #     #sniff to find the format
            #     fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
            #     csvfile.seek(0)
            #     #create a CSV reader
            #     myReader = csv.reader(csvfile, dialect=fileDialect)
            #     #read each row
            #     for row in myReader:
            #         #do your processing here
            #         #print(row)
            #         pass
            
            dados = {}

            # gera arquivo json   
            with open(myFilePath, 'r', encoding='utf-8') as csvfile: 
                #sniff para encontrar o formato format 
                fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                #read the CSV file into a dictionary
                dictReader = csv.DictReader(csvfile, dialect=fileDialect)
                for row in dictReader:
                    #print(row)
                    db.base.insert(row)
    return
 
 
if __name__ == '__main__':
    currentPath = os.path.dirname(__file__)
    filePath = os.path.abspath(os.path.join(currentPath, os.pardir,os.pardir,'_github/gt6/csv'))

    readMyFiles(filePath)


