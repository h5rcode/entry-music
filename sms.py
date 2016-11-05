import json
import urllib.request

def send_message(message):
	with open("sms.config") as sms_config_file:
		sms_config = json.load(sms_config_file);

	data = {
	        "user": sms_config["user"],
	        "pass": sms_config["password"],
	        "msg": message
	};

	params = json.dumps(data).encode("utf-8");
	req = urllib.request.Request(sms_config["url"], data=params, headers = { "Content-type": "application/json" });

	urllib.request.urlopen(req);
