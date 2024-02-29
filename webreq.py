import requests
import json

def api_call():
    scryfall_bulk_url = "https://api.scryfall.com/bulk-data"

    bulk_res = requests.get(scryfall_bulk_url)
    print (bulk_res) #debugging purposes only

    with open("bulk_res.json", "w", encoding="utf-8") as temp_outf:
        temp_outf.write(bulk_res.text)