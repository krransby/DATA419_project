# DATA419_project
Group project for DATA419: Online Communities and Social Networks

```
We will be required to:
 - Formulate a research question regarding one (or more) online community
 - Gather the necessary data (if legal and ethical)
 - Choose the right statistical techniques
 - Explain your results in a concise but technically rigorous report (with the necessary visualisations)
```

### Research question:
Can a network's structure be used to predict the growth of a community


### Data source and collection method:
* Data will be collected from Twitter using the ![twint](https://github.com/twintproject/twint) tool. 
* It will be collected in chunks of 24 hours (1 day) over a period of ...
* The twint search parameters will be ...


### Statistical techniques:
* Transitivty
* Motif Distrobution
* . . .


## Work distrobution:

**Network:** - Kayle
* Which?
* Where?
* When?


**Structure:** - House
* What?


**Community:** - Nana
* How do we find them?

**Growth:** - Nana
* How do we measure it?
```
Lab Session at 12/05/2021 -nana 

Community definition (taking the network between users sharing conversation as an example)  
Research analyst objects:  
            the tweets user and the interaction network whether or not they share the same conversation.  
 Node:  
            tweet users  
 Edge:  
            values = 1 if two users have commented on the same tweet post.  
            values = 0 if two users never have commented on the same tweet post.  
 Adjacency matrix A:    
            Build up the network matrix.    
 Detect clustering on matrix A at time t:  
            Find the connected network, define it as a cluster, record the nodes number, edge number, degrees on the node, density, etc.  
            After computing, get a number of clusters, mark it as the original community(communities).  
 Detect clustering on matrix A at time t+1:  
            Repeat the step above, check the differences on original community(nodes number, edge number, degrees on node, density, etc)  
 Community growth:  
            To be discussed: the number (the density) change over a certain period of time                       
 More to include:  
            The weight of edge  
            Network on a different relationship: like “mentions” instead of conversation  
```

**Predit:** - Selina
* How?
