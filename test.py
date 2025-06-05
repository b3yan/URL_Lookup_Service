from app.db_actions import get, update, insert

def test_get():
    get_value = get("https://en.wikipedia.org/wiki/Main_Page")
    print(get_value) # test

def test_update():
    update(url = 'not_malware.com', malware_info = "not malware")

def test_insert():
    insert_value = insert("malware.com", "malware")
    print(insert_value)

def test_all():
    insert("malware.com", "malware")
    insert("not_malware.com", "not malware")
    
    value_1 = get("malware.com")
    value_2 = get("not_malware.com")
    
    assert value_1 == "malware"    
    assert value_2 == "not malware"