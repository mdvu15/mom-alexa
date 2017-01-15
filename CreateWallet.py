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

#print(alexa_address)
print(get_total_balance(alexa_address['address'], coin_symbol='bcy'))
#simple_spend(from_privkey=alexa_address['private'], to_address=alexa_address['address'], to_satoshis=1000000, coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
'''
inputs = [{'address': alexa_address['address']}, ]
outputs = [{'address': alexa_address['address'], 'value': 1000000}]
unsigned_tx = create_unsigned_tx(inputs=inputs, outputs=outputs, api_key='4bcc9dcc6bc449fc85cd525802b30fa2', coin_symbol='bcy')
print(unsigned_tx)
'''
send_faucet_coins(address_to_fund=alexa_address['address'], satoshis=100000000, api_key='4bcc9dcc6bc449fc85cd525802b30fa2', coin_symbol='bcy')
print(get_total_balance(alexa_address['address'], coin_symbol='bcy'))

print(get_total_balance(flan_address['address'], coin_symbol='bcy'))
simple_spend(from_privkey=alexa_address['private'], to_address=flan_address['address'], to_satoshis=500, coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
print(get_total_balance(flan_address['address'], coin_symbol='bcy'))