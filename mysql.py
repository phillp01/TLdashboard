import MySQLdb as _mysql
import json


class MySQLDatabase(object):
    """Define driver class"""
    def __init__(self, database_name, username, password, host='localhost'):
        """Connecting to the Database"""
        try:
            self.db = _mysql.connect(db=database_name, host=host, user=username, passwd=password)
            self.database_name = database_name
            print "connected to MySQL!"
        except _mysql.Error, e:
            print e

    def __del__(self):
        """Testing to make sure the connection is made"""
        if hasattr(self, 'db'):
            self.db.close()
            print "MySQL Connection Closed"

    def get_available_tables(self):
        """Show available tables"""
        cursor = self.db.cursor()
        cursor.execute("Show Tables;")

        self.tables = cursor.fetchall()

        cursor.close()

        return self.tables

    def get_columns_for_table(self, table_name):
        """
        This method will enable to interact
        with our database to find what columns
        are currently in a specific table
        """
        cursor = self.db.cursor()
        cursor.execute("SHOW COLUMNS FROM `%s`" % table_name)
        self.columns = cursor.fetchall()

        cursor.close()

        return self.columns

#Connection details for `my_db` database
db = _mysql.connect(
    db='trading-live',
    host='localhost',
    user='root',
    passwd='',
    charset='utf8',
    use_unicode=False
)

encoding = "utf-8"

def searchDB():
    cursor=db.cursor()
    cursor.execute("SELECT mm_user_data.first_name, mm_user_data.last_name, mm_user_data.membership_level_id, mm_membership_levels.name FROM mm_user_data JOIN mm_membership_levels ON mm_user_data.membership_level_id = mm_membership_levels.id WHERE mm_user_data.status = 1 AND (mm_membership_levels.id = 2 OR mm_membership_levels.id = 17 OR mm_membership_levels.id = 18 OR mm_membership_levels.id = 24)")

    results = cursor.fetchall()
    return results
    #results = cursor.fetchone()
    #return json.dumps(cursor.rowcount)
    cursor.close()

#searchDB()

