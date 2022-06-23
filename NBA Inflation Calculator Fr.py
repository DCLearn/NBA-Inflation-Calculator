#NBA Inflation Calculator Fr

import pandas as pd
import numpy as np
import statistics as stats
from statistics import mean
from statistics import stdev


print("Compare a stat in one era to the stats in another ")
sc= str(input("Choose your category:  MP, FGM, FGA, FG%,3P, 3PA, 3P%, 2P, 2PA, 2P%, eFG%, FT, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV,  PF, PTS"))
stattie = int(input("What was the numerical value of the stat? Ex. 10 TRB, the numerical value is 10."))
first_year = int(input("What year was the stat achieved?"))
second_year = int(input("What year do you want to compare it to?"))

NBA_means, NBA_STDs = {
}, {
}

def this_function(i):

        url = "https://www.basketball-reference.com/leagues/NBA_" + str(i) + "_per_game.html#per_game_stats::pts_per_g"
        NBA_data = pd.read_html(url)[0]  #read the first table
        NBA_data = NBA_data.drop(NBA_data.columns[[tuple(range(0,7))]], axis=1) #remove unneccessary columns, age, team, games played etc.
        
        means_list, std_list, stat_cat = [], [], ['MP', 'FGM', 'FGA', 'FG%','3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',  'DRB',   'TRB',  'AST',  'STL',  'BLK',  'TOV',   'PF',   'PTS'] 
        
        w = stat_cat.index(sc) #retreive the index for the specific stat
        x= NBA_data.iloc[:,w] #retrieve column for specifc stat category
        x= x.values.tolist() #convert each column to a list

        x = [item for item in x if not(pd.isnull(item)) == True] #remove null or nan values

        rangey =int(len(x) - 1) 
    
        stats_list = [float(x[j]) for j in tuple(range(rangey)) if "." in x[j]] #only number remain, stat titles are removed
        
        if len(stats_list)>1: #the stat was actually recorded that year
            z=mean(stats_list)
            a=stdev(stats_list)
            means_list.append(float(z))
            std_list.append(float(a))
        else: 
            means_list.append("No Stat") #stat wasn't recorded that year
            std_list.append("No Stat")
            
        NBA_means[int(i)] = means_list
        NBA_STDs[int(i)] = std_list
        

this_function(first_year)
this_function(second_year)

meanies = pd.DataFrame(NBA_means)
VenD = pd.DataFrame(NBA_STDs)

if "No Stat" in NBA_STDs|NBA_means:
    print("Sorry, this statistic was not recorded in both years")
else:
    f = (stattie-NBA_means[first_year][0])/NBA_STDs[first_year][0] # f= x - mean1/stdev1
    g = (f * NBA_STDs[second_year][0]) + NBA_means[second_year][0] # g = f * stdev2/mean2
    print(g)

