import csv
from datetime import datetime, timedelta
from pathlib import Path
from random import randint, random, choice

DATA_PATH = Path('__file__').parent / 'data'
CONSULTANT_FILENAME = DATA_PATH / 'Consultants.csv'
ATTENDANCE_FILENAME = DATA_PATH / 'Attendance.csv'
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
SNAPSHOT_DATE = (datetime.now() + timedelta(days=56)).strftime(DATE_FMT)
CONSULTANTS_HEADER = ['SnapshotDate', 'ConsultantID', 'Name', 'MiddleName', 'Surname', 'ClientName', 'ProjectName', 'Title', 'YearsOfExperience']
ATTENDANCE_HEADER = ['Date', 'SessionID', 'ConsultantID', 'Attendance']

with open(CONSULTANT_FILENAME) as file:
    consultants = [_l.strip() for _l in file.readlines()]

consultants_header = consultants.pop(0)
assert consultants_header.split(',') == CONSULTANTS_HEADER

LATEST_CONSULTANT = {k: v for k, v in zip(consultants_header.split(','), consultants[-1].split(','))}


with open(ATTENDANCE_FILENAME) as file:
    attendance = [_l.strip() for _l in file.readlines()]

attendance_header = attendance.pop(0)
assert attendance_header.split(',') == ATTENDANCE_HEADER

# Remove some records
removed_consultant_ids = []
for _ in range(randint(5, 20)):
    _pop_idx = randint(0, len(consultants) - 1)
    _consultant_id = consultants[_pop_idx].split(',')[1]
    removed_consultant_ids.append(_consultant_id)
    consultants.pop(_pop_idx)

attendance_data = []
sessions_date = {}
for line in attendance:
    record = {k: v for k, v in zip(attendance_header.split(','), line.split(','))}
    sessions_date[record['SessionID']] = record['Date']
    if record['ConsultantID'] in removed_consultant_ids and record['Date'] >= SNAPSHOT_DATE:
        continue
    else:
        attendance_data.append(list(record.values()))

# Scrumble some records
consultant_data = []
for line in consultants:
    record = {k: v for k, v in zip(consultants_header.split(','), line.split(','))}
    record['SnapshotDate'] = SNAPSHOT_DATE
    record['YearsOfExperience'] = int(record['YearsOfExperience']) + randint(0, 1)
    if random() > 0.7:
        record['ClientName'] = choice(CLIENTS)
        record['ProjectName'] = choice(PROJECTS)
        record['Title'] = choice(TITLES)
    consultant_data.append(list(record.values()))

# Add some records
latest_consultant_id = int(LATEST_CONSULTANT['ConsultantID'])
for consultant_id in range(latest_consultant_id + 1, latest_consultant_id + randint(5, 20)):
    consultant_data.append(
        [
            SNAPSHOT_DATE, str(consultant_id), choice(FIRST_NAMES), '', choice(LAST_NAMES), choice(CLIENTS),
            choice(PROJECTS), choice(TITLES), randint(5, 10)
        ]
    )
    for session_id, session_date in sessions_date.items():
        if session_date >= SNAPSHOT_DATE:
            attendance_data.append([session_date, session_id, str(consultant_id), choice(['Yes', 'No'])])

with open(CONSULTANT_FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(CONSULTANTS_HEADER)
    writer.writerows(consultant_data)

with open(ATTENDANCE_FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(ATTENDANCE_HEADER)
    writer.writerows(attendance_data)
