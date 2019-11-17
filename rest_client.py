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
     def create_contact(self, row):
      try:
        print("try to persist contact in hubspot : {}".format(row[7]))
        endpoint = "{}contact/createOrUpdate/email/{}/?hapikey={}".format(cfg.appconfig['api_url'], row[7], cfg.appconfig['api_key'])
        print("Endpoint : {}".format(endpoint))
        headers = {}
        headers["Content-Type"]="application/json"
        
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
        print("Setting Call...")
        r = requests.post( url = endpoint, data = data, headers = headers )
        print(r.text)
        #self.sendMail()
      except Exception as e:
         #e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % str(e) )
        
        
     def findCSV(self):
        file_names = []
        for file in os.listdir("./csvfiles"):
            if file.endswith(".csv"):
                file_names.append(os.path.join("./csvfiles", file))
                print(os.path.join("./csvfiles", file))
        return file_names
        
     def sendMail(self):
        sendmail_location = "/usr/sbin/sendmail" # sendmail location
        p = os.popen("%s -t" % sendmail_location, "w")
        p.write("From: %s\n" % "from@somewhere.com")
        p.write("To: %s\n" % "otti@petitcode.com")
        p.write("Subject: thesubject\n")
        p.write("\n") # blank line separating headers from body
        p.write("body of the mail")
        status = p.close()
        if status != 0:
              print("Sendmail exit status", status)
   