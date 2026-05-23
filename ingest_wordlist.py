import sys
from pathlib import Path

import duckdb as ddb


def ingest_wordlist(wordlist_path: Path, db_path: Path, schema_path: Path):
    """
    Ingest a Wordlist file. File must be a single file with whitespace separating words.

    :param wordlist_path: Path to Wordlist file.
    :param db_path: Path to DuckDB Database file.
    :param schema_path: Path to SQL Schema file.
    :return:
    """
    word_list: list[str] = []

    with wordlist_path.open() as f:
        word_list = f.read().split()
    if not word_list:
        sys.stderr.write(b"Failed to load word list.")
        sys.exit(-1)

    char_tuples = [
        (word, *tuple(char for char in word))
        for word in word_list
    ]

    with ddb.connect(db_path) as conn, Path(schema_path).open() as schema_file:
        schema_script = schema_file.read()
        conn.execute(schema_script)
        conn.executemany("INSERT INTO MyWordleOlap.MyWordList VALUES (?, ?, ?, ?, ?, ?)", char_tuples)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        ingest_wordlist(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        wpath = Path(input("Path to Wordlist: "))
        dbp = Path(input("Path to Database: "))
        sp = Path(input("Path to Schema: "))

        ingest_wordlist(wpath, dbp, sp)
