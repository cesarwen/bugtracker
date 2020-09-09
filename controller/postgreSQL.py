#!/usr/bin/python
import sys
import psycopg2
from config_ini import config

class database:
    def __init__(self):
        # read connection parameters
        self.params = config()

    def __connect__(self):

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**self.params)

        return (conn)

    def __close__(self, conn):
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    def select_all(self, cmd):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            
            conn = self.__connect__()
            
            # create a cursor
            cur = conn.cursor()
            
        # execute a statement
            cur.execute(cmd)
        
        # gets all query responses
            rows = cur.fetchall()

        # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.__close__(conn)
            return(rows)

    def edit(self, cmd):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            
            conn = self.__connect__()
            
            # create a cursor
            cur = conn.cursor()
            
        # execute a statement
            cur.execute(cmd)

            # commit the changes to the database
            conn.commit()

        # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.__close__(conn)

