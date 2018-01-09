# Our critic data to work with
critics={
'Mark': 
{'Forrest Gump': 7, 'The Matrix': 9, 'Saving Private Ryan': 9, 'Gladiator': 8, 'The Lion King': 6, 'Into The Wild': 9, 'Finding Nemo': 6, 'Sin City': 4, 'Jaws': 7, 'Groundhog Day': 7, 'Fight Club': 10, 'The Silence of the Lambs': 7, 'Leon': 7, 'Terminator 2': 8, 'Aliens': 9, 'Braveheart': 6, 'Full Metal Jacket': 6,  'The Big Lebowski': 3, 'Men in Black': 6}, 

'Tom': 
{'Forrest Gump': 7, 'The Matrix': 5, 'Saving Private Ryan': 8, 'Gladiator': 6, 'The Lion King': 7, 'Finding Nemo': 8, 'Sin City': 3, 'Jaws': 4, 'Groundhog Day': 6, 'Fight Club': 10, 'The Silence of the Lambs': 4, 'Leon': 4, 'Terminator 2': 2, 'Aliens': 5, 'Braveheart': 3, 'Full Metal Jacket': 8,  'The Big Lebowski': 5, 'Men in Black': 4}, 

'Katy': 
{'Gladiator': 6, 'The Lion King': 7, 'Into The Wild': 10, 'Finding Nemo': 7, 'Sin City': 3, 'Fight Club': 6, 'The Silence of the Lambs': 4, 'Terminator 2': 6, 'Aliens': 7, 'Guardians of the Galaxy': 6,}, 

'Seb': 
{'Forrest Gump': 7, 'The Matrix': 5, 'Saving Private Ryan': 9, 'The Lion King': 5, 'Fight Club': 8, 'Terminator 2': 9, 'Aliens': 8, 'The Big Lebowski': 8, 'Men in Black': 3}, 

'Richard': 
{'Forrest Gump': 8, 'The Matrix': 9, 'Saving Private Ryan': 6, 'The Lion King': 6, 'Finding Nemo': 5, 'Sin City': 5, 'Jaws': 6, 'Fight Club': 7, 'The Silence of the Lambs': 7, 'Terminator 2': 9, 'Aliens': 8, 'Full Metal Jacket': 9, 'Men in Black': 6}, 

'Sally': 
{'Forrest Gump': 7, 'The Matrix': 9, 'Saving Private Ryan': 10, 'Gladiator': 9, 'Jaws': 5, 'Groundhog Day': 6, 'Fight Club': 7, 'The Silence of the Lambs': 9, 'Terminator 2': 7, 'Aliens': 8, 'Braveheart': 9, 'Full Metal Jacket': 8, 'The Big Lebowski': 7, 'Men in Black': 4}, 

'Victoria': 
{'Forrest Gump': 9, 'The Lion King': 7, 'Jaws': 5, 'Fight Club': 7}, 

'Emily': 
{'Forrest Gump': 9, 'The Matrix': 7, 'Finding Nemo': 7, 'Jaws': 7, 'Groundhog Day': 5, 'Fight Club': 9, 'The Silence of the Lambs': 7, 'Leon': 6, 'Aliens': 6, 'Men in Black': 7}, 

'Jamie': 
{'Forrest Gump': 7, 'The Matrix': 6, 'The Lion King': 5, 'Finding Nemo': 8, 'Jaws': 7, 'Fight Club': 9, 'Terminator 2': 7, 'Men in Black': 8}, 

'Ollie': 
{'Forrest Gump': 7, 'The Matrix': 7, 'Saving Private Ryan': 8, 'Gladiator': 7, 'Into The Wild': 6, 'Finding Nemo': 7, 'Sin City': 7, 'Jaws': 8, 'Groundhog Day': 7, 'Fight Club': 8, 'The Silence of the Lambs': 7, 'Leon': 7, 'Terminator 2': 5, 'Aliens': 8, 'Braveheart': 6, 'Full Metal Jacket': 8, 'Men in Black': 6}, 

'Matt': 
{'The Matrix': 7, 'Finding Nemo': 9, 'Groundhog Day': 6, 'Terminator 2': 9, 'Guardians of the Galaxy': 9, 'Men in Black': 6}, 

'Shaun': 
{'Forrest Gump': 6, 'The Matrix': 8, 'Saving Private Ryan': 9, 'The Lion King': 7, 'Finding Nemo': 7, 'Jaws': 5, 'Groundhog Day': 7, 'Fight Club': 9, 'The Silence of the Lambs': 6, 'Terminator 2': 5, 'Braveheart': 7,  'The Big Lebowski': 3, 'Guardians of the Galaxy': 6, 'Men in Black': 5}, 

'Owen': 
{'Forrest Gump': 4, 'The Matrix': 4, 'Saving Private Ryan': 5, 'The Lion King': 5, 'Into The Wild': 6, 'Finding Nemo': 5, 'Sin City': 7,  'Groundhog Day': 5, 'Fight Club': 7, 'The Silence of the Lambs': 5, 'Full Metal Jacket': 7,  'Guardians of the Galaxy': 7, 'Men in Black': 5}, 

}

from math import sqrt

# Returns a distance-based similarity score for person1 and person2
# Euclidean distance score
# Not being used but is shown for comparison
def sim_distance(prefs,person1,person2):
	# Get the list of shared_items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	# if they have no rating in common, return 0
	if len(si)==0: return 0

	# Add up the squares of all the differences
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

	return 1/(1+sqrt(sum_of_squares))

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	# Find the number of elements
	n= float(len(si))

	# If they have no ratings in common, return 0
	if n==0: return 0

	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])

	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den
	return r

# Returns the best matches for person from the prefs dictionary
# Number of results and similarity function are optional params
def topMatches(prefs,person,n=10,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other)
		for other in prefs if other!=person]

	# Sort the list so highest scores appear at the top
	scores.sort()
	scores.reverse()
	return scores[0:n]

# Gets recommendations for a person by using a weighted average of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare to self
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0:continue
		for item in prefs[other]:

			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item]==0:
				# Similarity * score
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				#Sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+=sim

		# Create the normalised list
		rankings=[(total/simSums[item],item) for item,total in totals.items()]

		# Return the sorted list
		rankings.sort()
		rankings.reverse()
		return rankings
