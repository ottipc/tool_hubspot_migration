import requests
import json
import sys

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
      try:
        print("try t persist contact in hubspot : {}".format(row[7]))
        endpoint = "https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/{}/?hapikey=730c761f-9db5-41c3-a391-b981552855bf".format(row[7])
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
      except Exception as e:
         #e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % str(e) )