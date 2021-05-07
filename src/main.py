import configparser

CONFIG_FILENAME = "auth.cfg"

def main():
    print("Testing")
    #Import authentication
    config = configparser.RawConfigParser()
    config.read(CONFIG_FILENAME)

    

if __name__ == "__main__":
    main()