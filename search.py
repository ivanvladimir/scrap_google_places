#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import config
import pprint
from tinydb import TinyDB, Query

from googleplaces import GooglePlaces, types, lang

s2t = {
    "restaurant":types.TYPE_FOOD,    
    "school":types.TYPE_SCHOOL,    
}

lat_lng={
    "lat":19.3794,
    "lng":99.1591
    
}

if __name__ == '__main__':
    p = argparse.ArgumentParser("Search google places")
    p.add_argument("KW", nargs='+',
            action="store",
            help="keywords to search")

    p.add_argument("--location",default="London, England",type=str,
            action="store", dest="location",
            help="Location for search")

    p.add_argument("--dbname",
            default="DB.json", type=str,
            action="store", dest="dbname",
            help="Name for the db file")
    p.add_argument("--type",default="restaurant",type=str,
            action="store", dest="type",
            help="Type of place")
 

    p.add_argument("-v", "--verbose",
            action="store_true", dest="verbose",
            help="Verbose mode [Off]")

    args = p.parse_args()
    google_places = GooglePlaces(config.APIKEY)

    print("Connecting to DB:",args.dbname)
    db = TinyDB(args.dbname)
    places = db.table('places')


    query_result = google_places.text_search(
             query=args.KW,lat_lng=lat_lng,
              language= 'es')
    
    Filter = Query()

    for place in query_result.places:
        # Returned places from a query are place summaries.
        print(place.name)
        print(place.geo_location)
        print(place.place_id)
        place.get_details()
	# Referencing any of the attributes below, prior to making a call to
    	# get_details() will raise a googleplaces.GooglePlacesAttributeError.
        #print(place.details.keys()) # A dict matching the JSON response from Google.
        print(place.formatted_address)
        print(place.local_phone_number)
        print(place.international_phone_number)
        print(place.website)
        print(place.url)
        print(80*"=")

        places_=places.search(Filter.id.search(place.place_id))

        if len(places_)==0:
            places.insert({
                "name":place.name,
                "id":place.place_id,
                    "address":place.formatted_address,
                "phone":place.local_phone_number,
                "website":place.website,
                "url":place.url,
                })

