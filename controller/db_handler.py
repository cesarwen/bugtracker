import postgreSQL
from ticket import ticket
from project import project

class db_handler:
    def __init__(self):
        self.__db__ = postgreSQL.database()
        self.project = project()
        self.ticket = ticket()

    def insert_ticket(self, name, due=None, project = None, description = None, task_type = None):
        query = self.ticket.new_ticket(name = "asd")
        self.__db__.edit(query)
    
    def insert_project(self, name, description=None):
        query = self.project.new_project(name, description)
        self.__db__.edit(query)
    
    def select(self, query):
        return(self.__db__.select_all(query))

    def update(self, query):
        return(self.__db__.edit(query))