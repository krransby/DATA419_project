#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Purpose: DATA419 Project 2021
    Title: Can we use network structures to predict the growth of communities?
    Source: https://github.com/krransby/DATA419_project
"""

__author__ = "Kayle Ransby - 34043590"
__credits__ = ["Kayle Ransby", "Shuzhen Heng", "Zhihao Song", "Hui Chen", "Giulio Dalla Riva"]
__version__ = "1.0.0"
__license__ = "???"


# Imports

import datetime
import twint
import nest_asyncio


# 'Globals'

SEARCH = ["Bitcoin", "Blockchain", "Crypto", "Ethereum", "Dogecoin", "cryptocurrency", "cryptonews", "cryptoexchange", "cryptoinvesting"]


def config(date_start, date_end, term):
    
    # Configure
    c = twint.Config()
    c.Geo = "-41.2728,173.2995,800km" # lat,long,radius: see here https://www.calcmaps.com/map-radius/
    c.Custom["tweet"] = ["id", "conversation_id", "date", "user_id", "username", "mentions", "hashtags"]
    c.Since = str(date_start)
    c.Until = str(date_end)
    c.Store_csv = True
    c.Search = term
    c.Output = "Tweet file"
    
    return c


def main():
      
    # Initial start and end date range
    date_end = datetime.date.today()
    date_start = date_end - datetime.timedelta(days=7)
    
    # Number of weeks to search within
    num_weeks = 26
    
    while num_weeks > 0:
        for term in SEARCH:
            
            # Get config
            c = config(date_start, date_end, term)
            
            # Run twint search
            twint.run.Search(c)
            
        # Move back one week
        date_start -= datetime.timedelta(days=7)
        date_end -= datetime.timedelta(days=7)
        
        num_weeks -= 1


if __name__ == '__main__':
    # fix "RuntimeError: This event loop is already running"
    nest_asyncio.apply()
    main()