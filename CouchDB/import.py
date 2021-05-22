import json
import couchdb

# Connect to CouchDB
user = "admin"
password = "1234"
couchserver = couchdb.Server("http://%s:%s@172.26.129.212:5984/" % (user, password))
dbname = "twitter"

# Create a new database if not existed
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

# Open file
file1 = open('TweetSearch.txt', 'r')

# Import each line of file to couchdb/twitter
for line in file1:
    doc = json.loads(line)
    doc["_id"] = str(doc["id"])
    del doc["id"]
    db.update([doc])

