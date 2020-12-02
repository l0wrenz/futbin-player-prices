# futbin-player-prices
## Requirements

Python >= 3.6

[Flask](https://flask.palletsprojects.com/en/master/installation/)

## Installation

clone repository

```
pip install -r requirements.txt
```

-> Follow Flask installation

## Usage

Open browser at localhost:5000/player/"insert player name here"

The name can be fuzzy, but must contain enough information to properly identify a player:

Example:

"localhost:5000/player/messi"

-> Lionel "Messi" or Junior "Messi"as

"localhost:5000/player/onel mes" Li"onel Mes"si

-> Lionel Messi