import csv
import sys


def stale(row):
    return int(row["age_minutes"]) > int(row["max_age_minutes"])


def stale_groups(rows):
    return [row["feature_group"] for row in rows if stale(row)]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for group in stale_groups(list(csv.DictReader(handle))):
            print(group)


if __name__ == "__main__":
    main(sys.argv[1])
