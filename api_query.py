import requests
import json

base_url = 'https://www.dnd5eapi.co/api/'

def get_query():
    query = input()
    query = query.lower()
    query = query.replace(' ', '-')
    return query

def get_resource(url):
    if (requests.get(url).status_code == 200):
        json_data =  requests.get(url).json()
        results = json_data["results"]
        for text in results:
            print(text["name"])

    else:
        print("Error 404: The resource you tried to access couldn't be found.")

print("What are you looking for? (Type 'help' for a list of options)")
query = get_query()

while (query != "done"):
    if (query != "help"):
        url = base_url + query
        get_resource(url)

    else:
        json_data = requests.get(base_url).json()
        keys = json_data.keys()
        for key in keys:
            print(key)

    print("\nWhat are you looking for? (Type 'help' for a list of options, type 'done' when finished)")
    query = get_query()