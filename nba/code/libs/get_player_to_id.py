import json

def get_player_to_id():
	with open('info/player_to_id.json', 'r') as f:
		player_to_id = json.load(f)
	return player_to_id
