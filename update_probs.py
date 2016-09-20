import requests, time
from state_urls import state_urls

# # for state in state_urls:
# 	# print state
# 	# print state_urls[state]

# AL = state_urls['AL']
# r = requests.get(AL)
# # print r.encoding
# # print r.headers
# response_data = r.json()
# for k in response_data['Contracts']:
# 	print k

# print '\n\n\n\n\n\n\n'

# for k in response_data:
# 	print k
# 	print k, response_data[k]
	
state_prices = {}
for state in state_urls:
	state_prices[state] = {}
	r = requests.get(state_urls[state])
	response_data = r.json()
	
	contracts = response_data['Contracts']
	for c in contracts:
		state_prices[state][c['Name']] = c['LastTradePrice']
	time.sleep(1)


print state_prices
