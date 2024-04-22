import logging
from pathlib import Path
from subprocess import run

import duckdb

from env import DB_NAME, RAW_SCHEMA

DATA_PATH = Path('__file__').parent / 'data'
ATTENDANCE = 'Attendance'
CONSULTANTS = 'Consultants'
EXTERNALS = 'Externals'
HANDSON = 'HandsOn'
SESSION = 'Session'

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(levelname)s - <%(filename)s> - %(funcName)s - %(message)s'
)
logger = logging.getLogger(__name__)


def ingest_data(_conn) -> None:
    _conn.execute(f'CREATE SCHEMA IF NOT EXISTS {RAW_SCHEMA}')
    logger.info(f'Created {RAW_SCHEMA} schema')
    for table in (ATTENDANCE, CONSULTANTS, EXTERNALS, HANDSON, SESSION):
        _conn.sql(
            f'CREATE OR REPLACE TABLE {RAW_SCHEMA}.{table} AS '
            f'SELECT * FROM read_csv(\'{str(DATA_PATH / table)}.csv\')'
        )
        logger.info(f'Ingested {table} data')


if __name__ == '__main__':
    conn = duckdb.connect(DB_NAME)
    ingest_data(conn)
    conn.close()

#    logger.info('Ingestion complete. Running `dbt run` to create dimension tables')
#    dimensions = run(
#        ['dbt', 'run', '--select', 'staging'],
#        check=False, capture_output=True
#    )
#    logger.info(f"\n{dimensions.stdout.decode('utf-8')}")
#
#    logger.info('Running `dbt test` to validate dimension tables')
#    test_staging = run(
#        ['dbt', 'test', '--select', 'staging', '--indirect-selection=cautious'],
#        check=False, capture_output=True
#    )
#    logger.info(f"\n{test_staging.stdout.decode('utf-8')}")
#
#    logger.info('Running `dbt run` to create data mart')
#    marts = run(
#        ['dbt', 'run', '--select', 'marts'],
#        check=False, capture_output=True
#    )
#    logger.info(f"\n{marts.stdout.decode('utf-8')}")
#    logger.info('Running `dbt test` to validate data mart')
#    test_marts = run(
#        ['dbt', 'test', '--select', 'marts',],
#        check=False, capture_output=True
#    )
#    logger.info(f"\n{test_marts.stdout.decode('utf-8')}")
