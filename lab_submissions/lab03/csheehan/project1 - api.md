a. A quick explanation of the website you're working from (or where the data comes from)
	Sports-Reference.com/cbb is the college hoops section of the sports-reference website. It is the family of sites that runs baseball-reference and pro-football-reference.com.
b. A description of what's available (either api, scraping, or some other service)
	There is no API, but I've been able to use BeautifulSoup to scrape team conferences and rosters, and daily box scores for the 2013/14 season. All told, adding up every player's box score for every game yields ~115k records, but I assume that number will drop significantly once the records are filtered for a minimum minutes played.
c. An explanation of what you want to investigate with some basic stats and plotting
	I think it might be interesting to compare which teams and conferences have different positions as their highest scoring/assisting/rebounding players. I'm also interested to see whether teams with the highest offensive and defensive ratings skew taller or shorter.
