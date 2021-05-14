#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Purpose: DATA419 Project 2021
    Title: Can we use network structures to predict the growth of communities?
    Source: https://github.com/krransby/DATA419_project
"""

__author__ = "Kayle Ransby - 34043590"
__credits__ = ["Kayle Ransby", "Shuzhen Heng", "Zhihao Song", "Hui Chen", "Giulio Dalla Riva"]
__version__ = "1.0.1"
__license__ = "???"


# Imports

import datetime
import twint
import nest_asyncio


# 'Globals'

SEARCH = ["Bitcoin", "Blockchain", "Crypto", "Ethereum", "Dogecoin", "cryptocurrency", "cryptonews", "cryptoexchange", "cryptoinvesting"]
WEEKS = 1
OUTDIR = "Tweet file"


def config(date_start, date_end, term):
    """
    Function to generate configuration for twint searches.

    Parameters
    ----------
    date_start : datetime.date
        Date to start search at.
    date_end : datetime.date
        Date to end search at.
    term : string
        The search term for twint to use.

    Returns
    -------
    c : twint.Config()
        twint configuration to be used by twint.run.search().

    """
    
    # Configure
    c = twint.Config()
    c.Geo = "-41.2728,173.2995,800km" # lat,long,radius: see here https://www.calcmaps.com/map-radius/
    c.Custom["tweet"] = ["id", "conversation_id", "date", "user_id", "username", "mentions", "hashtags"]
    c.Since = str(date_start)
    c.Until = str(date_end)
    c.Store_csv = True
    c.Hide_output = True
    c.Search = term
    c.Output = OUTDIR
    
    return c


def retrieve_csv(num_weeks):
    """
    Generates a .csv file containing tweet data to be used for network construction.

    Parameters
    ----------
    num_weeks : int
        Number of weeks to search tweets (from today back).

    Returns
    -------
    None.

    """
    
    # Initial start and end date range
    date_end = datetime.date.today()
    date_start = date_end - datetime.timedelta(days=7)
    
    print("Begin tweet scraping ...")
    
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
    
    print("Tweet scraping complete.\n")


def clean_csv():
    """
    Function to clear duplicates from the output .csv file.

    Returns
    -------
    None.

    """
    
    print("Removing duplicate entries ...")
    
    with open(OUTDIR + '/tweets.csv', 'r', encoding="utf8") as in_file, open(OUTDIR + '/tweets_cleaned.csv', 'w', encoding="utf8") as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen: continue # skip duplicate
    
            seen.add(line)
            out_file.write(line)
    
    print("Duplicate entries removed.\n")


def main():
    """
    Main execution function.

    Returns
    -------
    None.

    """
    
    # Get tweet data
    retrieve_csv(WEEKS)
    
    # Clean tweet data
    clean_csv()
    


if __name__ == '__main__':
    # fix "RuntimeError: This event loop is already running"
    nest_asyncio.apply()
    main()
