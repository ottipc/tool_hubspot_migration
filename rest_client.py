#!/usr/bin/env python
import requests
import json
import sys
import os
import config as cfg
class RestClient:

     #url = "https://api.hubapi.com/contacts/v1/"
     #API_KEY = '730c761f-9db5-41c3-a391-b981552855bf'
    # Initializer / Instance Attributes
     def __init__(self, url, API_KEY):
        self.url = url
        self.key = API_KEY

     def make_restclient(url, API_KEY):
        client = RestClient(url, API_KEY)
        client.url = url
        client.key = API_KEY
        #student.major = major
        # Note: I didn't need to create a variable in the class definition before doing this.
        #student.gpa = float(4.0)
        return client
     
     def get_code(self):
        #client = RestClient(url, API_KEY)
        #client.url = url
        #client.key = API_KEY
        print('Get Code ...')
        
        endpoint = "https://app.hubspot.com/oauth/authorize"
        data = {'scope':'contacts','client_id':'{}'.format(cfg.appconfig['client_id']),'redirect_uri':'{}'.format(cfg.appconfig['redirect_uri'])}
        headers = {}
        r = requests.get( url = endpoint, data = data, headers = headers )
        print('Response Get Code .....{}'.format(r.text))
        print(r.text)
        #student.major = major
        # Note: I didn't need to create a variable in the class definition before doing this.
        #student.gpa = float(4.0)
        return r
     
     
     
     def refresh_token(self):
        #client = RestClient(url, API_KEY)
        #client.url = url
        #client.key = API_KEY
        print('Refresh Token ...')
        
        endpoint = "{}token".format(cfg.appconfig['api_oauth_url'])
        data = {'grant_type':'refresh_token','client_id':'{}'.format(cfg.appconfig['client_id']),'client_secret':'{}'.format(cfg.appconfig['client_secret']),'refresh_token':'{}'.format(cfg.appconfig['refresh_token'])}
        headers = {'Content-Type':'application/x-www-form-urlencoded','charset':'utf-8'}
        #print('Endpoint  refresh token ..... : {}'.format(endpoint))
        r = requests.post( url = endpoint, data = data, headers = headers )
        #print('Response fresh token.....{}'.format(r.text))
        resp_dict = json.loads(r.text)
    #    print('ACCESS token.....{}'.format(resp_dict['access_token']))
        return resp_dict['access_token'];
     
     
     
     def get_token(self):
        #client = RestClient(url, API_KEY)
        #client.url = url
        #client.key = API_KEY
        print('Get Token ...')
        
        endpoint = "{}token".format(cfg.appconfig['api_oauth_url'])
        data = {'grant_type':'authorization_code','client_id':'{}'.format(cfg.appconfig['client_id']),'client_secret':'{}'.format(cfg.appconfig['client_secret']),'redirect_uri':'{}'.format(cfg.appconfig['redirect_uri']),'code':'{}'.format(cfg.appconfig['app_auth_code'])}
        headers = {'Content-Type':'application/x-www-form-urlencoded','charset':'utf-8'}
        print('Endpoint  ..... : {}'.format(endpoint))
        r = requests.post( url = endpoint, data = data, headers = headers )
        print('Response .....{}'.format(r.text))
        print(r.text)
        
        #student.major = major
        # Note: I didn't need to create a variable in the class definition before doing this.
        #student.gpa = float(4.0)
        return r
     
     
     
     def create_contact(self, row, access_token):
      try:
        if not row[7]:
            raise Exception("Email is empty, not able to persist in Hubspot")
    
        print("try to persist contact in hubspot : %s" % row[7])
        endpoint = "{}contact/createOrUpdate/email/{}".format(cfg.appconfig['api_url'], row[7])
        #print("Endpoint : {}".format(endpoint))
        headers = {}
        headers["Content-Type"]="application/json"
        headers["Authorization"]="Bearer {}".format(access_token)
        
        data = json.dumps({
  "properties": [
    {
      "property": "email",
      "value": "%s" % row[7]
    },
    {
      "property": "Login",
      "value": "%s" % row[0]
    },
    #{
    #  "property": "Mitglied-Status",
    #  "value": " %s " % row[1]
    #},
    {
      "property": "firstname",
      "value": "%s" % row[2]
    },
    {
      "property": "lastname",
      "value": "%s" % row[3]
    },
    {
      "property": "website",
      "value": "http://hubspot.com"
    },
    {
      "property": "company",
      "value": "HubSpot"
    },
    {
      "property": "phone",
      "value": "%s" % row[3]
    },
    {
      "property": "mobilephone",
      "value": "%s" % row[5]
    },
    {
      "property": "mg_nr",
      "value": "%s" % row[8]
    },
    {
      "property": "address",
      "value": "%s" % row[11]
    },
    {
      "property": "date_of_birth",
      "value": "%s" % row[12]
    },
    {
      "property": "Mehrwertsteuer",
      "value": "%s" % row[13]
    },
    {
      "property": "Kontoinhaber",
      "value": "%s" % row[14]
    },
    {
      "property": "Kontonummer",
      "value": "%s" % row[15]
    },
    {
      "property": "Bankleitzahl",
      "value": "%s" % row[16]
    },
    {
      "property": "name_der_bank",
      "value": "%s" % row[17]
    },
    {
      "property": "IBAN",
      "value": "%s" % row[18]
    },
    {
      "property": "BIC",
      "value": "%s" % row[19]
    },
    {
      "property": "sepa_mandat_vom",
      "value": "%s" % row[20]
    },
    {
      "property": "sepa_referenz",
      "value": "%s" % row[21]
    },
    {
      "property": "city",
      "value": "%s" % row[10]
    },
    {
      "property": "fax",
      "value": "%s" % row[6]
    },
    {
      "property": "state",
      "value": "MA"
    },
    {
      "property": "datum_der_letzten_Buchung",
      "value": "%s" % row[22]
    },
    {
      "property": "wert_der_letzten_Buchung",
      "value": "%s" % row[23]
    },
    {
      "property": "zip",
      "value": "%s" % row[9]
    },
    {
      "property": "kontaktkategorie",
      "value": "%s" % row[24]
    }
  ]
})      
        #print("Setting Call...")
        r = requests.post( url = endpoint, data = data, headers = headers )
        #print(r.text)
        print(r.status_code)
        if r.status_code==404:
            raise Exception("Api URL not available : " . endpoint)
        if r.status_code!=200:
            raise Exception(r.text)
      except Exception as e:
        raise e
        
     def findCSV(self):
        file_names = []
        csvdir = cfg.appconfig['csvdirectory']
        for file in os.listdir(csvdir):
            if file.endswith(".csv"):
                file_names.append(os.path.join(csvdir, file))
                print(os.path.join(csvdir, file))
        return file_names
        
     def sendMailCorrect(self, csvfile):
        sendmail_location = "/usr/sbin/sendmail" # sendmail location
        p = os.popen("%s -t" % sendmail_location, "w")
        p.write("From: %s\n" % cfg.appconfig['email_from'])
        p.write("To: %s\n" % cfg.appconfig['email_to'])
        p.write("Subject: CSV imported correctly\n")
        p.write("\n") # blank line separating headers from body
        p.write("File imported correctly to Hubspot and moved to processed: {} ".format(csvfile))
        status = p.close()
        if status != 0:
              print("Sendmail exit status", status)
              
     def sendMailError(self, csvfile, etext):
        sendmail_location = "/usr/sbin/sendmail" # sendmail location
        p = os.popen("%s -t" % sendmail_location, "w")
        p.write("From: %s\n" % cfg.appconfig['email_from'])
        p.write("To: %s\n" % cfg.appconfig['email_to'])
        p.write("Subject: ERROR importing CSV !\n")
        p.write("\n") # blank line separating headers from body
        p.write("\nFile NOT imported correctly to Hubspot and moved to erroprocessed: {} ".format(csvfile))
        p.write("\n\nError: {}".format(etext))
        status = p.close()
        if status != 0:
              print("Sendmail exit status", status)