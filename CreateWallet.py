from blockcypher import create_wallet_from_address
from blockcypher import generate_new_address
from blockcypher import get_address_details
from blockcypher import simple_spend
from blockcypher import get_total_balance
from blockcypher import create_unsigned_tx
from blockcypher import send_faucet_coins

flan_address = generate_new_address(coin_symbol='bcy', api_key='feaf33689a3a4a1e82eb4457bf2e2009')
flan_wallet = create_wallet_from_address(wallet_name='flannery', address = flan_address['address'], api_key='feaf33689a3a4a1e82eb4457bf2e2009', coin_symbol = 'bcy')

alexa_address = generate_new_address(coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
alexa_wallet = create_wallet_from_address(wallet_name='alexa', address = alexa_address['address'], api_key='4bcc9dcc6bc449fc85cd525802b30fa2', coin_symbol = 'bcy')

print(get_total_balance(alexa_address['address'], coin_symbol='bcy'))
send_faucet_coins(address_to_fund=alexa_address['address'], satoshis=100000000, api_key='4bcc9dcc6bc449fc85cd525802b30fa2', coin_symbol='bcy')
print(get_total_balance(alexa_address['address'], coin_symbol='bcy'))

print(flan_address['address'])
print(alexa_address['private'])