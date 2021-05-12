from _settings import CFG_FILENAME
import configparser, os
import aurin_handler

TEST_RECORDS = "5000"

def main():
    
    # Initialize everything
    config = initConfig()
    aurin = aurin_handler.AurinHandler(config)
    aurin.getDatasetTitle(TEST_RECORDS)
    




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