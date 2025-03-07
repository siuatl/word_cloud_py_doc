import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--sqlite-db", help="a data base")
args = parser.parse_args()
if args.sqlite_db:
    print(f"{args.sqlite_db}")
