# update.py
#
# This script is for updating the .csv files that act as the database.
# 
# We update the regular and post season stats every year. When we update the stats,
# we need to put an ID field in the .csv file with ID values for each player.

from pandas import read_csv

#############################################################################

def get_stats():
    pass

#############################################################################

def add_ids(csv_file):
    df = read_csv(csv_file)
    pass