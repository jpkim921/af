from airflow.hooks.base import BaseHook
from web3 import Web3

class Web3Hook(BaseHook):
    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def w3(self):
        return Web3(Web3.HTTPProvider(self.url))
    
    def checkBalance(self, address):
        w3 = self.w3()
        return w3.eth.get_balance(address)