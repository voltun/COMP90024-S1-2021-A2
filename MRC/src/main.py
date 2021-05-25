from _settings import CFG_FILENAME, AURIN_DATA_FILE, AURIN_PROCESSED
import configparser, os
import aurin_handler
import os.path
from twitterSearch import twitterSearch
from twitterStream import *
from uploadToDB import uploadToDB
from aurin_data_process import aurin_raw_to_stats

TEST_RECORDS = 5000
TEST_IDENTI = "aurin:datasource-AU_Govt_ABS_Census-UoM_AURIN_DB_2_lga_i16_lbr_frc_sts_age_sx_abr_trs_str_isl_pers_census_2016"

def main():
    
    # Initialize everything
    config = initConfig()
    aurin = aurin_handler.AurinHandler(config)

    # Harvest data from AURIN if the data does not exist
    if not os.path.exists(AURIN_DATA_FILE):
        aurin.queryDataset(TEST_IDENTI)
        aurin_raw_to_stats(AURIN_DATA_FILE)
        uploadToDB(AURIN_PROCESSED, "aurindata")
        
    # Harvest tweets from Twitter via Searching and Streaming
    twitterSearch(config)
    twitterStream(config)
    
    # Upload harvested tweets to CouchDB
    uploadToDB("tweetSearch.txt", "twitterdata")
    uploadToDB("tweetStream.txt", "twitterdata")
    


# Initialize the config file for storing authentication credentials
def initConfig():
    # Obtain full file path
    pardir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(pardir, '../', CFG_FILENAME)

    # Setup configparser to read in authentication credentials
    config = configparser.ConfigParser()
    config.read(filepath)

    return config


if __name__ == "__main__":
    main()
