# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 22:11:43 2026

@author: Raj Mohammad
"""


# Task 1
import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Raj Mohammad/OneDrive/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT * FROM interns WHERE track = 'Data Science' AND stipend > 5000",conn)

df = pd.read_sql_query("SELECT track, AVG(stipend) AS average_stipend FROM interns GROUP BY track",conn)

df = pd.read_sql_query("SELECT track, COUNT(*) AS total_interns FROM interns GROUP BY track",conn)
print(df)

# Task 2

import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Raj Mohammad/OneDrive/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT interns.name, mentors.mentor_name FROM interns INNER JOIN mentors ON interns.track = mentors.track",conn)
print(df)
