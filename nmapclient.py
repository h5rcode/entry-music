import address
import host
import subprocess
import xml.etree.ElementTree as ET

def get_hosts():
	file_name = "nmap-output.xml";

	subprocess.call(["nmap", "-sP", "192.168.1.0/24", "-oX", file_name]);

	tree = ET.parse(file_name);
	root = tree.getroot();

	hosts = [];
	for host_element in root.findall("./host"):
		addresses = [];
		for address_element in host_element.findall("./address"):
			addrtype = address_element.attrib["addrtype"];
			addr = address_element.attrib["addr"];
			addresses.append(address.Address(addrtype, addr));

		hostname_elements = host_element.findall("./hostnames/hostname");
		first_hostname_element = hostname_elements[0];
		hostname = first_hostname_element.attrib["name"];

		hosts.append(host.Host(hostname, addresses));

	return hosts;
