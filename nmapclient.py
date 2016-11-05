import subprocess
import xml.etree.ElementTree as ET

def get_device_addresses():
	file_name = "nmap-output.xml";

	returncode = subprocess.call(["nmap", "-sP", "192.168.1.0/24", "-oX", file_name]);

	tree = ET.parse(file_name);
	root = tree.getroot();

	addresses = [];
	for address in root.findall("./host/address[@addrtype='ipv4']"):
        	addresses.append(address.attrib["addr"]);

	return addresses;

