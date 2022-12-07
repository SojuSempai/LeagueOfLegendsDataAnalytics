'''
Anthony Nguyen
ISTA 161
Professor Thompson
12/01/2021

Contributers: Stackoverflow,
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read the 3 datasets
df1 = pd.read_csv("Challenger_Ranked_Games.csv")
df2 = pd.read_csv("GrandMaster_Ranked_Games.csv")
df3 = pd.read_csv("Master_Ranked_Games.csv")

# check their sizes
df1.shape , df2.shape , df3.shape

data = pd.DataFrame()

# we need to get the rank for each dataset
df1['rank'] = 'challenger'
df2['rank'] = 'grandMaster'
df3['rank'] = 'master'

# append all dataframe to a one df
data = data.append(df1, ignore_index=True)
data = data.append(df2, ignore_index=True)
data = data.append(df3, ignore_index=True)


#creats a scatter plot graph Blue side compared to Red side damage based on rank Challenger, Grandmasters, Masters 
plt.figure(figsize=(17 , 13))
plt.title("Relationship between RedChampionDamageDealt and BlueChampionDamageDealt based on rank" , fontsize = 19 , c ='red')
plt.xlabel("RedChampionDamageDealt" , fontsize=16 , c ='black')
plt.ylabel("BlueChampionDamageDealt" , fontsize=16 , c ='black')
sns.scatterplot(data['redChampionDamageDealt'] , data['blueChampionDamageDealt'] , hue = data['rank'])
plt.savefig("graph1_scatterplot.png")
plt.show()

# create a regression plot for the above two columns
#https://seaborn.pydata.org/tutorial/regression.html and https://www.geeksforgeeks.org/seaborn-regression-plots/ and https://stackoverflow.com/questions/41787143/overplot-seaborn-regplot-and-swarmplot with explinations from Randy Nguyen, and Tom Nguyen
plt.figure(figsize=(17 , 13))
plt.title("redChampionDamageDealt in relation to blueChampionDamageDealt for a sample size of 500" , fontsize = 19 , c ='red')
plt.xlabel("Red Side Damage Dealt" , fontsize=16 , c ='black')
plt.ylabel("Blue Side Damage Dealt" , fontsize=16 , c ='black')
sns.regplot(x="redChampionDamageDealt", y="blueChampionDamageDealt", data=df1[:500] , x_estimator=np.mean)
plt.show()

#creates histogram that shows the average amount of time for match
plt.figure(figsize=(15,10))
sns.distplot(data['gameDuraton']/60, hist=True, kde=False , color='#B85B14')
plt.title("Average duration distribution for the games recorded"  , fontsize =20 , c ='red')
sns.set(font_scale = 2)
plt.xlabel('Duration (time in minutes)')
plt.ylabel('Games Frequency (counts) ')
plt.savefig("graph2_gameduration.png")
plt.show()

print("Average game length: {:.2f} minutes".format(data['gameDuraton'].mean()/60))


# get correration between other variables and blueWins
blueWins_corr = data.drop('rank', axis=1).corr()['blueWins'][:].sort_values(axis=0, ascending=False) 
#get correration between other variables and blueWins
redWins_corr = data.drop('rank', axis=1).corr()['redWins'][:].sort_values(axis=0, ascending=False) 

#https://stackoverflow.com/questions/37790429/seaborn-heatmap-using-pandas-dataframe used this discussion to attempt my heatmap. With debugging guidence from Randy Nguyen, and Tom Nguyen
fig, (ax1 , ax2) = plt.subplots(1, 2, figsize=(20, 12))
fig.suptitle("Relationship between other variables and wins per side" , fontsize =22 , fontweight='bold' , c ='red')
redWins_correlation_cols = [col for col,corr_val in blueWins_corr.iteritems() if 'red' in col]
sns.heatmap(redWins_corr[redWins_correlation_cols].sort_values(
    axis=0, ascending=False).to_frame(), 
            annot=True, cbar=False, ax=ax1 , cmap='spring')
blueWins_correlation_cols = [col for col,corr_val in redWins_corr.iteritems() if 'blue' in col]
sns.heatmap(blueWins_corr[blueWins_correlation_cols].to_frame(), 
            annot=True, cbar=False, ax=ax2 , cmap='YlGnBu')
sns.set(font_scale = 1)
fig.tight_layout(w_pad=7)

# set titles
ax2.set_title("Correlation of other variables with Blue Wins" , fontweight = 'bold' , fontsize=17 , c ='blue')
ax1.set_title("Correlation of other variables with Red Wins" , fontweight = 'bold' , fontsize=17 , c ='red')
# set ticks params
ax2.xaxis.set_tick_params(which='both', rotation=45 , labelsize=20)
ax2.yaxis.set_tick_params(which='both', rotation=40 , labelsize=15)
ax1.xaxis.set_tick_params(which='both', rotation=45  , labelsize=20)
ax1.yaxis.set_tick_params(which='both', rotation=40  , labelsize=15)
fig.subplots_adjust(top=0.90)
plt.savefig("graph-3_Correlation.png")
plt.show()
