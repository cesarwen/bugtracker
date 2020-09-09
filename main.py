import sys
import os

base = os.path.abspath(os.getcwd())
sys.path.append('{}/controller'.format(base))
sys.path.append('{}/view'.format(base))
sys.path.append('{}/model'.format(base))

import db_handler

if __name__ == '__main__':
    db = db_handler.db_handler()
    #db.insert_ticket(name = "crambors")
    #db.insert_project(name = "Portifolio site", description = "making a portifolio website to make self propaganda")
    query = """ UPDATE projects
                SET name = 'latex cv', description = 'Well done, quick and simple CV'
                WHERE id = 3"""
    db.update(query)

    query = "SELECT * FROM projects"
    projects = db.select(query)
    for project in projects:
        print(project)