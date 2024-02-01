## QUESTION 1

pokemon = [
    {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "is_default": True,
        "order": 1,
        "weight": 20,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "chlorophyll",
                    "url": "http://pokeapi.co/api/v2/ability/34/",
                },
            }
        ],
    },
    {
        "id": 3,
        "name": "venesaur",
        "base_experience": 50,
        "height": 10,
        "is_default": True,
        "order": 1,
        "weight": 30,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "fire",
                    "url": "http://pokeapi.co/api/v2/ability/38/",
                },
            }
        ],
    },
    {
        "id": 2,
        "name": "pikachu",
        "base_experience": 60,
        "height": 4,
        "is_default": True,
        "order": 1,
        "weight": 37,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "lightning",
                    "url": "http://pokeapi.co/api/v2/ability/30/",
                },
            }
        ],
    },
]


# How would you get the url for Bulbasaur's ability?

def get_bulb():
    for poke_obj in pokemon:
        if poke_obj["name"] == "bulbasaur":
            return poke_obj["abilities"][0]["ability"]["url"]
            
print(get_bulb())

# How would you return the first pokemon with base experience over 40?

def first_base_poke():
    for poke_obj in pokemon:
        if poke_obj["base_experience"] > 40:
            return poke_obj["name"]

print(first_base_poke())

# How would you return ALL OF THE pokemon with base experience over 40? (Gotta catch em all)

base_exp_ovr = [poke_obj for poke_obj in pokemon if poke_obj["base_experience"] > 40]

print(base_exp_ovr)

# How would you return an array of all of the pokemon's names?

poke_names = [poke_obj["name"] for poke_obj in pokemon]

print(poke_names)



# How would you determine whether or not the pokemon array contained any pokemon with a weight greater than 60?
# Whatever method you use should return True if there are any such pokemon, False if not.

def poke_weights():
    for poke_obj in pokemon:
        if poke_obj["weight"] > 60:
            return True
        else:
            print("No Snorlax Here")
            return False

print(poke_weights())

