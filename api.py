#!/usr/bin/env python
import json, base64, requests, urllib, sys, argparse, httplib, collections
       
# Please edit below.  You can find these information from HALO "[Site Administration] -> [API Keys]" page
api_key_id = "313f442e"
api_secret_key = "4cbe23f66822b8bbc9957705e3399198"

host = 'api.cloudpassage.com'

# get the access token used for the API calls 
connection = httplib.HTTPSConnection(host)
authstring = "Basic " + base64.b64encode(api_key_id + ":" + api_secret_key)
header = {"Authorization": authstring}
params = urllib.urlencode({'grant_type': 'client_credentials'})
connection.request("POST", '/oauth/access_token', params, header)
response = connection.getresponse()
jsondata =  response.read().decode()
data = json.loads(jsondata)
key = data['access_token']

tokenheader = {"Authorization": 'Bearer ' + key, "Content-type": "application/json"}

connection.close()

################################ API GET Calls ######################################################

def latest_IP():
    connection.request("GET", "/v1/firewall_zones",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    Latest_IPdata =json.loads(jsondata)
    
    latest_IP =[]
    for entry in Latest_IPdata['firewall_zones']:
        latest_IP.append((entry['name'], entry['id']))
    return latest_IP
    
def latest_Service():
    connection.request("GET", "/v1/firewall_services",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    Latest_Service_data = json.loads(jsondata)
    
    Service = []
    for entry in Latest_Service_data['firewall_services']:
        Service.append((entry['protocol'],entry['port'], entry['id']))
    
    latest_Service = []
    for line in Service:
        line = list(line)
        if line[1] == None:
            line[1] = '0'
        name = line[0] +"/" + line[1]
        latest_Service.append((name, line[2]))
    return latest_Service

def latest_Interface():
    connection.request("GET", "/v1/firewall_interfaces",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    Latest_Interface =json.loads(jsondata)
    
    latest_Interface =[]
    for entry in Latest_Interface['firewall_interfaces']:
        latest_Interface.append((entry['name'], entry['id']))
    return latest_Interface

def get_IPzones():
    connection.request("GET", "/v1/firewall_zones",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    IPdata = json.loads(jsondata)
    return IPdata 
    
def get_Services():
    connection.request("GET", "/v1/firewall_services",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    Servicedata = json.loads(jsondata)
    return Servicedata
    
def get_interfaces():
    connection.request("GET", "/v1/firewall_interfaces",'',tokenheader)
    response = connection.getresponse()
    jsondata =  response.read().decode()
    Interfacesdata = json.loads(jsondata)
    return Interfacesdata

###############################  API PUT Calls  #################################################

def post_IPzones(reqbody):
    connection.request("POST", "/v1/firewall_zones",json.dumps(reqbody),tokenheader)
    print json.dumps(reqbody, indent=2)
    response = connection.getresponse()
    respbody =  response.read().decode()
    connection.close()

def post_Services(reqbody):
    for i in reqbody:
        print i
        service ={'firewall_service': i }
        print service
        connection.request("POST", "/v1/firewall_services",json.dumps(service),tokenheader)
        response = connection.getresponse()
        respbody =  response.read().decode('ascii', 'ignore')
    connection.close()

def post_Interfaces(reqbody):
    connection.request("POST", "/v1/firewall_interfaces",json.dumps(reqbody),tokenheader)
    response = connection.getresponse()
    respbody =  response.read().decode('ascii', 'ignore')
    connection.close()

def post_firewallPolicy(reqbody):
    print "API"
    print json.dumps(reqbody, indent =2)
    connection.request("POST", "/v1/firewall_policies",json.dumps(reqbody),tokenheader)
    response = connection.getresponse()
    respbody =  response.read().decode('ascii', 'ignore')
    connection.close()
        
