from _settings import CFG_FILENAME
import configparser, os
import aurin_handler
from twitterSearch import twitterSearch
from twitterStream import *
from uploadToDB import uploadToDB

TEST_RECORDS = 5000
TEST_IDENTI = "aurin:datasource-AU_Govt_ABS_Census-UoM_AURIN_DB_2_lga_i16_lbr_frc_sts_age_sx_abr_trs_str_isl_pers_census_2016"

# TEST_IDENTI = "VIC"

def main():
    
    # Initialize everything
    config = initConfig()
    aurin = aurin_handler.AurinHandler(config)

    aurin.getDatasetTitle(TEST_RECORDS)
    twitterSearch(config)
    twitterStream(config)
    uploadToDB("tweetSearch.txt")
    uploadToDB("tweetStream.txt")


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
