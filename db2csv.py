#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import config
import pprint
import csv
from tinydb import TinyDB, Query


if __name__ == '__main__':
    p = argparse.ArgumentParser("Search google places")
    p.add_argument("--dbname",
            default="DB.json", type=str,
            action="store", dest="dbname",
            help="Name for the db file")

    p.add_argument("--csv",
            default="DB.csv", type=str,
            action="store", dest="csvname",
            help="Name for the csv file")

    p.add_argument("-v", "--verbose",
            action="store_true", dest="verbose",
            help="Verbose mode [Off]")

    args = p.parse_args()

    print("Connecting to DB:",args.dbname)
    db = TinyDB(args.dbname)
    places = db.table('places')


    unique_places=set()
    for place in places.all():
        if len(place['url'].strip())>0:
            unique_places.add(place['url'].strip())

                


    print("Connecting to DB:",args.csvname)
    with open(args.csvname, 'a') as csvfile:
       csvwriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
       for place in places.all():
           if place['url'].strip() in unique_places:
               csvwriter.writerow([place['name'],place['address'],place['website'],place['url'],place['phone']])
               unique_places.remove(place['url'].strip())


   

