import json

nytimes = json.load(open('malaysia_pretty_printed.json', 'r'))
print ','.join(['contributor','pub date','section','subsection','wordcount','url'])

for article in nytimes['response']['docs']:
	print '"' + '","'.join([article['byline']['person'][0]['lastname'],
		article['pub_date'],
        article['section_name'],
        article['subsection_name'],
        article['word_count'],
        article['web_url']]) + '"'