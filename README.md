# Movie-Recommender-Engine
A movie recommender that can be used by friends and family for a more custom personalized recommendation. In this challenge, we used collaborative filtering to solve.  
Remember: The more accurate the recommendation – the faster to watch the movie!

# How to Run
To get started with the movie recommender you must first download the source code. Afterwards, you should modify the critic’s ratings dataset according to your new critic’s ratings. 

# Now for the fun part!
To receives recommendations for a certain critic, enter in the python command line: getRecommendation(critics,’your critics name’)
Model 

There are many methods to find the similarity between two data points. A popular method is Euclidean distance. 

# Method 1: Euclidean distance
Euclidean distance is great but it isn’t always the most accurate. This is because a movie can be rated an 8 by one critic and 10 by another critic and they’re both considered great to both. When the value can be the different but represent the same thought – Pearson distance is great to use. 

# Method 2: Pearson distance
A more efficient method to find the similarities is Pearson distance. Pearson distance removes the problem of using Euclidean distance by changing the axes to critics instead of movies.

The equation used in the code can be seen below.

Where:

N = number of pairs of scores
 = sum of the products of paired scores
 = sum of x scores
 = sum of y scores
 = sum of squared x scores
 = sum of squared y scores

# Author
•	Blog by Mark Cook - Initial work – Mark Cook
