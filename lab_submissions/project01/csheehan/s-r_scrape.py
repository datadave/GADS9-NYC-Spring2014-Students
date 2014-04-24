# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from bs4 import BeautifulSoup
from os import listdir, path
from urllib2 import urlopen
import re
#import sleep from time

# <codecell>

def get_flds(soup):
    div_tbls = soup.findAll('div',{'class':'table_container'})
    for tbl in div_tbls:
        if tbl['id'] != 'div_four_factors':
            for c in tbl.thead.children:
                if c.name == 'tr':
                    fields = ['game']
                    for th in c:
                        if th.string !='\n':
                            fields.append(th.string)
    
    fields[0] = "Name"
    fields.insert(0,'Team')
    return  fields

# <codecell>

def get_stats(soup, file):
    stats = []
    div_tbls = soup.findAll('div',{'class':'table_container'})
    for tbl in div_tbls:
        if tbl['id'] != 'div_four_factors':
            tm = tbl['id'].replace('div_', '')
            for c in tbl.tbody.children:
                if c.name == 'tr' and len(c['class']) == 1:
                    row = [file.replace('box_scores/',''),tm]
                    for td in c:
                        if td.string !='\n':
                            if td.string is None:                                
                                row.append(str(0))
                            else:
                                row.append('"' + td.string + '"')
                    stats.append(row)
    return stats

# <codecell>

def write_stats(file, targetName, get_header = False):
    f = open(file)
    soup = BeautifulSoup(f.read())
    write = ''
	#get flds by function
    if get_header == True:
		flds = get_flds(soup)
		write = ','.join(flds)
    #get stats by function
    stats = get_stats(soup, file)
    
    #write = ','.join(flds)
    for stat in stats:
        write += '\n' + ','.join(stat)
	
    fwrite = open(targetName, 'a')	#write string to file (append)
    fwrite.write(write)
    fwrite.close()
    #print file + ' processed.'

# <codecell>

def get_teams(soup):
    teams = {}
    div_tms = soup.find('table',{'id':'ratings'})
    for tr in div_tms.tbody:
        t = re.search('/cbb/schools/(?P<school_tag>.+)/2014.html', str(tr))
        c = re.search('/cbb/conferences/(?P<school_conf>.+)/2014.html', str(tr))
        if t is not None and c is not None:
            tm =  t.groupdict('school_tag')['school_tag']
            con =  c.groupdict('school_conf')['school_conf']
            teams[tm] = {'conf': con, 'roster': {}}
    return teams

# <codecell>

def calc_inches(str_height):
    h = str_height.split("-")
    h = int(h[0])*12 + int(h[1])
    return h

def get_roster_flds(team):
    url = "http://www.sports-reference.com/cbb/schools/{}/2014.html".format(team)
    page = urlopen(url)
    soup = BeautifulSoup(page.read())
    roster = soup.find('table',{'id':'roster'})
    for c in roster.thead.children:
        if c.name == 'tr':
            fields = ['Team']
            for th in c:
                if th.string !='\n':
                    fields.append(th.string)
    return fields[:5]
                        
                        
def get_roster(team):
    url = "http://www.sports-reference.com/cbb/schools/{}/2014.html".format(team)
    page = urlopen(url)
    soup = BeautifulSoup(page.read())
    roster = soup.find('table',{'id':'roster'})
    players = {}
    for c in roster.tbody.children:
        if c.name == 'tr':
            player = []
            for td in c:
                if td.string !='\n':
                    player.append(td.string)
            player[3] = calc_inches(player[3])
            players[player[0]] = player[1:4]
    return players

# <codecell>

url = "http://www.sports-reference.com/cbb/seasons/2014-ratings.html"
page = urlopen(url)
soup = BeautifulSoup(page.read())
teams =  get_teams(soup)
teams

# <codecell>

fwrite = open('teams.csv', 'a')
fwrite.write('team,conf' + '\n')

for t,d in teams.iteritems():
    fwrite.write(t + ',' + d['conf'] + '\n')
fwrite.close()    

# <codecell>

keys = teams.keys()
keys.sort()

#flds = get_roster_flds(keys[0])
#fwrite = open('rosters.csv', 'a')
#fwrite.write(','.join(flds) + '\n')
#fwrite.close()

roster = []
for key in keys[:10]:
    teams[key]['roster'] =  get_roster(key)
    c = teams[key]['conf']
    for play,vals in teams[key]['roster'].iteritems():
        row = [key,'"' + play + '"']
        for v in vals:
            row.append(str(v))
        fwrite = open('rosters.csv', 'a')
        fwrite.write(','.join(row) + '\n')
        fwrite.close()
        #time.sleep(2)

print "Rosters compiled"

# <codecell>

files = listdir('box_scores') # where box is directory in pwd with HTML files of box scores (with .txt suffix)
files.sort()
#len(files) = 5719
#write_stats('box_scores/'+files[0], "boxes.csv", True)
#[3035:3186]
#3821-2 = problems
for f in files[3186:3500]:
    print f
    write_stats('box_scores/'+f, "boxes.csv")

print "Done pulling files."

# <codecell>


