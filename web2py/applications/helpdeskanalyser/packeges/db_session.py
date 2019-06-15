# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:37:32 2018

@author: Miromar J. Lima
"""

import psycopg2

class CreateSession:
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "jmenzen")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

'''
class CreateSession:     
    # Tests
    def __new__(self, url_db = 'postgresql://postgres:postgres@localhost/jmenzen'):        
    # Change ip to acesse server
         
        #database_platform://database_user:password@hostname_or_ip/database_name

        self.string_con = url_db
        
        # an Engine, which the Session will use for connection resources
        self.db_engine = create_engine(self.string_con, poolclass=NullPool)
    
        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.db_engine)   
        
        # create a Session
        self.sess = self.Session() 
        
        return self.sess       
'''