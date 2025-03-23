import sqlite3
from bs4 import BeautifulSoup
import argparse
import string
parser = argparse.ArgumentParser(
    description="This program allows the user to generate a word cloud from the Python documentation.")
parser.add_argument("-f", "--sqlite-db", required=True,
                    help="path to a SQLite database file")
args = parser.parse_args()
db_con = sqlite3.connect(args.sqlite_db)
cursor = db_con.cursor()
cursor.execute('SELECT * FROM Pages LIMIT 10 OFFSET 100')
table = dict()
for row in cursor:
    data = row[2]
    if data is None:
        continue
    soup = BeautifulSoup(data, 'html.parser')
    text = soup.find_all('p')
    for line in text:
        txt = line.get_text()
        tet = txt.strip()
        tex = txt.translate(txt.maketrans('', '', string.punctuation))
        text_s = tex.lower()
        if len(text_s) == 0:
            continue
        words = text_s.split()
        print(words)
        for word in words:
            if not word.isalpha() or len(word) < 2:
                continue
            table[word] = table.get(word, 0) + 1
print(table)
