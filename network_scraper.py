#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Purpose: DATA419 Project 2021
    Title: Can we use network structures to predict the growth of communities?
    Source: https://github.com/krransby/DATA419_project
"""

__author__ = "Kayle Ransby - 34043590"
__credits__ = ["Kayle Ransby", "Shuzhen Heng", "Zhihao Song", "Hui Chen", "Giulio Dalla Riva"]
__version__ = "1.1.2"
__license__ = "???"


# Imports

from copy import deepcopy
import datetime
import twint
import nest_asyncio


# 'Globals'

SEARCH = [
    "nzpol", "NZParliament", "JudithCollinsMP", "johnkeypm", "winstonpeters",
    "RusselNorman", "jacindaardern", "patrickgowernz", "dbseymour", "ardern", 
    "collins", "NZNationalParty", "nzlabour", "top_nz", "NZFirst", "Maori Party"
          ]

# year, month, day
END_DATE = datetime.datetime(2020, 12, 31)
WEEKS = 52

# directory the .csv files will be placed in
OUTDIR = "Tweet file"

# lat,long,radius: see here https://www.calcmaps.com/map-radius/
NZ = "-41.2728,173.2995,800km"              # NZ
NZAU = "-25.541822,146.437553,3361.56km"    # NZAU

# Fields to be written to the .csv file
CSV_FORMAT = ["id", "conversation_id", "date", "user_id", "username", "mentions", "hashtags", "replies_count", "retweets_count", "likes_count", "tweet", "urls"]


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
    c.Geo = NZ                     # Uncomment this line to restrict search to NZ
    c.Custom["tweet"] = CSV_FORMAT
    c.Since = str(date_start)
    c.Until = str(date_end)
    c.Store_csv = True
    c.Hide_output = True
    c.Search = term
    c.Output = OUTDIR
    
    return c


def retrieve_csv():
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
    date_end = END_DATE
    date_start = date_end - datetime.timedelta(days=7)
    
    num_weeks = deepcopy(WEEKS)
    
    print("Begin tweet scraping ...")
    
    while num_weeks > 0:
        for term in SEARCH:
            
            print("Scraping date range", str(num_weeks) + ":", str(date_start), "-", str(date_end) + ".")
            
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
    
    print(len(seen), "unique tweets found.")


def identify_week():
    """
    Function to add the 'week' of the given tweet to the .csv file

    Returns
    -------
    None.

    """
       
    with open(OUTDIR + '/tweets_cleaned.csv', 'r', encoding="utf8") as in_file, open(OUTDIR + '/tweets_cleaned_week.csv', 'w', encoding="utf8") as out_file:
        
        header = in_file.readline().strip().split(',') # skip the first line
        
        header.append("week\n")
        
        out_file.write(','.join(header))
        
        for line in in_file:
            
            line_list = line.split(',')
            
            if len(line_list) == len(CSV_FORMAT): # only write lines that have all variables
            
                line_date = line_list[CSV_FORMAT.index('date')]
                
                tweet_date = datetime.datetime.strptime(line_date, "%Y-%m-%d")
                
                week = deepcopy(WEEKS)
                date_end = END_DATE
                date_start = date_end - datetime.timedelta(days=7)
                
                while week > 0:
                    
                    if date_start < tweet_date <= date_end:
                        line = line.strip()
                        line += ',{}\n'.format(week)                    
                        out_file.write(line)
                        break
                    else:
                        # Move back one week
                        date_start -= datetime.timedelta(days=7)
                        date_end -= datetime.timedelta(days=7)
                        week -= 1


def main():
    """
    Main execution function.

    Returns
    -------
    None.

    """
    
    # Get tweet data
    retrieve_csv()
    
    # Clean tweet data
    clean_csv()
    
    # Add the week tweets were posted to new .csv file
    identify_week()
    

if __name__ == '__main__':
    # fix "RuntimeError: This event loop is already running"
    nest_asyncio.apply()
    main()
