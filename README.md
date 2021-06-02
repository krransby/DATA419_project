# DATA419_project
Group project for DATA419: Online Communities and Social Networks (21S1)


We are required to:
- [x] Formulate a research question regarding one (or more) online community
- [x] Gather the necessary data (if legal and ethical)
- [x] Choose the right statistical techniques
- [ ] Explain your results in a concise but technically rigorous report (with the necessary visualisations)


### Research question:
Can a network's structure be used to predict the growth of a community?


### Data source and collection method:
* Data will be collected from Twitter using the ![twint](https://github.com/twintproject/twint) tool. 
* It will be collected in chunks of 7 days (1 week) over a period of 1 year (52 weeks).
* The twint search parameters will be ... (see network_scraper.py).


## Work distrobution:

**Network:** - Kayle
* Which? - 2020 Elections in New Zealand.
* Where? - Twitter, ~~within New Zealand geolocation.~~
* When? - 1 week chunks over from 2020 (52 chunks).


**Structure:** - House
* Average degree: simply the average number of edges per node in the community.	
* Modularity: Modularity is a measure of the structure of networks or graphs which measures the strength of division of a network into modules (also called groups, clusters or communities).	
* Transitivty: Transitivity is the overall probability for the network to have adjacent nodes interconnected, thus revealing the existence of tightly connected communities (or clusters, subgroups, cliques).
* Motif Distribution: Network motifs are recurrent and statistically significant subgraphs or patterns of a larger graph.	
* Density: describes the portion of the potential connections in a network that are actual connections.
![image](https://user-images.githubusercontent.com/65093375/120415568-e09cd600-c3af-11eb-83af-160370adea77.png)


**Community:** - Nana  

Methods to detect groups according to different parameters:  
•	**group_components**: Group by connected compenents  
•	**group_edge_betweenness**: Group densely connected nodes  
•	**group_fast_greedy**: Group nodes by optimising modularity  
•	**group_infomap**: Group nodes by minimizing description length  
•	**group_label_prop**: Group nodes by propagating labels  
•	**group_leading_eigen**: Group nodes based on the leading eigenvector of the modularity matrix  
•	**group_louvain**: Group nodes by multilevel optimisation of modularity  
•	**group_optimal**: Group nodes by optimising the moldularity score  
•	**group_spinglass**: Group nodes using simulated annealing  
•	**group_walktrap**: Group nodes via short random walks  
•	**group_biconnected_component**: Group edges by their membership of the maximal binconnected components  

In this project, we are using **group_louvain** to seperate community.

**Growth:** - Nana  

The definition for community growth:  
  After the detection of community week by week, Look at the communities from week(n) and week(n+1):    
    For each community from week(n), repeat the comparation with all the communities from week(n+1):  
    -> 1, if none of them having intersection, we call the community died;  
    -> 2, if some of them having certain size of intersection with the chosen community from week(n):  
      ---> 2.a, calculate the proportion of the intersection against the chosen community from week(n).  
      ---> 2.b, if the proportion bigger than the threshold (0.3 for example), we call the community from week(n) "Father", and the community from week(n+1) "Son".  
      
This growth method will make a many-to-many relatonship for father and son community.  

**Predit:** - Selina
* How?


## Data structures:

### Scraped data:
| id | conversation_id | date | user_id | username | mentions | hashtags | replies_count | retweets_count | likes_count | tweet | urls | week |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Tweet ID | Conversation ID the tweet is part of | Date the tweet was posted | User's ID | User's Handle | Mentioned users | Hashtags used in tweet | # Replies to tweet | # retweets | # likes the tweet has | Tweet content (may be corrupted) | URL(s) in the tweet | Week the tweet was posted |

(please see the ![cleaned tweet .csv file](https://github.com/krransby/DATA419_project/blob/main/Tweet%20file/tweets_cleaned_week.csv) for up-to-date data)


### Statistical techniques to use as predictors:
| Average Degree | Modularity | Transitivty Ratio / Clustering Coefficient | Motif Distrobution | Density |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|  |  |  |  | D = L/N |

(These predictors will be based on each community within the one-week period)

### Inputs required for prediction:

| Y | Predictors | Group | Time |
| ------------- | ------------- | ------------- | ------------- |
| Target value | Predictors (in table above) | Community ID | Time ('week' field in first table) |

## Lab sessions:

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
