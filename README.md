# **URL Lookup Service**

## 1. DB Schema:
**MySQL server -> create table: url_table**
```
CREATE TABLE url_table(
    url VARCHAR(512) PRIMARY KEY, 
    malware_info VARCHAR(512) NOT NULL
);
```
P.S. We can also add additional fields like updated_time, updated_by, inserted_time, and inserted_by, ... to track the actions' date time and author.

## 2. Basic Requirements:
**Python 3.2.1 and pip**

## 3. Reproduce Steps:
1. Clone project- `git clone https://github.com/b3yan/URL_Lookup_Service`
2. Go to folder: `cd URL_Lookup_Service`
3. Install modules: `pip install -r install_modules.txt`
4. Change password in application/db_connection.py to your own password.
4. Run the application: `python run_application.py`

## 4. Thought Exercise:
Please refer to the Thought Exercise.pdf file. Thank you!
