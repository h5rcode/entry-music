#!/usr/bin/python3

import datetime
import json
import nmapclient
import omxplayerclient
import os
import os.path
import sys

os.chdir(sys.path[0])

addresses = nmapclient.get_device_addresses();

minutes_since_last_connection = 15;

hosts = None;
if os.path.isfile("hosts.json"):
	with open("hosts.json") as hosts_file:
        	hosts = json.load(hosts_file);
else:
	hosts = [];

new_hosts = [];
current_hosts = hosts[:];
now = datetime.datetime.now();
min_delta = datetime.timedelta(minutes = minutes_since_last_connection);

for address in addresses:
	address_host = None;
	play_song = False;
	for host in hosts:
		host_address = host["address"]
		if (host_address == address):
			address_host = host;
			break;

	if address_host == None:
		play_song = True;
		address_host = {
			"address": address
		};
		current_hosts.append(address_host);
	else:
		last_seen = datetime.datetime.strptime(address_host["lastSeen"], "%Y-%m-%dT%H:%M:%S.%f");
		delta = now - last_seen;

		if (delta >= min_delta):
			play_song = True;

	address_host["lastSeen"] = now.isoformat();

	if (play_song):
		new_hosts.append(address_host["address"]);
		omxplayerclient.play_sound("music/example.mp3");

with open("hosts.json", "w") as hosts_file:
	json.dump(current_hosts, hosts_file);
