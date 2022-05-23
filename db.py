import sqlite3
conn = sqlite3.connect(r'D:\python_nas\project\_vlr_ui\game_db.db')
c = conn.cursor()
c.execute('''CREATE TABLE valorant_tgt (username TEXT, password TEXT, name TEXT,riot_id TEXT,rank TEXT,contact TEXT,valorant_tracker TEXT,title TEXT,PRIMARY KEY(username,riot_id))''')

c.execute('''CREATE TABLE dota_2_tgt (username TEXT, password TEXT, name TEXT,steam_link TEXT ,rank TEXT,contact TEXT,role TEXT,title TEXT,PRIMARY KEY(username,steam_link))''')

c.execute('''CREATE TABLE apex_legends_tgt (username TEXT , password TEXT, name TEXT,steam_link TEXT,rank TEXT,contact TEXT,title TEXT,PRIMARY KEY(username,steam_link))''')

c.execute('''CREATE TABLE IF NOT EXISTS report_dota_fix(steam_link TEXT,reason TEXT,reason_title TEXT,Image BLOB,PRIMARY KEY(steam_link))''')

conn.commit()
