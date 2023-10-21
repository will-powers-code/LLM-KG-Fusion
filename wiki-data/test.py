"""
#return name and mother's name
SELECT DISTINCT ?name ?mothersname
WHERE {
  #select items with occupation 
  ?item wdt:P106 <PROFESSION>.
  #get labels for actor names
  ?item rdfs:label ?name filter(lang(?name) = "en").
  #get mother id 
  ?item wdt:P25  ?mother.
  #get names of mothers
  ?mother rdfs:label ?mothersname filter(lang(?mothersname) = "en").

  #filter for mothers that have no wikipedia article
  filter not exists{?article schema:about ?mother}
  #filter for mothers names with a last name
  filter exists{?mother wdt:P734 ?val}

}
LIMIT 10000
""".format("xyz")