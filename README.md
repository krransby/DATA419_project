# DATA419 Assessment 4: Group Research Project
Group project for DATA419: Online Communities and Social Networks (21S1)


### Research question:
Can we use a community's structure to predict the growth and future of that community?


## Work distrobution:

**Network Data:** - Kayle

Which topic are we using?
* The five parliamentary parties in the 53rd New Zealand Parliament. 
* The MPs these parties currently have.

Where are we getting the data?
* Twitter, ~~from posts within the New Zealand geolocation.~~
* Data will be collected from Twitter using the ![twint](https://github.com/twintproject/twint) tool.

What time period will the data be from?
* The data will be a time series.
* It will be collected in chunks of 7 days (1 week) over a period of 1 year (52 weeks).
* Scraping will work back in time from 17-10-2020 (The end of the 2020 election in NZ).


**Network properties to use as predictors:** - House
* Average degree: simply the average number of edges per node in the community.	
* Modularity: Modularity is a measure of the structure of networks or graphs which measures the strength of division of a network into modules (also called groups, clusters or communities).	
* Transitivty: Transitivity is the overall probability for the network to have adjacent nodes interconnected, thus revealing the existence of tightly connected communities (or clusters, subgroups, cliques).
* Motif Distribution: Network motifs are recurrent and statistically significant subgraphs or patterns of a larger graph.	
* Density: describes the portion of the potential connections in a network that are actual connections.

**Community Detection:** - Nana  

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

**Defining Growth:** - Nana  

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
| id | conversation_id | date | user_id | username | mentions | hashtags | replies_count | retweets_count | likes_count | urls | week |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |

(please see the ![cleaned tweet .csv file](https://github.com/krransby/DATA419_project/blob/main/Tweet%20file/tweets_cleaned_week.csv) for up-to-date data)


### Statistical techniques to use as predictors:
| Average Degree | Transitivty Ratio / Clustering Coefficient | 3-Motif Distrobution | 4-Motif Distrobution | Density |
| ------------- | ------------- | ------------- | ------------- | ------------- |

(These predictors will be based on each community within the one-week period)

### Inputs required for prediction:

| expected Y | predictors | community_id | week | next week expected Y | next week predictors | next week community_id |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |

(Expected Y will either be the number of nodes or the number of edges in the given community for that week)
