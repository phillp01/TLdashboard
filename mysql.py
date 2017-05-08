import MySQLdb as _mysql
import json

# Connection details for `my_db` database
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

searchDB()

