import csv
import os
import requests

CSV_URL ='https://github.com/abhinav97rai/Passwort-Vault/raw/master/keygenerator.csv'
CSV_URL1 ='https://github.com/abhinav97rai/Passwort-Vault/raw/master/encryption.csv'
CSV_URL2 ='https://github.com/abhinav97rai/Passwort-Vault/raw/master/decryption.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)
    download1 = s.get(CSV_URL1)
    download2 = s.get(CSV_URL2)
    decoded_content = download.content.decode('utf-8')
    decoded_content1 = download1.content.decode('utf-8')
    decoded_content2 = download2.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    output_file='keygenerator.py'
    with open(output_file, 'w') as f:
        for row in my_list:
            f.write(row[0])
            f.write("\n")

    cr1 = csv.reader(decoded_content1.splitlines(), delimiter=',')
    my_list1 = list(cr1)
    output_file1='encryption.py'
    with open(output_file1, 'w') as f:
        for row1 in my_list1:
            f.write(row1[0])
            f.write("\n")

    cr2 = csv.reader(decoded_content2.splitlines(), delimiter=',')
    my_list2 = list(cr2)
    output_file2='decryption.py'
    with open(output_file2, 'w') as f:
        for row2 in my_list2:
            f.write(row2[0])
            f.write("\n")
import decryption
os.remove(output_file)
os.remove(output_file1)
os.remove(output_file2)
