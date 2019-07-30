"""
STRETCH : Chapter 8: How to Win Friends and Influence Users

Google's PageRank algorithm is what they use to show you the most relevant search results for your query. Through this and other factors, Google influences what you see on that first page every single time you search something (and how often are you going past the first page?)

PageRank Your Friends

PageRank is currently implemented using concepts from graph theory, assigning scores of "relevance" to links. We're going to model that by doing the same thing to our social networks (what, you've never ranked your friends before?). This is how social media influence is calculated! Let's find out which of our friends have the most influence in the network.

The algorithm for PageRank uses an iterative approach, where each iteration improves our approximation of the true PageRank value. For determining the importance of web pages, the rankings become stable after around 30-40 iterations. But for our much smaller graphs, the rankings will likely become stable after just a few iterations.

Each vertex is assigned an initial PageRank value of 1/n for n vertices. So if our social network has 10 users, each user is assigned 1/10.
For each iteration:
Assign each vertex a new PageRank value of 0.
For each vertex v, take v's previous PageRank value and divide it amongst v's outgoing links. So if v had a PageRank value of 1/10 and has links to a, b, and c, then a, b, and c will each receive 1/30 to their new PageRank values.
Here's a great video explanation if you'd like to learn more.

Note: For the below challenge, you'll be using a directed weighted graph.

Stretch Challenge: Write a method influencer(self) that uses the PageRank algorithm to rank you and your friends according to influence.

def influencer(self):
# Create a dictionary of vertex -> PageRank value and set initial values to 1/n
# For each iteration:
    # Create a new dictionary of vertex -> PageRank value, set all to 0
    # For each vertex v:
    	# Divide up v's previous PageRank value amongst v's neighbors.
	# For m neighbors, each neighbor receives value/m
    # Replace previous PageRanks with new PageRanks
# Sort all vertices according to their PageRank value, return sorted list
"""

# DID NOT COMPLETE THIS STRETCH CHALLENGE
