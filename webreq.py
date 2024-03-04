import requests
import json

def bulk_meta_call():
    scryfall_bulk_url = "https://api.scryfall.com/bulk-data"

    bulk_meta_res = requests.get(scryfall_bulk_url)
    print (bulk_meta_res) #debugging purposes only, will not be included in full release

    with open("bulk_meta.json", "w", encoding="utf-8") as temp_outf:
        temp_outf.write(bulk_meta_res.text)

def dc_call():
    bulk_meta_json = open("./bulk_meta.json", encoding="utf-8")
    json_dat = json.load(bulk_meta_json)

    data_dat = json_dat.get("data")
    dc_dat_uri = data_dat[2].get("uri")
    dc_dat_date = data_dat[2].get("updated_at")

    scryfall_dc_bulk_uri = dc_dat_uri

    dc_meta_res = requests.get(scryfall_dc_bulk_uri)
    print (dc_meta_res) #debugging purposes only, will not be included in full release

    #maybe change file name to scryfall id
    with open("dc_bulk_meta.json", "w", encoding="utf-8") as temp_outf:
        temp_outf.write(dc_meta_res.text)

def ac_call():
    bulk_meta_json = open("./bulk_meta.json", encoding="utf-8")
    json_dat = json.load(bulk_meta_json)

    data_dat = json_dat.get("data")
    ac_dat_uri = data_dat[3].get("uri")
    ac_dat_date = data_dat[3].get("updated_at")

    scryfall_ac_bulk_uri = ac_dat_uri

    ac_meta_res = requests.get(scryfall_ac_bulk_uri)
    print (ac_meta_res) #debugging purposes only, will not be included in full release

    #maybe change file name to scryfall id
    with open("dc_bulk_meta.json", "w", encoding="utf-8") as temp_outf:
        temp_outf.write(ac_meta_res.text)