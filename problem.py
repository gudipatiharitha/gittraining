import random
outcomes = { "heads":0, 
		"tails":0,
		}
sides=outcomes.keys()
for i in range (1000):
	outcomes[random.choice(sides)] +=1
print 'heads: ',outcomes['heads']
print 'tails: ',outcomes['tails']

# for dice 
outcomes = { "1":0, 
		"2":0, "3":0,"4":0,"5":0,"6":0
		}
faces=outcomes.keys()
for i in range (1000):
	outcomes[random.choice(faces)] +=1
print '1: ',outcomes['1']
print '2: ',outcomes['2']
print '3: ',outcomes['3']
print '4: ',outcomes['4']
print '5: ',outcomes['5']
print '6: ',outcomes['6']
