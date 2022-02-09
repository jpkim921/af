import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from custom_operators.my_operators import MyFirstOperator

from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator


with DAG('my_test_dag', description='Another tutorial DAG',
        schedule_interval='0 12 * * *',
        start_date=datetime(2017, 3, 20), catchup=False
        ) as dag:

    dummy_task = DummyOperator(task_id='dummy_task', dag=dag)
    operator_task = MyFirstOperator(my_operator_param='This is a test.', task_id='my_first_operator_task', dag=dag)

dummy_task >> operator_task
