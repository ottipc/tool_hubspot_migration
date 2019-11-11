import csv, sys
import rest_client
filename = 'test_hubspot.csv'
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    try:
        client = rest_client.RestClient("","")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                var = "Column names are {}".format(row)
                print(var)
                line_count += 1
            else:
                #print("\t{0} data in the {1} department, and was born in {2}".format(row[0],row[1],row[2]))
                client.create_contact(row)            
                #print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    print('Processed {} lines.'.format(line_count))
    
    