# -*- coding: utf-8 -*-
__author__ = 'Саша'
import sqlite3

con = sqlite3.connect("test_base.db3")
cur = con.cursor()
sql = """\
CREATE TABLE user (
  id_user INTEGER PRIMARY KEY AUTOINCREMENT,
  email text,
  passw text
);

CREATE TABLE rubl (
  id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
  name_rubl TEXT
);

CREATE TABLE site (
  id_site INTEGER PRIMARY KEY AUTOINCREMENT,
  is_user INTEGER,
  id_rubl INTEGER,
  url TEXT,
  title TEXT,
  iq INTEGER
);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError, err:
    print u"Ошибка:", err
else:
    print u"Запрос успешно выполнен"
cur.close()
con.close()
raw_input()
