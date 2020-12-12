# import csv
# import pandas as pd

# first_df = pd.read_csv('extracted_geoinfo.csv')
# # print(first_df.columns)
# first_df.drop(columns=['crawl_result'],inplace=True)
# # print(first_df.columns)
# first_df.to_csv('1207_info.csv')

import csv
import sqlite3

def dataImport(csvpath, dbpath, tablename):
    reader = csv.DictReader(open(csvpath, '/Users/hazel_lin/Documents/GitHub/Bars-in-Taipei/1207_info.csv'), delimeter=',',quoting=csv.QUOTE_MINIMAL)
    conn = sqlite3.connect(dbpath)
    # fix error with non-ASCII input
    conn.text_factory = str
    c = conn.cursor()
    create_query = 'CREATE TABLE '+ tablename +'(name TEXT NOT NULL,rating FLOAT NOT NULL,address TEXT NOT NULL, ave_price FLOAT NOT NULL, url TEXT NOT NULL, tel TEXT NOT NULL, lat_lng TEXT NOT NULL, place_id TEXT UNIQUE)'
    c.execute(create_query)
    for row in reader:
        print (row)
        to_db = [row['name'],row['rating'],row['address'],row['ave_price'],row['url'],row['tel'],row['lat_lng'],row['place_id']]
        c.execute('INSERT INTO '+geoinfo+'(name, rating, address, ave_price, url, tel, lat_lng, place_id')
    conn.commit()
print('Done')