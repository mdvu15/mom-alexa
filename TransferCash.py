from blockcypher import create_wallet_from_address
from blockcypher import generate_new_address
from blockcypher import get_address_details
from blockcypher import simple_spend
from blockcypher import get_total_balance
from blockcypher import create_unsigned_tx
from blockcypher import send_faucet_coins

try:
	print(get_total_balance('C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2'))
	simple_spend(from_privkey='356ce8496d761f51aa5939da9f7bbfb94886234f1f8eb5507bea9f3676e6c8e8', to_address='C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', to_satoshis=500, coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
	print("I transferred money to your account. Your balance is now", get_total_balance('C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2'), "satoshis.")
except:
	print("I have nothing left to give.")