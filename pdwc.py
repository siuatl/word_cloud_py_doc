#! /usr/bin/env python3

import sqlite3
from bs4 import BeautifulSoup
import argparse
import string
import sys


def normalize_size(count, upper, lower):
    """ 
    Calculates the normalized size for the given word frequency.

    :param count (int): The word frequency.
    :param upper (int): The highest word frequency.
    :param lower (int): The lowest word frequency.

    :returns: The size between 20 and 100 inclusive, where the word frequency percentage is proportional to the size percentage.
    """

    # Range of sizes = [0, 80] + 20 = [20, 100]
    if count > upper or count < lower:
        raise Exception(f'count out of range (count={count} range=[{lower}, {upper}])')
    range_of_sizes = 80
    smallest_size = 20

    percent_freq = (count - lower) / float(upper - lower)
    normalized_size = (percent_freq * range_of_sizes) + smallest_size
    return normalized_size


def main():
    parser = argparse.ArgumentParser(
        description="This program allows the user to generate a word cloud from the Python documentation.")
    parser.add_argument("-f", "--sqlite-db", required=True,
                        help="path to a SQLite database file")
    args = parser.parse_args()
    db_con = sqlite3.connect(args.sqlite_db)
    cursor = db_con.cursor()
    cursor.execute('SELECT * FROM Pages')
    w_not_required = ['also', 'added', 'about', 'arguments', 'been', 'bytes', 'called', 'changed', 'them', 'want', 'provides', 'window', 'longer',
                      'changes', 'call', 'current', 'contributed', 'characters', 'document', 'does', 'example', 'each', 'written', 'provided', 'supported',
                      'from', 'file', 'functions', 'first', 'following', 'files', 'given', 'have', 'information', 'instance', 'instead', 'into', 'what',
                      'line', 'like', 'methods', 'must', 'more', 'modules', 'message', 'name', 'note', 'next', 'names', 'objects', 'because',  'exceptions', 'just',
                      'only', 'other', 'previous', 'returns', 'returned', 'raised', 'release', 'should', 'same', 'some', 'being', 'were', 'whether', 'many',
                      'supports', 'such', 'specified', 'this', 'that', 'there', 'than', 'these', 'they', 'then', 'types', 'time', 'used', 'using', 'corresponding',
                      'values', 'with', 'will', 'when', 'which', 'standard', 'updated', 'builtin', 'format', 'sequence', 'where', 'your', 'directory', 'defined',
                      'windows', 'available', 'attributes', 'after', 'always', 'before', 'base', 'both', 'between', 'classes', 'created', 'containing',
                      'calls', 'calling', 'contains', 'different', 'either', 'equivalent', 'form', 'found', 'link', 'most', 'errors', 'part',
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
            for word in words:
                if word.startswith('http'):
                    continue
                if not word.isalpha() or len(word) < 4:
                    continue
                if word in w_not_required:
                    continue
                table[word] = table.get(word, 0) + 1
    table_sorted = sorted(
        table.items(), key=lambda item: item[1], reverse=True)
    table_sorted = table_sorted[:100]

    upper = table_sorted[0][1]
    lower = table_sorted[-1][1]

    my_js = open('gword.js', 'w')
    my_js.write("gword = [")
    headd = True
    for i in table_sorted:
        if not headd:
            my_js.write(",\n")
        headd = False
        size_f = i[1]
        my_js.write("{text: '"+i[0]+"', size: " +
                    str(normalize_size(size_f, upper, lower))+"}")
    my_js.write("\n];\n")
    my_js.close()


if __name__ == '__main__':
    sys.exit(main())
