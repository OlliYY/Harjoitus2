import mysql.connector

from repositories.users_mysql_repository import UsersMysqlRepository


def users_repository_factory():
    con = mysql.connector.connect(
        user='root',
        database='sovelluskehykset_bad1',
        password=''
    )
    return UsersMysqlRepository(con)