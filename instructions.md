The Faker Network

Chapter 0: Set up

How many social network platforms are you currently on? Each of those is an example of graph theory being applied to solve the problem of finding connections – and recommending appropriate ones.

In this tutorial, you'll be given a graph built using Faker that will act as your social network. You'll be working with your nine closest (fake) friends to figure out interesting data about them, how to expand your network, and how to categorize them

Learning Outcomes

By the end of this tutorial, you will be able to...

Use a variety of neighbor lookup algorithms for a given graph
Traverse a graph through various search methods
Categorize your graph based on data or known attributes
Using Git/GitHub

Much like we've done in earlier tutorials, make sure you're committing your code as you complete milestones. At a minimum, you should make a commit whenever the tutorial prompts you.

Let's get your repo set up!

Go to the starter repo and clone the repo locally
Now we need to change the remote so that you can commit/push/pull the changes you make to your own repo. It is very important you do the below steps in order to get everything working properly.
Go to GitHub and create an empty, public repository called REPO-NAME, and now associate it as a remote for your cloned starter code, and then push to it.
Go to your repo on GitHub and make sure your previously empty repo is now full with starter code! Now when you add/commit/push, it'll be to your repo!
Chapter 1: Who do you know?

This tutorial will focus on properties of a social network. To begin with, we'll need to define a network as a set of people (vertices) and the people they know. If person A knows person B then there is an edge between them.

Draw a graph with you at the center connected by and edge to another 9 people you know. Do any of these 9 know each other? If so draw an edge between them. This will be your "Social Graph" to use as a sample in the rest of this tutorial.
Implement in code

The Graph Abstract Data Type (ADT) is defined as follows:

