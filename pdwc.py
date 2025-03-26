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
cursor.execute('SELECT * FROM Pages LIMIT 10')
w_not_required = ['also', 'added', 'about', 'arguments', 'been', 'bytes', 'called', 'changed', 'them', 'want', 'provides', 'window',
                  'changes', 'call', 'current', 'contributed', 'characters', 'document', 'does', 'example', 'each', 'written', 'provided',
                  'from', 'file', 'functions', 'first', 'following', 'files', 'given', 'have', 'information', 'instance', 'instead', 'into',
                  'line', 'like', 'methods', 'must', 'more', 'modules', 'message', 'name', 'note', 'next', 'names', 'objects', 'because',  'exceptions', 'just',
                  'only', 'other', 'previous', 'returns', 'returned', 'raised', 'release', 'should', 'same', 'some', 'being', 'were', 'whether', 'many',
                  'supports', 'such', 'specified', 'this', 'that', 'there', 'than', 'these', 'they', 'then', 'types', 'time', 'used', 'using',
                  'values', 'with', 'will', 'when', 'which', 'standard', 'updated', 'builtin', 'format', 'sequence', 'where', 'your', 'directory', 'defined',
                  'windows', 'available', 'attributes', 'after', 'always', 'before', 'base', 'both', 'between', 'classes', 'created', 'containing',
                  'calls', 'calling', 'contains', 'different', 'either', 'equivalent', 'form', 'found', 'link', 'most', 'errors',
                  'mode', 'make', 'need',  'optional', 'options', 'otherwise', 'passed', 'process', 'possible', 'strings', 'parameters', 'variables',
                  'suggesting', 'since', 'size', 'single', 'section', 'text', 'test', 'their', 'uses', 'useful', 'without', 'would']
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
        # print(words)
        for word in words:
            if word.startswith('http'):
                continue
            if not word.isalpha() or len(word) < 4:
                continue
            if word in w_not_required:
                continue
            table[word] = table.get(word, 0) + 1
# table_sor = dict(sorted(table.items(), key=lambda item: item[1], reverse=True))
table_sor = sorted(table, key=table.get, reverse=True)

# print(table_sor, '\n')

bigger = None
# lower = None
for k in table_sor[:100]:
    if bigger is None or bigger < table_sor[:100]:
        bigger = table_sor[:100]
    # if lower is None or lower > table_sor[:100]:
    #     lower = table_sor[:100]
print('Range of table:', bigger)
