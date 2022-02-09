import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from custom_operators.wallet_operator import WalletOperator
# from custom_hooks.web3_hook import Web3Hook


from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator


with DAG('connect_web3', description='Test Web3 hookG',
        schedule_interval='0 12 * * *',
        start_date=datetime(2017, 3, 20), catchup=False
        ) as dag:

    dummy_task = DummyOperator(task_id='dummy_task')
    wallet_task = WalletOperator(task_id="wallet_task", name="wallet_name")


dummy_task >> wallet_task
