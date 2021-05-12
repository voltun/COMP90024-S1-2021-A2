from _settings import CFG_AURIN, AURIN_OUT_FILE
from lxml import etree
import urllib.request as urllib2

URL_CAPABILITY = 'http://openapi.aurin.org.au/csw?request=GetCapabilities&service=CSW'
URL_GETDATASET = 'http://openapi.aurin.org.au/csw?request=GetRecords&service=CSW&versi'\
    +'on=2.0.2&typeNames=csw:Record&elementSetName=full&resultType=results&constraintLan'\
    +'guage=CQL_TEXT&constraint_language_version=1.1.0&maxRecords='
URL_DESC_DATASET = "http://openapi.aurin.org.au/csw?request=DescribeRecord&service=CSW&"\
    + "typeName=\'ABS - Jobs In Australia - All Jobs (GCCSA) 2011-2018\'"


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


    def getCapabilities(self):
        """
        Gets all capabilities of AURIN OpenAPI service.
        """

        xml = self.__openapi_request(URL_CAPABILITY)
        root = etree.fromstring(xml)
        print('================ CAPABILITIES ================')
        # print(etree.tostring(root, pretty_print=True).decode())


    def getDatasetTitle(self, max_records:str):
        """
        Gets N number of dataset titles from AURIN. Stores the output onto
        a text file.

        max_records (int) - Maximum number of dataset titles to fetch
        """

        xml = self.__openapi_request(URL_GETDATASET + max_records)
        root = etree.fromstring(xml)
        # print(etree.tostring(root, pretty_print=True).decode())

        # Outputs all datasets onto a file
        with open(AURIN_OUT_FILE, 'w') as outfile:
            for dataset in root.findall(".//csw:Record", root.nsmap):
                outfile.write(dataset.find(".//dc:title", root.nsmap).text + '\n')
                # print('Dataset: '+dataset.find(".//dc:title", root.nsmap).text)
                # print(dataset.find(".//dc:rights", root.nsmap).text)
            print("All available AURIN datasets written to " + AURIN_OUT_FILE)
    
    def test(self):
        xml = self.__openapi_request(URL_DESC_DATASET)
        root = etree.fromstring(xml)
        print(etree.tostring(root, pretty_print=True).decode())
    # def query(self, dataset):
    #     # Query the attributes of the first dataset
    #     dataset = root.findall(".//dc:title", root.nsmap)[0].text
    #     url = 'http://openapi.aurin.org.au/wfs?request=DescribeFeatureType&service=WFS&version=1.1.0&typeName='+dataset
    #     print('================ DATASET PROPERTIES ================')
    #     print('Query URL: '+url)
    #     xml = openapi_request(url)
    #     root = etree.fromstring(xml)
    #     print(etree.tostring(root, pretty_print=True))

# # Get the first feature (row) of the first dataset
# url = 'http://openapi.aurin.org.au/wfs?request=GetFeature&service=WFS&version=1.1.0&TypeName='+dataset+'&MaxFeatures=1'
# print('================ FIRST FEATURE ================')
# print('Query URL: '+url)
# xml = openapi_request(url)
# root = etree.fromstring(xml)
# print(etree.tostring(root, pretty_print=True))

