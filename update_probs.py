import requests, time
import datetime, json
from state_urls import state_urls
from electoral_votes import electoral_votes
from state_abbrevs import state_abbrevs

#################	
state_prices = {}
for state in state_urls:
	state_prices[state_abbrevs[state]] = {}
	r = requests.get(state_urls[state])
	response_data = r.json()
	
	contracts = response_data['Contracts']
	for c in contracts:
		state_prices[state_abbrevs[state]][c['Name']] = c['LastTradePrice']
	time.sleep(5)
	print state, state_prices[state_abbrevs[state]][c['Name']]

state_data = {}
for s in state_prices:
	state_data[s] = {}
	state_data[s]['republican'] = state_prices[s]['Republican']
	state_data[s]['democratic'] = state_prices[s]['Democratic']
	state_data[s]['electoralVotes'] = electoral_votes[s]
	state_data[s]['probability'] = 1.0 - state_prices[s]['Democratic']

now = datetime.datetime.now()
f = open('state_data' + now.strftime('%Y%m%d.%H:%M') + '.json', 'wb')
f.write(json.dumps(state_data))
f.close()

f = open('state_data_latest.json', 'wb')
f.write(json.dumps(state_data))
f.close()
