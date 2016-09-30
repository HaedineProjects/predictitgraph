import json
from state_abbrevs import STATES

f = open('current_probabilities.json')
states = json.load(f)
print states

print 'state,value'
for state in sorted(states):
	d = states[state]['Democratic']
	# r = state['Republican']
	print STATES[state] + ',' + unicode(1.0 - d)
	
	