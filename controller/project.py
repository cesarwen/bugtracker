class project:
    def __init__(self):
        self.__insert__ = """INSERT INTO
        projects (name, description)
        VALUES ('{}', '{}');"""

    def new_project(self, name, description=None):
        return(self.__insert__.format(name, description))
