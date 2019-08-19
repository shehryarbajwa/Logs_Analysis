"""
Logs analysis Udacity Project Full Stack Nano-degree
"""

import pyscopg2


conn = sqlite3.connect("news")

cursor = conn.cursor()

cursor.execute("select * from authors limit 10")

results = cursor.fetchall()

print(results)

