import json

from read_Iptables import *
from api import get_IPzones, get_Services, get_interfaces
from api import latest_IP, latest_Service, latest_Interface, post_Services, post_IPzones, post_Services, post_Interfaces, post_firewallPolicy
from kpc import create_IPzone, create_networkService, create_networkInterface
from kpc import existing_IPzone, existing_service, existing_interfaces
from create_policy import create_Policy

# Get Iptables
mylist_input_final, mylist_output_final 

existing_IP = existing_IPzone(get_IPzones())
existing_Service = existing_service(get_Services())
existing_Interfaces = existing_interfaces(get_interfaces())
print existing_Service
print"++++++++++++++++++++++++++++++++++++"

latest_IP = latest_IP()
latest_Service = latest_Service()
latest_Interface = latest_Interface()

#from get_info
print latest_Service
print latest_IP
print "+++++++++++++++"
for k,v in latest_IP:
    print k + "and" + v


zones = create_IPzone(mylist_input_final, mylist_output_final, existing_IP)
services = create_networkService(mylist_input_final,mylist_output_final,existing_Service)
interfaces = create_networkInterface(mylist_input_final,mylist_output_final,existing_Interfaces)
policies = create_Policy(mylist_input_final, mylist_output_final, latest_IP, latest_Service, latest_Interface)
print json.dumps(policies, indent = 4 )

print zones

    
post_IPzones(zones)
post_Interfaces(interfaces)
post_Services(services)

post_firewallPolicy(policies)