A class `Graph()`` creates a new, empty graph.
The methods addVertex(vert) and addEdge(fromVert, toVert) add a new vertex and directed edge respectively.
While addEdge(fromVert, toVert, weight) Adds a weighted, directed edge.
The methods getVertex(vertKey) finds the named vertKey and getVertices() returns the list of all vertices.
There are two common ways to implement the graph ADT in Python; the adjacency matrix and the adjacency list. There are trade-offs in each representation.

Challenge: Implement the graph ADT with an adjacency list in the file graph-adt-list.py.

Challenge: Implement the graph ADT with an adjacency matrix in the file graph-adt-matrix.py.

Challenge: Create a graph reader in the file graph-reader.py that reads in a graph from a text file and creates an instance of this class via the graph ADT. Assume the graph is represented in the text file by a list of vertices on line 1 followed by edges represented as ordered pairs, one per line.

Chapter 2: Won't you Be My Neighbor?

Have you ever had that moment where you find out a friend knows another one of your friends? Having one of those "worlds collide" moments can be exciting, scary, or a whole mixture of emotions. Instead of having that situation surprise us, what if we had a way to look know this information. in advanced?

Find Your Neighbors

Turns out we do! We can utilize a neighbor lookup for a given node in our graph to see what other nodes it is connected with. If you and a friend are connected, you two share a friendship. How do we know if two nodes are connected? They share an edge!

Challenge: Write a function that takes in a graph and a node as input, and outputs all nodes connected to the input node.

CODE GOES HERE

Make sure the input node is actually in the graph
Find all edges for the input node
See what nodes are connected to the input node via the edge
return the connected nodes
Down The Friend Chain We Go

Alright, no more surprise connections for us! But what if we want to go even further than one connection? Onward!

Chapter 3: Breadth of Fresh Neighbors

How does Facebook or LinkedIn know what friends to recommend to you? They look at who your friends are friends with, and who their friends are friends with, and so on

two friends

Source: Giphy

Friends of Friends

The function you just wrote is great for finding your immediate friends, but what if we want to see their friend's friends?

Think back to CS 1.3: what's an algorithm at your disposal we could use here?

Since we want to find all friends at a certain connection level away (friend's friend would be 2 connections from you), this sounds like a perfect application of Breadth First Search (BFS). Check out the Tree Traversals lesson from CS 1.3 if you want a refresher.

Challenge: Write a function that takes in a graph, a node, and n (an integer) as input, and outputs all nodes that are n connections away from the input node.

CODE GOES HERE

Make sure the input node is actually in the graph
Run BFS starting from the input node and going n levels deep
Return all nodes found at the nth level
A More Granular Approach

Great application of BFS! But as with anything related to BFS, specificity isn't a strong suite. Having all of your 3rd, 4th, 5th degree connections is daunting. What if we just want to see how two specific people are connected? We'll solve this in the next chapter!

Chapter 4: Friends Along the Way

There's this idea of six degrees of separation: take two people in the world, and they are at most six social connections away from each other. You may be more familiar with the Six Degrees of Kevin Bacon as an example of this.

kevin bacon

Source: MisterDressup

You may not know Kevin Bacon (or do you?), but we can still apply this to our graph of friends to find the connections that create a chain between two people. This is an application of path finding

Finding the Path

Think of a graph as a neighborhood, each house as a node, and immediate neighbors as nodes that share an edge. If you wanted to figure out how to get from one house to another, you'd walk to that house, passing other houses along the way. You'd be walking a path, walking from one node to another via edges!

Challenge: Write a function that takes in a graph and two nodes (A and B) as input, and outputs the list of nodes that must be traversed to get from A to B. The output list of nodes must be in order of nodes visited starting from A and ending at B.

Hint: BFS or it's familiar friend Depth First Search (DFS) could be useful here. Again if you need a refresher, here's that Tree Traversals lesson from CS 1.3

CODE GOES HERE

Make sure that both nodes A and B are actually in the graph
Run BFS or DFS starting from A
Figure out a way to keep track of each path you take
Once you find B, end the search.
Since you've been tracking the paths, find the path that goes from A to B
Return the path, in the order of nodes visited starting with A and ending with B
Optimizing our Path

This works, but what if there are multiple paths between two nodes? What if one of those paths is significantly longer than the other? Do you know Veronica from high school from your cousin Ricky, who went to college with Sarah, who dated Jane, who is friends with Billy, who was on the swim team with Veronica? Or do you know Veronica from your friend Tom who also is friends with Veronica? In the next chapter, we'll learn how to differentiate paths in order to optimize our route.

Chapter 5: Closest of Friends

If you were trying to show how two people are socially connected, you would want to do so in the least number of connections possible. Can you imagine if LinkedIn couldn't determine if someone was a 2nd or 20th degree connection?

Shortest Path

In order to solve this problem, we want to find the shortest path between two nodes in a graph.

Challenge 1: Write a function that takes in a graph and two nodes (A and B) as input, and outputs the list of nodes that make up the shortest path from A to B. The output list of nodes must be in order of nodes visited starting from A and ending at B.

CODE GOES HERE

Make sure that both nodes A and B are actually in the graph
Run BFS starting from A
Figure out a way to keep track of each path you take
Once you find B, end the search.
Since you've been tracking the paths, find the shortest path that goes from A to B
Return the shortest path, in the order of nodes visited starting with A and ending with B
This seems pretty similar to what we did in an earlier chapter, right? What if not all edges were of equal connection?

Dijkstra's Algorithm

For a given graph, it may take more work to traverse one edge over another. These are show through edge weights, or weighted edges. Up until now, all of our edges have had an implicit weight of one (1), so they were all equal. But in many cases, weights could be any value. Going back to our house example, some places are more challenging to walk through than others (hills, no sidewalk, a horde of gnomes blocking the path, etc.).

We can't use BFS or DFS anymore to find the shortest path since those two algorithms don't take weights into consideration. So what can we use instead?

Dijkstra's Algorithm is a shortest path algorithm that takes weighted edges into consideration! From the starting node, the algorithm visits neighbors one by one and assigns them a distance value based on the cumulative weights of the shortest path to get to that neighbor. Distances are updated if a shorter path can be found, and once we're at the target node, we'll know the shortest path to get to there. It's like running a more thoughtful BFS!

Note: For the below challenge, you'll be using the weighted graph from the starter code, which can be found here

Challenge 2: Write a function that takes in a weighted graph and two nodes (A and B) as input, and outputs the shortest path from A to B using Dijkstra's algorithm.

CODE GOES HERE

step by step walkthrough of implementing Dijkstra
The Long and Short of it is...

Now we can handle the shortest path for both unweighted and weighted graphs! Great work! It's great to find the shortest path, but sometimes we want to know more about a graph. There's a lot of properties around distance we can measure, and we'll dive into another one of them in the next chapter!

Chapter 6: Long-Distance Friendships

We know you're six degrees away from Kevin Bacon, but who are you the furthest away from? Not your pen pal in Bhutan (that would still be a neighbor!), but someone you don't know, and who you in fact know the least!

Graph Diameter

One concept around graph distance that helps us solve this problem is finding the diameter of a graph. The diameter of a graph is the calculated by finding the shortest path between every possible pair of nodes, and then selecting the longest of those paths.

Challenge: Write a function that takes in a weighted graph as input, and outputs the diameter of the graph

CODE GOES HERE

For every node, find the shortest path from it to every other node in the graph and track the paths and their length
From your list of path/length pairs, pick the one with the largest length and return the length.
Stretch Challenges: Find other properties of a graph! See if you can calculate the center or radius of a weighted graph. Keep these notes in mind:

A radius of a graph must also have a diameter.
Radius can be calculated by finding the minimum distance among all the maximum distances between a node to all other nodes
The center of a graph is the set of all nodes where the greatest distance to other nodes is the shortest.
Read up on eccentricity to help with this!
Becoming an Influencer

We've seen a lot of social network applications with our graph so far, but there are other real applications of graph theory throughout the industry! One of the biggest applications is in the tool you use every day...

Chapter 7: How to Win Friends and Influence Users

Google's PageRank algorithm is what they use to show you the most relevant search results for your query. Through this, Google influences what you see on that first page every single time you search something (and how often are you going past the first page?)

PageRank Your Friends

PageRank is currently implemented using concepts from graph theory, assigning scores of "relevance" to links. We're going to model that by doing the same thing to our social networks (what, you've never ranked your friends before?). This is how social media influence is calculated! Let's find out which of our fake friends have the most influence in the network:

Note: For the below challenge, you'll be using a directed weighted graph from the starter code, which can be found here

CODE GOES HERE

walk through implementing page rank on the graph, step by step
Clique through

So now you've ranked your fake friends (do they feel real, yet?), but as with any large group of people, smaller groups start to form within the larger ones. We can find these cliques through graph theory! One more chapter to go, you got this!

Chapter 8: On Wednesdays We Wear Pink

Find “cliques” of friends (small groups of tightly-connected users), etc…

The clique problem is a popular computational problem in computer science. Contrary to popular belief, this problem was not caused by people being personally victimized by Regina George.

mean girls

Source: Giphy

While we are confident that we're not bound by wearing pink on Wednesdays, solving clique problems is a whole other issue. These problems tend to be challenging, but it's nothing we can't take on!

Clique Discovery

Among other applications, the clique problem can arise in a social network. With our social network, a clique will represent a subset of people (nodes) who all know each other (share edges), and we can use various algorithms to find these cliques.

Challenge: Write a function that given a graph as input, finds INSERT SOMETHING ABOUT CLIQUES

CODE GOES HERE

walk through clique algorithm, step by step
Congrats on completing your journey through the Faker Network!

Feedback and Review - 2 minutes

We promise this won't take longer than 2 minutes!

Please take a moment to rate your understanding of the learning outcomes from this tutorial, and how we can improve it via our tutorial feedback form

This allows us to get feedback on how well the students are grasping the learning outcomes, and tells us where we can improve the tutorial experience.
