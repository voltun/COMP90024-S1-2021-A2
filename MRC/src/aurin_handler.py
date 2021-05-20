from _settings import CFG_AURIN, AURIN_TITLE_FILE, AURIN_DATA_FILE,\
AURIN_FEATURE_FILE
from lxml import etree
import urllib.request as urllib2

URL_CAPABILITY = 'http://openapi.aurin.org.au/csw?request=GetCapabilities&service=CSW'
URL_TITLE = 'http://openapi.aurin.org.au/csw?request=GetRecords&service=CSW&versi'\
    +'on=2.0.2&typeNames=csw:Record&elementSetName=full&resultType=results&constraintLan'\
    +'guage=CQL_TEXT&constraint_language_version=1.1.0&maxRecords='
URL_DESC_DATASET = "http://openapi.aurin.org.au/wfs?request=DescribeFeatureType&"\
    +"service=WFS&version=1.1.0&typeName="
URL_FETCH_DATA = 'http://openapi.aurin.org.au/wfs?request=GetFeature&service=WFS&'\
    +'version=1.1.0&TypeName='

class AurinHandler:
    """
    Handles all API calls and operations regarding AURIN datasets.

    Adapted from openapi-examples by Robert Hutton 
    <rhutton@unimelb.edu.au>
    Link: https://github.com/AURIN/openapi-examples/tree/master/python
    """

    test_data = ""

    def __init__(self, config):
        self.username = config.get(CFG_AURIN, "username")
        self.password = config.get(CFG_AURIN, "password")


    def __openapi_request(self, url):
        """
        Submit an authenticated request to the AURIN Open API
        """
        # create an authenticated HTTP handler and submit URL
        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(None, url, self.username, \
            self.password)
        auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(auth_manager)
        urllib2.install_opener(opener)

        req = urllib2.Request(url)
        try:
            handler = urllib2.urlopen(req)
        except:
            print("Failed to open HTTP connection to "+url)
            print(req)
            exit(-1)
            
        # print (handler.getcode())
        # print (handler.headers.getheader('content-type'))
            
        return handler.read()


    def queryCapabilities(self):
        """
        Gets all capabilities of AURIN OpenAPI service.
        """

        xml = self.__openapi_request(URL_CAPABILITY)
        root = etree.fromstring(xml)
        print('================ CAPABILITIES ================')
        print(etree.tostring(root, pretty_print=True).decode())


    def queryDatasetTitle(self, max_records:str):
        """
        Gets N number of dataset titles from AURIN. Stores the output onto
        a text file.

        max_records (int) - Maximum number of dataset titles to fetch
        """

        xml = self.__openapi_request(URL_TITLE + str(max_records))
        root = etree.fromstring(xml)
        # print(etree.tostring(root, pretty_print=True).decode())

        # Outputs all datasets onto a file
        with open(AURIN_TITLE_FILE, 'w') as outfile:
            for dataset in root.findall(".//csw:Record", root.nsmap):
                outfile.write(dataset.find(".//dc:title", root.nsmap).text + '\n')
                outfile.write("Identifier:\t" + dataset.find(".//dc:identifier", \
                    root.nsmap).text + "\n\n")
                # print('Dataset: '+dataset.find(".//dc:title", root.nsmap).text)
                # print(dataset.find(".//dc:rights", root.nsmap).text)
            print("All available AURIN datasets written to " + AURIN_TITLE_FILE)
    

    def queryFeatureType(self, dataset):
        """
        Query the headers of the dataset then prints it out.

        dataset (str) - dataset identifier or non-space string of dataset name
        """
        
        url = URL_DESC_DATASET + dataset
        print('================ DATASET PROPERTIES ================')
        print('Query URL: '+url)
        xml = self.__openapi_request(url)
        root = etree.fromstring(xml)
        # print(etree.tostring(root, pretty_print=True).decode())

        # Write dataset output to specified file
        with open(AURIN_FEATURE_FILE, 'w') as outfile:
            outfile.write(etree.tostring(root, pretty_print=True).decode())
                # print('Dataset: '+dataset.find(".//dc:title", root.nsmap).text)
                # print(dataset.find(".//dc:rights", root.nsmap).text)
            print("Dataset properties written to " + AURIN_FEATURE_FILE)


    def queryDataset(self, dataset:str, max_rows=None):
        """
        Fetches data instances of given dataset from AURIN API. If
        max_rows is not specified, fetches the entire entry by default.

        Writes output to a specified txt file. 

        dataset (str) - dataset identifier or non-space string of dataset name.
        max_rows (int) - DEFAULT=None; If specified, fetches max_rows \
            number of rows. Must be > 0.
        """
        if max_rows is None:
            url = URL_FETCH_DATA + dataset        
        else:
            url = URL_FETCH_DATA + dataset + "&MaxFeatures=" + str(max_rows)
        print('Query URL: '+url)
        xml = self.__openapi_request(url)
        root = etree.fromstring(xml)
        # print(etree.tostring(root, pretty_print=True).decode())

        # Write dataset output to specified file
        with open(AURIN_DATA_FILE, 'w') as outfile:
            outfile.write(etree.tostring(root, pretty_print=True).decode())
                # print('Dataset: '+dataset.find(".//dc:title", root.nsmap).text)
                # print(dataset.find(".//dc:rights", root.nsmap).text)
            print("Rows of data written to " + AURIN_DATA_FILE)

