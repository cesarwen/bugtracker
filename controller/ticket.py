from datetime import datetime

class ticket:
    def __init__(self):
        self.__insert__ = """INSERT INTO
        tickets (created, due, name, project, description, done, task_type)
        VALUES ('{}', '{}', '{}', {}, '{}', {}, {});"""

    def new_ticket(self, name, due=None, project = 1, description = None, task_type = 1):
        now=datetime.now()
        return(self.__insert__.format(now, due, name, project, description, 0, task_type))