#!/usr/bin/python3
import datetime
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
        try:
            csv_reader = csv.reader(csv_file, delimiter=';')
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
        except csv.Error as ce:
            sys.exit('file {}, line {}: {}'.format(csvfile, reader.line_num, ce))
            actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
            csvfilename = os.path.basename(csvfile).replace('.csv','.{}.csv'.format(actual_date))
            os.rename(csvfile, "{}errorprocessed/{}".format(cfg.appconfig['csvdirectory'],csvfilename))    
            # move file to errorprocessed
            client.sendMailError(csvfile);
            print(" CSV Error {} : {} ".format(csvfile, ce.args))
            continue;
        except Exception as e:
            print('Exception importing {} : {}'.format(csvfile, str(e)))
            client.sendMailError(csvfile, str(e));
            # move file to errorprocessed
            actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
            csvfilename = os.path.basename(csvfile).replace('.csv','.{}.csv'.format(actual_date))
            os.rename(csvfile, "{}/errorprocessed/{}".format(cfg.appconfig['csvdirectory'],csvfilename))    
            continue;
        print('Processed {} lines.'.format(line_count))
        client.sendMailCorrect(csvfile);    
        # move file to processed
        actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
        csvfilename = os.path.basename(csvfile).replace('.csv','.{}.csv'.format(actual_date))
        os.rename(csvfile, "{}/processed/{}".format(cfg.appconfig['csvdirectory'],csvfilename))    
