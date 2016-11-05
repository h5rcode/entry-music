#!/usr/bin/python3

import nmapclient
import sms

addresses = nmapclient.get_device_addresses();

message = "Addresses of the devices currently connected to the network:\n{0}".format("\n".join(addresses));

sms.send_message(message);
