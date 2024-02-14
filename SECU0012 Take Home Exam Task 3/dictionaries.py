witness_data_dict = { # nested dictionary for all witnesses
    1: {
        "Age": 34,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    2: {
        "Age": 47,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "scooter",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    3: {
        "Age": 37,
        "Victim/Witness?": "dont know",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": "two",
    },
    4: {
        "Age": 34,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "running",
        "Gender involved": "female",
        "Number of attackers": "two",
    },
    5: {
        "Age": 39,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "scooter",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    6: {
        "Age": 32,
        "Victim/Witness?": "dont know",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    7: {
        "Age": 29,
        "Victim/Witness?": "dont know",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    8: {
        "Age": 28,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "scooter",
        "Gender involved": "female",
        "Number of attackers": "two",
    },
    9: {
        "Age": 43,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    10: {
        "Age": 30,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "scooter",
        "Gender involved": "female",
        "Number of attackers": "two",
    }
}

for key, inner_dict in witness_data_dict.items(): # looks through all keys in witness_data_dict
    age = inner_dict.get("Age")  # gets the value for "Age" 
    print(f"Witness, Age: {age}")

victim_data_dict = { # nested dictionary for all victims 
    1: {
        "Age": 32,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    2: {
        "Age": 27,
        "Victim/Witness?": "dont know",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "two",
    },
    3: {
        "Age": 25,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "running",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    4: {
        "Age": 23,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    5: {
        "Age": 28,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "bike",
        "Gender involved": "female",
        "Number of attackers": "two",
    },
    6: {
        "Age": 37,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    7: {
        "Age": 38,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": "two",
    },
    8: {
        "Age": 39,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "running",
        "Gender involved": "male",
        "Number of attackers": "one",
    },
    9: {
        "Age": 42,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "scooter",
        "Gender involved": "female",
        "Number of attackers": "one",
    },
    10: {
        "Age": 45,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "dont know",
        "Gender involved": "male",
        "Number of attackers": "one",
    }
}

for key, inner_dict in victim_data_dict.items(): # looks through all keys in victim_data_dict
    age = inner_dict.get("Age")  # gets the value for "Age" 
    print(f"Victim, Age: {age}")


add_data_dict = { # nested dictionary for additional data
    1: {
        "Age": 19,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "bike",
        "Gender involved": "male",
        "Number of attackers": 1,
    },
    2: {
        "Age": 24,
        "Victim/Witness?": "victim",
        "Crime perpetrated by": "scooter",
        "Gender involved": "dont know",
        "Number of attackers": 2,
    },
    3: {
        "Age": 22,
        "Victim/Witness?": "witness",
        "Crime perpetrated by": "scooter",
        "Gender involved": "women",
        "Number of attackers": 3,

    }
}

# Print add_data_dict for witness_data_dict
for key in [1, 3]: # looks at dictionaries 1 to 3 in nested dictionary add_data_dict 
    if key in add_data_dict: # looks through every key 
        age = add_data_dict[key].get("Age") # gets "Age" key 
        print(f"Added Witness, Age: {age}")

# Print add_data_dict for victim_data_dict
for key in [2]: # looks at dictionary 2 in nested dictionary add_data_dict 
    if key in add_data_dict: # looks through every key 
        age = add_data_dict[key].get("Age") # gets "Age" key 
        print(f"Added Victim, Age: {age}")






