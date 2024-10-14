import models
import mysql.connector


class UsersMysqlRepository:
    def __int__(self, con):
        self.con = con

    def get_all(self):
        with self.con.cursor(dictionary=True) as cur:
            cur.execute('SELECT * FROM users')
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models.User(user['id'], user['username'], user['firstname'], user['lastname']))
            return users
