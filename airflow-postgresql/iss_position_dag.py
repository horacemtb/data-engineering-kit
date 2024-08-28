"""
DAG to fetch and store the International Space Station (ISS) position data.

This DAG performs:
1. Fetches the ISS position from the Open Notify API.
2. Stores the timestamp, latitude, and longitude in a PostgreSQL database.

- Schedule: Every 5 minutes
- PostgreSQL Connection ID: postgres_analytics
- API Endpoint: http://api.open-notify.org/iss-now.json

Author: [@dmitry_volobuev]
Date: August 28, 2024
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook

import requests
from datetime import datetime
import logging

API_URL = 'http://api.open-notify.org/iss-now.json'
DB_CONN_ID = 'postgres_analytics'
TABLE = 'iss_position'
REQUEST_TIMEOUT = 30

log = logging.getLogger(__name__)


def _fetch_iss_position():
    """
    Fetches the current position of the ISS from the public API.

    Returns:
        tuple: A tuple containing timestamp, latitude, and longitude of ISS.
    """
    try:
        response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        log.info(data)
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        return timestamp, latitude, longitude
    except requests.RequestException as e:
        log.error(f"Error fetching ISS position: {e}")
        raise


def _store_iss_position():
    """
    Fetches ISS position data and stores it in a PostgreSQL database.
    """
    try:
        timestamp, latitude, longitude = _fetch_iss_position()
        pg_hook = PostgresHook(postgres_conn_id=DB_CONN_ID)
        insert_sql = """
        INSERT INTO {} (timestamp, latitude, longitude)
        VALUES (%s, %s, %s)
        """.format(TABLE)
        pg_hook.run(insert_sql, parameters=(timestamp, latitude, longitude))
    except Exception as e:
        log.error(f"Error storing ISS position: {e}")
        raise


args = {'owner': 'airflow'}

with DAG(dag_id='iss_position_dag',
         default_args=args,
         description='Fetch ISS position and store in PostgreSQL',
         start_date=datetime(2024, 8, 28),
         tags=['@dmitry_volobuev'],
         schedule_interval='*/5 * * * *',
         catchup=False,
         max_active_runs=1,
         max_active_tasks=1) as dag:

    fetch_iss_position = PythonOperator(
        task_id='fetch_iss_position',
        python_callable=_fetch_iss_position,
    )

    store_iss_position = PythonOperator(
        task_id='store_iss_position',
        python_callable=_store_iss_position,
    )

    fetch_iss_position >> store_iss_position
