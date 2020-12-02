from flask import Flask
import requests
import json

url = "https://www.futbin.com/21/playerPrices?player="
app = Flask(__name__)
data = {}

with open('data.json') as json_file:
    data = json.load(json_file)

@app.route('/player/<search_term>')
def get_player(search_term):
    
    search_terms = search_term.split(" ")

    name = [name for name in data if "".join(search_terms).lower() in "".join(name.lower().split(" "))]

    if (len(name) > 1):
            print("Multiple Players found!")
            res = ""
            for name in name:
                res += name + "\n"
            return res

    if len(name) == 0:
        first = [name for name in data if search_terms[0].lower() in "".join(name.lower().split(" "))]
        second = [name for name in data if search_terms[1].lower() in "".join(name.lower().split(" "))]
        if (first[0] == second[0]):
            name = first[0]
        else: return "9999999"

    if len(name) == 0:
        return "9999999"

    name = name[0]
    player_id = data[name]
    print(name)
    print(player_id)
    r = requests.get(url+str(player_id))

    price = "".join(json.loads(r.text)[str(player_id)]["prices"]["ps"]["LCPrice"].split(","))
    if int(price) == 0:
        price = "".join(json.loads(r.text)[str(player_id)]["prices"]["ps"]["MinPrice"].split(","))

    return price
