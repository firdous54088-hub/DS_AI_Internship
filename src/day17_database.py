# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 19:43:36 2026

@author: Raj Mohammad
"""

# Task 1

import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Raj Mohammad/OneDrive/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT * FROM interns",conn)
df = pd.read_sql_query("SELECT name, track FROM interns",conn)

print(df)
