# Data Modeling Hands On

This hands-on repository has a very simple set up. The assumption is that CSV files in `./data`, come from a transactional
system that records the attendance of consultants and external guests to inspiring Knowledge Sharing sessions.
The coupling with the transactional system is quite loose, the files are exported regularly from their DB and dropped in
the folder, no new development is allowed on that side, so the data schemas are stable.

The KS sessions are registered in `Session.csv` for the whole year already (assume we are in January 2025). The hands-on
part of the sessions is recorded in `HandsOn.csv` and referenced in the session record via `HandsOnID`. Guest and consultant
participation is registered respectively in `Externals.csv`, and `Attendance.csv` and referenced via `SessionID`.
A snapshot of the current consultants is in `Consultants.csv`.

Consultants, alas, come and go, and as you might have guessed, during the hand-on you will create additional snapshots 
(using the `change_consultants.py` script) to simulate changes coming from the transactional system. 

The scope of this hands-on is to leverage dimensional modeling to answer some [business questions](#business-questions)
by creating some (DBT) models, namely few dimensions and a fact tables, able to deal with changes in the underlying data.


## Business Questions

The champions of the KS sessions are interested in knowing whether there's a correlation between the experience of the
consultants and the topic presented, so they want a dashboard that would show the average `YearsOfExperience` per each session
together with the `Subject` and `Topic` of that session. Also, if the number of participants (both externals and internals)
increases, could that be an indication of an interesting topic?

Would exposing a single fact table be enough to answer these questions?


## Running the pipeline

For the sake of simplicity, and before creating additional models, you can run the pipeline for ingesting the data in the
`raw` and `staging` layers simply by `./run.sh`. This will create the virtual environment, install the dependencies, and
run all the pipeline steps (check the `run.py` file). Alternatively you can use `make install` for just the virtual environment
creation and dependency installation. After that run `set -a && source env.local` and then `source $PATH_TO_VIRTUAL_ENV/bin/activate`
to `python ./run.py`.

The ingestion step will only create or replace tables in the `raw` schema of the DB (we are using DuckDB as a local 
analytical storage system). You can run this as many times as you want. The `staging` layer will populate the `_stg`
schema executing the models in `./models/staging`. To explore the created tables run `duckdb $DB_NAME`. Here you can use
standard SQL commands to check the data.

## Create Marts (dimensions + facts)

This is the actual exercise! On top of the staging layer, use the dimensional modeling technique to create a star schema
model!

### Changing the data
With your virtual environment activated, run `python change_consultants.py` to replace the `Consultants.csv` and
`Attendance.csv`, re-run the pipeline...

* Do you see the changes being reflected in your facts?
* What happens if you query again?

