#!/usr/bin/python3
import datetime
import csv
import sys
import rest_client
import os
import config as cfg
client = rest_client.RestClient("", "")
files = client.findCSV()
print(cfg.appconfig['api_url'])
access_token = client.refresh_token()

# client.get_token()
for csvfile in files:
    with open(csvfile) as csv_file:
        processedLines = []
        try:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    var = "Column names are {}".format(row)
                    print(var)
                    line_count += 1
                else:
                    print("Processing Contact...")
                    processed = client.create_contact(row, access_token)
                    processedLines.append(processed)
                    print("Processed :  {} ".format(processed))
                    #print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
        except csv.Error as ce:
            print('Exception importing {} : {} in Line : {}'.format(
                csvfile, str(e), line_count + 1))
            actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
            csvfilename = os.path.basename(csvfile).replace(
                '.csv', '.{}.csv'.format(actual_date))
            # move file to errorprocessed
            os.rename(
                csvfile, "{}errorprocessed/{}".format(cfg.appconfig['csvdirectory'], csvfilename))
            client.sendMailError(csvfilename, "Error at Importing : {} : Line {}".format(
                str(ce), line_count + 1), processedLines)
            print(" CSV Error {} : {} ".format(csvfile, ce.args))
            continue
        except Exception as e:
            print('Exception importing {} : {} in Line : {}'.format(
                csvfile, str(e), line_count + 1))
            actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
            csvfilename = os.path.basename(csvfile).replace(
                '.csv', '.{}.csv'.format(actual_date))
            # move file to errorprocessed
            os.rename(
                csvfile, "{}/errorprocessed/{}".format(cfg.appconfig['csvdirectory'], csvfilename))
            client.sendMailError(csvfilename, "Error at Importing : {} : Line {}".format(
                str(e), line_count + 1), processedLines)
            continue
        print('Processed {} lines.'.format(line_count))
        actual_date = datetime.datetime.now().strftime("%d.%m.%Y%I-%H:%M:%S")
        csvfilename = os.path.basename(csvfile).replace(
            '.csv', '.{}.csv'.format(actual_date))
        # move file to processed
        os.rename(
            csvfile, "{}/processed/{}".format(cfg.appconfig['csvdirectory'], csvfilename))
        client.sendMailCorrect(csvfilename, processedLines)
