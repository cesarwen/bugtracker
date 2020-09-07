import sys
sys.path.append('../controller')
sys.path.append('../view')

import postgreSQL

if __name__ == '__main__':
    db= postgreSQL.database()
    cmd = "INSERT INTO PROJECTS (NAME) VALUES ('TEY')"
    #db.insert(cmd)

    cmd = "SELECT * FROM PROJECTS"

    print(cmd)

    rows = db.select(cmd)
    for row in rows:
        print(row)