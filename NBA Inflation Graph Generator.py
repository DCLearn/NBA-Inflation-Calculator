#NBA inflation graoh generator
from os import stat
from re import X
import pandas as pd
import numpy as np
import statistics as stats
from statistics import mean
from statistics import stdev
from numpy import nan
import string
import matplotlib.pyplot as plt


NBA_means, NBA_STDs = {
}, {
}

print("Compare statistical category trends over a period in the NBA")
sc= str(input("Choose your category:  MP, FGM, FGA, FG%,3P, 3PA, 3P%, 2P, 2PA, 2P%, eFG%, FT, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV,  PF, PTS "))
first_year = int(input("earlier year "))
second_year = int(input("later year ")) + 1


for year in range(first_year,second_year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html#per_game_stats::pts_per_g"
    NBA_data=pd.read_html(url)[0]  
    NBA_data = NBA_data.drop(NBA_data.columns[[tuple(range(0,7))]], axis=1)
    
    means_list=[]

    for y in tuple(range(0,23)):
        x= NBA_data.iloc[:, y] #go through each column of the table
        x= x.values.tolist() #convert each column to a list

        x = [item for item in x if not(pd.isnull(item)) == True] #remove null or nan values


        rangey, stats_list=int(len(x) - 1), []
        for i in tuple(range(0,rangey)):
            if "." in x[i]: #x[i] is a number and not a stat title
                stats_list.append(float(x[i]))
            else: 
                continue


        if len(stats_list)>1: #the stat was actually recorded that year
            z=mean(stats_list)
            means_list.append(float(z))
          
        else: 
            means_list.append(float(0.0)) #stat wasn't recorded that year
          
            
        


    NBA_means[int(year)] = means_list
  

meanies = pd.DataFrame(NBA_means) 
meanies.index=['MP', 'FGM', 'FGA', 'FG%','3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',  'DRB',   'TRB',  'AST',  'STL',  'BLK',  'TOV',   'PF',   'PTS']

meanies= meanies.T #transpose data frame, swapping the x- and y- axis
meanies["Years"]= range(first_year,second_year) #add a column for years


meanies.plot.scatter(x='Years', y=sc, s=None, c=None)
plt.suptitle(" ".join ([sc, " Since ", str(first_year)]))
plt.show()
