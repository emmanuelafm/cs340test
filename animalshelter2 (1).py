#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:52:47 2023

@author: emmanuelafile_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, USER, PASS):
        # USER = 'aacuser'
        # PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30539
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection successful")
        
    def create(self,data):
        if data is not None:
            self.database.animals.insert_one(data)
            return data
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self,data):
        if data is not None:
            query = list(self.database.animals.find(data,{"_id":False}))
            return query
        else:
            raise Exception("No data found")
            return False
    
    def update(self,search,new_data):
        if search is not None:
            query = self.database.animals.update_many(search, {"$set":new_data})
        else:
            raise Exception("No data found")
            return False
        return query.raw_result
    
    def delete(self,delete):
        if delete is not None:
            query = self.database.animals.delete_many(delete)
        else:
            raise Exception("No data found")
            return False
        return query.raw_result