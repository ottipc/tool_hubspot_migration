import requests
import json


class RestClient:

     columnLoginName = "Login" #0
     columnMitgliedstatusName = "Mitglied-Status" #1
     columnVornameName = "Vorname" #2
     columnFamiliennameName = "Familienname" #3
     columnTelefonName = "Telefon" #4
     columnMobilName = "Mobil" #5
     columnFaxName = "Fax" #6
     columnEmailName = "E-Mail" #7
     columnMgNrName = "Mg.Nr" #8
     columnPLZName = "PLZ" #9
     columnOrtName = "Ort" #10
     columnAnschriftName = "Anschrift" #11
     columnGeburtstagName = "Geburtstag" #12
     columnMehrwertsteuerName = "Mehrwertsteuer" #13
     columnKontoinhaberName = "Kontoinhaber" #14
     columnKontonummerName = "Kontonummer" #15
     columnBankleitzahlName = "Bankleitzahl" #16
     columnBankName = "Name der Bank" #17
     columnIBANName = "IBAN" #18
     columnBICName = " BIC" #19
     columnSEPAMName = "SEPA Mandat vom" #20
     columnSEPARName = "SEPA Referenz" #21
     url = "https://api.hubapi.com/contacts/v1/"
     API_KEY = '730c761f-9db5-41c3-a391-b981552855bf'
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
        print("try t persist contact in hubspot : {}".format(row[7]))
        endpoint = "https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/{}/?hapikey=730c761f-9db5-41c3-a391-b981552855bf".format(row[7])
        headers = {}
        headers["Content-Type"]="application/json"
        
        data = json.dumps({
  "properties": [
    {
      "property": "email",
      "value": "test@test.de"
    },
    {
      "property": "firstname",
      "value": " %s " % row[2]
    },
    {
      "property": "lastname",
      "value": " %s " % row[3]
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
      "value": " %s " % row[3]
    },
    {
      "property": "address",
      "value": " %s " % row[11]
    },
    {
      "property": "city",
      "value": " %s " % row[10]
    },
    {
      "property": "state",
      "value": "MA"
    },
    {
      "property": "zip",
      "value": " %s " % row[9]
    }
  ]
})  
        r = requests.post( url = endpoint, data = data, headers = headers )
        print(r.text)