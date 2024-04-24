import csv
from datetime import datetime, timedelta
from pathlib import Path
from random import randint, random, choice

DATA_PATH = Path('__file__').parent / 'data'
FILENAME = DATA_PATH / 'Consultants.csv'
DATE_FMT = '%Y-%m-%d'
FIRST_NAMES = [
    'Tim', 'Peter', 'Lysbeth', 'Anne', 'Ada', 'Hannah', 'Jelle', 'Anthony', 'Sara'
]
LAST_NAMES = [
    'Smits', 'Johannson', 'Fenstra', 'Erikson', 'Van Gaal', 'Davis', 'Playmouth', 'Taylor'
]
PROJECTS = [
    'Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa'
]
CLIENTS = [
    'Ikea', 'Ayvens', 'Skoon', 'KLM', 'Politie', 'Liander', 'Eneco', 'Managed Grid', 'Internal'
]
TITLES = [
    'Senior Data Engineer', 'Lead Data Engineer', 'Project Manager', 'Data Analyst', 'Software Developer',
    'Research Assistant', 'Senior ML Engineer', 'Senior Data Scientist'
]
HEADER = [
    'SnapshotDate', 'ConsultantID', 'Name', 'MiddleName', 'Surname',
    'ClientName', 'ProjectName', 'Title', 'YearsOfExperience'
]
SNAPSHOT_DATE = (datetime.now() + timedelta(days=84)).strftime(DATE_FMT)


with open(FILENAME) as file:
    lines = [_l.strip() for _l in file.readlines()]

header = lines.pop(0)

assert header.split(',') == HEADER

LATEST_CONSULTANT = {k: v for k, v in zip(header.split(','), lines[-1].split(','))}

# Remove some records
for _ in range(randint(5, 20)):
    _pop_idx = randint(0, len(lines) - 1)
    lines.pop(_pop_idx)

# Scrumble some records
data = []
for line in lines:
    record = {k: v for k, v in zip(header.split(','), line.split(','))}
    record['SnapshotDate'] = SNAPSHOT_DATE
    record['YearsOfExperience'] = int(record['YearsOfExperience']) + randint(0, 1)
    if random() > 0.7:
        record['ClientName'] = choice(CLIENTS)
        record['ProjectName'] = choice(PROJECTS)
        record['Title'] = choice(TITLES)
    data.append(list(record.values()))

# Add some records
latest_consultant_id = int(LATEST_CONSULTANT['ConsultantID'])
for consultant_id in range(latest_consultant_id + 1, latest_consultant_id + randint(5, 20)):
    data.append(
        [
            SNAPSHOT_DATE, str(consultant_id), choice(FIRST_NAMES), '', choice(LAST_NAMES), choice(CLIENTS),
            choice(PROJECTS), choice(TITLES), randint(5, 10)
         ]
    )

with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(HEADER)
    writer.writerows(data)
