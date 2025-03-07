import argparse
parser = argparse.ArgumentParser(
    description="This program allows the user to generate a word cloud from the Python documentation.")
parser.add_argument("-f", "--sqlite-db", required=True,
                    help="path to a SQLite database file")
args = parser.parse_args()
if args.sqlite_db:
    print(f"{args.sqlite_db}")
