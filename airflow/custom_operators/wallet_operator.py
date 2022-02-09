import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from airflow.models import BaseOperator
from custom_hooks.web3_hook import Web3Hook

import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

log = logging.getLogger(__name__)

class WalletOperator(BaseOperator):

    # @apply_defaults
    def __init__(self, name:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def execute(self, context):
        hook = Web3Hook("http://127.0.0.1:8545")
        w3 = hook.w3()
        isConnected = w3.isConnected()
        balance = hook.checkBalance("0x3f99b97cd684B05932F2b079214d3b47BfA247b0")
        log.info(f"Are we connected to w3? -> {isConnected}")
        log.info(f"Balance of wallet: {balance}")
        return balance

# class MyFirstPlugin(AirflowPlugin):
#     name = "my_first_plugin"
#     operators = [MyFirstOperator]

