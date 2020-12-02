from flask import Flask
from flask_cors import CORS
import requests
import json

url = "https://www.futbin.com/21/playerPrices?player="
app = Flask(__name__)
CORS(app)
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

    if (len(name) == 0 and len(search_terms) > 1):
        first = [name for name in data if search_terms[0].lower() in "".join(name.lower().split(" "))]
        second = [name for name in data if search_terms[1].lower() in "".join(name.lower().split(" "))]

        for second_name in second:
            if second_name in first:
                name = [second_name]
                print(name)

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
