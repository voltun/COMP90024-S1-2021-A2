# COMP90024-S1-2021-A2
COMP90024 Cloud &amp; Cluster Computing, Semester 1 2021, Assignment 2

Team members:
- Sanmathi Kumar Nabhiraja
- Kenneth Godwin Zhang
- Ryan Chow
- Yajing Zhang
- Nicholas Wong

<b>IMPORTANT:</b>
- Deployment and operations must be performed while connected to University of Melbourne Cisco VPN.
- Duplicate "auth_default.cfg" file and fill in the relevant API keys and tokens. Rename the file as "auth.cfg".
- To run playbook: ./run-nectar.sh &lt;MRC email&gt;
- Note: Twitter API developer account should have at least standard v1.1 access.

<b>Deploy system</b>
- Ensure your working directory is /Ansible/
- Run the following command to start Ansible deployment:
`./run-nectar.sh <MRC registered email>`
- Enter your MRC password when prompted.
- Enter your sudo password when prompted.

<b>Access 3-Nodes CouchDB</b>
- Access via Fauxton GUI interface [([Connect to Cisco Anyconnect)](https://studentit.unimelb.edu.au/wireless-vpn/vpn)
>http://172.26.129.212:5984/_utils<br/>
>username: admin 
password:1234

- Access via Command Line Tool(The curl utility)
>Example import request<br/>
`curl -H "Content-Type: application/json" --data-binary @/home/xxx/data.json https://usr:pwd@host:5984/someDatabase/_bulk_docs/`<br/>
>Example get request<br/>
`shell> curl http://<username>:<password>@127.0.0.1:5984`<br/>
`shell> curl http://<username>:<password>@172.26.129.212:5984/`<br/>
[check here for more commands](https://docs.couchdb.org/en/stable/intro/curl.html)

