#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import config

if __name__ == '__main__':
    p = argparse.ArgumentParser("Twitter ML")
    p.add_argument("KW",default="escuelas",
            action="store", dest="host",
            help="keywords to search")
    p.add_argument("-v", "--verbose",
            action="store_true", dest="verbose",
            help="Verbose mode [Off]")

    service = build("customsearch", "v1",
             developerKey=config.developerKey)

    res = service.cse().list(
             q=args.keywords
            ).execute()
