import json
import os.path
import user

class User:
	def __init__(self, hostname, address, music):
		self.hostname = hostname;
		self.address = address
		self.music = music
		self._last_connection_date = None

	def _get_last_connection_date(self):
		return self._last_connection_date

	def _set_last_connection_date(self, last_connection_date):
		self._last_connection_date = last_connection_date

	last_connection_date = property(_get_last_connection_date, _set_last_connection_date)

	@staticmethod
	def load_users(file):
		json_users = None
		if os.path.isfile(file):
		        with open(file) as users_file:
	                	json_users = json.load(users_file)
		else:
		        json_users = []

		users = []
		for json_user in json_users:
			hostname = json_user["hostname"]
			address = json_user["address"]
			music = json_user["music"]
			users.append(user.User(hostname, address, music))

		return users
