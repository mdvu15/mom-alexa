from blockcypher import create_wallet_from_address
from blockcypher import generate_new_address
from blockcypher import get_address_details
from blockcypher import simple_spend
from blockcypher import get_total_balance
from blockcypher import create_unsigned_tx
from blockcypher import send_faucet_coins

print(get_total_balance('BxEAVmVhjPB5WyM5w1DR3zeHcwn9aMVJtm', coin_symbol='bcy'))
simple_spend(from_privkey='e6c3f444b3675a9e2a7b6af533fe0e8a13c6642427ec2e09c9ef148be9a60541', to_address='BxEAVmVhjPB5WyM5w1DR3zeHcwn9aMVJtm', to_satoshis=500, coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
print(get_total_balance('BxEAVmVhjPB5WyM5w1DR3zeHcwn9aMVJtm', coin_symbol='bcy'))