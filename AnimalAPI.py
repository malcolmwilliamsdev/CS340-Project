#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:42:29 2024

@author: malcolmwillia_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    # CRUD operations for animal collection in MongoDB
    
    def __init__(self, username, passwd):
        # connection vars
        # USER = 'aacuser'
        # PASS = 'mongopass123'
        USER = username
        PASS = passwd
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31144
        DB = 'aac'
        COL = 'animals'
        
        # init connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # insert a document
    def create(self, data: dict) -> bool:
        if data == None:
            raise Exception("Create failed. Data is empty.")
            
        result_id = self.collection.insert_one(data).inserted_id
        return False if result_id == None else True
        
    # search documents
    def read(self, data: dict) -> bool:
        if data == None:
            raise Exception("Read failed. Data is empty.")
        
        return list(self.collection.find(data))
    
    # update documents
    def update(self, filter:dict, data:dict) -> bool:
        if filter == None:
            return Exception("Update failed. Filter is empty.")
        
        if data == None:
            return Exception("Update failed. Data is empty.")
        
        update = {"$set": data}
        
        return self.collection.update_many(filter, update).modified_count
    
    # delete documents
    def delete(self, filter:dict) -> bool:
        if filter == None:
            return Exception("Delete failed. filter is empty.")
        
        return self.collection.delete_many(filter).deleted_count