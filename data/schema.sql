DROP SCHEMA IF EXISTS MyWordleOlap CASCADE;

CREATE SCHEMA MyWordleOlap;

CREATE TABLE IF NOT EXISTS MyWordleOlap.MyWordList (
    word VARCHAR(5),
    l0 CHAR,
    l1 CHAR,
    l2 CHAR,
    l3 CHAR,
    l4 CHAR,
);

CREATE VIEW MyWordleOlap.Words AS
    SELECT word FROM MyWordleOlap.MyWordList;
