import requests


professions = [
    {"label":"actor" ,"id":"wd:Q33999" },
    {"label":"musician" ,"id":"wd:Q639669" },
    {"label":"rapper" ,"id":"wd:Q2252262" },
    {"label":"writer" ,"id":"wd:Q36180" },
    {"label":"painter" ,"id":"wd:Q1028181" },
    {"label": "scientist","id":"wd:Q901"},
    {"label": "politician","id":"wdQ82955"},
]

#get query and add profession
query = open("./wiki-data/query.rq").read()

for profession in professions:
    #get query and add profession
    queryProfession = query.replace("<PROFESSION>",profession["id"])
    #send request
    url = 'https://query.wikidata.org/sparql'
    data:dict = requests.get(url, params = {'format': 'json', 'query': queryProfession}).json()["results"]["bindings"]
    #save data
    with open(f"wiki-data/results-{profession['label']}.csv", "w") as file:
        for entry in data:
            file.write(f'{entry["name"]["value"]},{entry["mothersname"]["value"]}\n')

