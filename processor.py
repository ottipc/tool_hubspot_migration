import csv, sys
import rest_client
import os
import config as cfg
client = rest_client.RestClient("","")
files = client.findCSV()
print(cfg.appconfig['api_url'])
access_token = client.refresh_token()

#client.get_token()
for csvfile in files:
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        try:
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    var = "Column names are {}".format(row)
                    print(var)
                    line_count += 1
                else:
                    #print("\t{0} data in the {1} department, and was born in {2}".format(row[0],row[1],row[2]))
                    client.create_contact(row, access_token)  
                    #print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        print('Processed {} lines.'.format(line_count))
# move file to processed
#os.rename(csvfile, "./csvfiles/processed/{}".format(os.path.basename(csvfile)))    
    