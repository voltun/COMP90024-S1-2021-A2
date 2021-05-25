**Access via Fauxton GUI interface**
http://172.26.129.212:5984/_utils <br/> username: admin password:1234

**Access via Command Line Tool(The curl utility)**
Example get request
shell> curl http://admin:password@127.0.0.1:5984
shell> curl http://admin:1234d@172.26.129.212:5984/


**Import single doc json file to CouchDB** <br/>
`$curl -X POST -d @melb.json  http://admin:1234@172.26.129.212:5984/geomel/_bulk_docs -H 'Content-Type:application/json'
`
