# COMP90024-S1-2021-A2
COMP90024 Cloud &amp; Cluster Computing, Semester 1 2021, Assignment 2

Team members:
- Snabhiraja
- Kenneth 
- Ryan Chow
- Yajing Zhang
- Nicholas Wong

<b>IMPORTANT:</b>
- Duplicate "auth_default.cfg" file and fill in the relevant API keys and tokens. Rename the file as "auth.cfg".
- To run playbook: ./run-nectar.sh &lt;MRC email&gt;
- Note: Twitter API developer account should have at least standard v1.1 access.


<b>Access 3-Nodes CouchDB</b>
- Access via Fauxton GUI interface [([Connect to Cisco Anyconnect)](https://studentit.unimelb.edu.au/wireless-vpn/vpn)
>http://172.26.129.212:5984/_utils<br/>
>username: admin 
password:1234

- Access via Command Line Tool(The curl utility)
>Example import request
curl -H "Content-Type: application/json" --data-binary @/home/xxx/data.json https://usr:pwd@host:5984/someDatabase/_bulk_docs/
>Example get request
`shell> curl http://admin:password@127.0.0.1:5984`<br/>
`shell> curl http://admin:1234d@172.26.129.212:5984/`<br/>
[check here for more commands](https://docs.couchdb.org/en/stable/intro/curl.html)

