import json

def import_data_to_database(database):
    with open("app/data/rick_morty-characters.json") as jFile:
        dict_rick_morty_charaters = json.load(jFile)

    with open("app/data/rick_morty-episodes.json") as jFile:
        dict_rick_morty_episodes = json.load(jFile)

    # Fetch all dictionnary "episodes" to insert on db
    for episode in dict_rick_morty_episodes:
        database.insert("episodes", id = episode.get("id"), name = episode.get("name"), 
                    air_date = episode.get("air_date"), episode = episode.get("episode"))


    # Fetch all dictionnary "characters" to insert on db
    for character in dict_rick_morty_charaters:
        database.insert("characters", id = character.get("id"), name = character.get("name"), 
                            status = character.get("status"), species = character.get("species"), 
                            type = character.get("type"), gender = character.get("gender"))
                            
        # Fetch all episode when the character appears to insert on db
        for episode_appeared in character.get("episode"):
            database.insert("characters_episodes", id_character = character.get("id"), id_episode = episode_appeared)

    


