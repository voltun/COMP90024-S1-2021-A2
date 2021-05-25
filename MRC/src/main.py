from _settings import CFG_FILENAME
import configparser, os
import aurin_handler

TEST_RECORDS = 5000
TEST_IDENTI = "aurin:datasource-AU_Govt_ABS_Census-UoM_AURIN_DB_2_lga_i16_lbr_frc_sts_age_sx_abr_trs_str_isl_pers_census_2016"


def main():
    
    # Initialize everything
    config = initConfig()
    aurin = aurin_handler.AurinHandler(config)
    # aurin.queryDatasetTitle(TEST_RECORDS)
    # aurin.getCapabilities()
    aurin.queryFeatureType(TEST_IDENTI)
    aurin.queryDataset(TEST_IDENTI)
    




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