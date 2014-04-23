# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%matplotlib inline
# from pylab import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# <codecell>

players = pd.read_csv('rosters_final.csv')

# <codecell>

df = pd.DataFrame(players)

# <codecell>

df[df.Pos == 'W'].Pos
df.loc[104,'Pos'] = 'G-F'
df.loc[3731,'Pos'] = 'G-F'

# <codecell>

df.Pos.unique()

# <codecell>

# Splitting up the positions

positions = set()
for p in df.Pos:
    positions.update(pos for pos in p.split('-'))
    
for pos in positions:
    df[pos] = [pos in player.split('-') for player in df.Pos]

# <codecell>

df.Class.unique()

# <codecell>

df[df.Class == 'So'].index

# <codecell>

df.loc[[1399,2954],'Class'] = 'SO'

# <codecell>

df[df.Class == 'F']

# <codecell>

df.loc[[3507,3509],'Class'] = 'FR'

# <codecell>

df.Class.unique()

# <codecell>

df.describe()

# <codecell>

df.head()

# <codecell>

teams = pd.read_csv('teams.csv')

# <codecell>

tm_df = pd.DataFrame(teams)
tm_df.columns = ['Team', 'Conf']
tm_df.head()

# <codecell>

tms_players = pd.merge(df, tm_df, how='inner', on='Team', left_on=None, right_on=None,
      left_index=False, right_index=False, sort=True)
tms_players.head(5)

# <codecell>

gms = pd.read_csv('boxes.csv')

# <codecell>

gms_df = pd.DataFrame(gms)
gms_df.rename(columns={'Team': 'Game', 'Name': 'Team', 'Starters': 'Player'}, inplace=True)
gms_df.head()

# <codecell>

tms_gms_players = pd.merge(tms_players,gms_df, how='inner', on=['Team', 'Player'])

# <codecell>

pd.set_option('display.max_columns', 50)
tms_gms_players.iloc[0:5,:32]
tms_gms_players.head()
tgp = tms_gms_players

# <codecell>

tgp.columns

# <codecell>

tgp.groupby(tgp.Conf).Ht.min()

# <codecell>

#
fig,ax1 = plt.subplots(1,1)
ax1.hist(tgp.Ht,bins=np.arange(tgp.Ht.min(),tgp.Ht.max()),color='#B8D12A', lw=0.5)
ax1.set_title('Frequency of Height')
ax1.set_xlabel('Height (Inches)')

# <codecell>

tgp.describe()

# <codecell>

plt.figure(figsize=(10,5))
plt.scatter(tgp.MP, tgp.PTS, lw=0, color='#B8D12A', alpha=.5)
plt.axis([0,tgp['MP'].max(),0,tgp['PTS'].max()])
plt.xlabel("Minutes Played")
plt.ylabel("Points Scores")
plt.title("Points Scored by Minutes Played",fontsize='15')

# <codecell>

plt.figure(figsize=(10,5))
plt.scatter(tgp.Ht, tgp.PTS, lw=0, color='#B8D12A', alpha=.5)
plt.axis([tgp['Ht'].min(),tgp['Ht'].max(),0,tgp['PTS'].max()])
plt.xlabel("Height")
plt.ylabel("Points Scores")
plt.title("Points Scored by Height",fontsize='15')

# <codecell>

conferences =  tgp.Conf.unique()
conferences.sort()
conferences

# <codecell>

# Compare height vs points across conferences
# create a 4x8 grid of plots.

fig, axes = plt.subplots(nrows=8, ncols=4, figsize=(16, 24), tight_layout=True)
bins = np.arange(tgp.Ht.min(),tgp.Ht.max())

conferences =  tgp.Conf.unique()
conferences.sort()
#conferences = conferences[:4]
for ax, con in zip(axes.ravel(), conferences): # Each of 32 axes gets a conference
    ax.scatter(tgp[tgp.Conf == con].Ht, tgp[tgp.Conf == con].PTS, lw=0, color='#B8D12A', alpha=.5)
    ax.axis([tgp['Ht'].min(),tgp['Ht'].max(),0,tgp['PTS'].max()])
    ax.set_xlabel("Height (Inches)")
    ax.set_ylabel("Points Scores")
    ax.annotate(con, xy=(65,40),fontsize=14)    

# <codecell>

tgp.info()

# <codecell>

tgp.MP[tgp.MP==0] = np.nan
tgp.MP[tgp.MP==0] = np.nan

# <codecell>

tgp.columns

# <markdowncell>

# tgp.rename(columns={'FG%': 'FGp', '2P': 'FG2P', '2PA': 'FGA2P', '2P%': 'FGp2P', '3P': 'FG3P', '3PA': 'FGA3P', '3P%': 'FGp3P', 'FT%': 'FTp'}, inplace=True)
# 
# tgp.FG[np.isnan(tgp.MP)] = np.nan
# tgp.FGA[np.isnan(tgp.MP)] = np.nan
# tgp.FGp[np.isnan(tgp.MP)] = np.nan
# tgp.FG2P[np.isnan(tgp.MP)] = np.nan
# tgp.FGA2P[np.isnan(tgp.MP)] = np.nan
# tgp.FGp2P[np.isnan(tgp.MP)] = np.nan
# tgp.FG3P[np.isnan(tgp.MP)] = np.nan
# tgp.FGA3P[np.isnan(tgp.MP)] = np.nan
# tgp.FGp3P[np.isnan(tgp.MP)] = np.nan
# tgp.FT[np.isnan(tgp.MP)] = np.nan
# tgp.FTA[np.isnan(tgp.MP)] = np.nan
# tgp.FTp[np.isnan(tgp.MP)] = np.nan
# tgp.ORB[np.isnan(tgp.MP)] = np.nan
# tgp.DRB[np.isnan(tgp.MP)] = np.nan
# tgp.TRB[np.isnan(tgp.MP)] = np.nan
# tgp.AST[np.isnan(tgp.MP)] = np.nan
# tgp.STL[np.isnan(tgp.MP)] = np.nan
# tgp.BLK[np.isnan(tgp.MP)] = np.nan
# tgp.TOV[np.isnan(tgp.MP)] = np.nan
# tgp.PF[np.isnan(tgp.MP)] = np.nan
# tgp.PTS[np.isnan(tgp.MP)] = np.nan
# 
# 

# <codecell>

categories = ['TRB','AST','STL','BLK','PTS']
stats = {2:'double-double', 3:'triple-double',4:'quadruple-double',5:'quintuple-double'}
categories,stats

# <codecell>

def mess_around(obs):
    categories = ['TRB','AST','STL','BLK','PTS']
    n = 0
    for c in categories:
        #print obs[c]
        if int(obs[c]) >= 10:
            n+=1
    return n

# <codecell>

#for x,stat in stats.iteritems():
#tgp[double_double] = [mess_around(gm) for gm in tgp]
#print mess_around(tgp[15656:15657])

# <codecell>

tgp.info()

# <codecell>

tgp[(tgp.PTS > 10) & (tgp.TRB >= 10) & (tgp.AST >= 10)].tail()

