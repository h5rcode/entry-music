#!/usr/bin/python3

import datetime
import json
import nmapclient
import omxplayerclient
import os
import os.path
import sys
import user

def get_last_connections():
	last_connections = None
	if os.path.isfile(last_connections_file_name):
        	with open(last_connections_file_name) as last_connections_file:
                	last_connections = json.load(last_connections_file)
	else:
        	last_connections = {}
	return last_connections

os.chdir(sys.path[0])

min_delta = datetime.timedelta(minutes = 15)
users_file_name = "users.config";
last_connections_file_name = "last-connections.json"

now = datetime.datetime.now()
last_connections = get_last_connections()

hosts = nmapclient.get_hosts()
users = user.User.load_users(users_file_name)

for user in users:
	user_address = user.address
	for host in hosts:
		is_connected = False
		for host_address in host.addresses:
			if host_address.address == user_address:
				is_connected = True
				break
		if is_connected:
			break

	if is_connected:
		should_play_music = False

		last_connection_date = None
		if user.hostname in last_connections:
			last_connection_date = datetime.datetime.strptime(last_connections[user.hostname], "%Y-%m-%dT%H:%M:%S.%f")

		if last_connection_date == None:
			should_play_music = True
		else:
			delta = now - last_connection_date
			if delta >= min_delta:
				should_play_music = True

		if should_play_music:
			file = "music/" + user.music
			omxplayerclient.play_sound(file)

		last_connections[user.hostname] = now.isoformat()

with open(last_connections_file_name, "w") as last_connections_file:
	json.dump(last_connections, last_connections_file)
