from application.db_connection import db

def get(url):
    cursor = db.cursor()
    query = "select malware_info from dev.url_table where url = %s"
    cursor.execute(query, (url,))
    result = cursor.fetchone()
    if not result: return None
    cursor.close()
    return result[0]

def update(url, malware_info):
    cursor = db.cursor()
    query = "update dev.url_table set malware_info=%s where url = %s ;"
    result = cursor.execute(query, (malware_info, url, ) )
    db.commit()
    cursor.close()
    return result

def insert(url, malware_info):
    if malware_info not in {"malware", "not malware"}: return "Invalid malware values!"
    cursor = db.cursor()
    query = "insert into dev.url_table (url, malware_info) values (%s, %s)"
    cursor.execute(query, (url, malware_info,))
    update(url, malware_info)
    db.commit()
    cursor.close()
    return "Inserted successfully!"