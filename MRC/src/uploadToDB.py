import json,couchdb, requests

def uploadToDB(uploadFile, dbname):
    user = "admin"
    password = "1234"
    couchserver = couchdb.Server("http://%s:%s@172.26.129.212:5984/" % (user, password))
    
    # Create a new database if not existed
    if dbname in couchserver:
        db = couchserver[dbname]
    else:
        db = couchserver.create(dbname)

    # SEND AURIN DATA
    if dbname == "aurindata":
        headers = {
            'Content-type': 'application/json',
        }

        data = open(uploadFile)
        post_url = 'http://admin:1234@172.26.129.212:5984/aurin_test/_bulk_docs'

        response = requests.post(post_url, headers=headers, data=data)
        print(response)
        return

    # Open file
    file1 = open(uploadFile, 'r')
    # Import each line of file to couchdb/twitter
    for line in file1:
        doc = json.loads(line)
        doc["_id"] = str(doc["id"])
        del doc["id"]
        db.update([doc])
