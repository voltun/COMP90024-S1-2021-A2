# COMP90024-S1-2021-A2
COMP90024 Cloud &amp; Cluster Computing, Semester 1 2021, Assignment 2

Team members:
- Snabhiraja
- Kenneth 
- Ryan Chow
- Yajing Zhang
- Nicholas Wong


Teams are expected to use:
- a version-control system such as GitHub or Bitbucket for sharing source code.
- MapReduce based implementations for analytics where appropriate, using CouchDB’s built in MapReduce capabilities.
- The entire system should have scripted deployment capabilities. This means that your team will provide a script, which, when executed, will create and deploy one or more virtual machines and orchestrate the set up of all necessary software on said machines (e.g. CouchDB, the twitter harvesters, web servers etc.) to create a ready-to-run system. Note that this setup need not populate the database but demonstrate your ability to orchestrate the necessary software environment on the UniMelb Research Cloud. Teams should use Ansible (http://www.ansible.com/home) for this task.
- Teams may wish to utilise container technologies such as Docker, but this is not mandatory.
- The server side of your analytics web application may expose its data to the client through a ReSTful design. Authentication or authorization is NOT required for the web front end.

Teams are also encouraged to describe:
- How fault-tolerant is your software setup? Is there a single point-of-failure?
- Can your application and infrastructure dynamically scale out to meet demand?


<b>Assignment Description</b>

The software engineering activity builds on the lecture materials describing Cloud systems and
especially the UniMelb Research Cloud and its use of OpenStack; on data from the Twitter APIs, and
CouchDB and the kinds of data analytics (e.g. MapReduce) that CouchDB supports as well as data from
the Australian Urban Research Infrastructure Network (AURIN – https://portal.aurin.org.au). The
focus of this assignment is to harvest tweets from across the cities of Australia on the UniMelb
Research Cloud and undertake a variety of social media data analytics scenarios that tell interesting
stories of life in Australian cities and importantly how the Twitter data can be used
alongside/compared with/augment the data available within the AURIN platform to improve our
knowledge of life in the cities of Australia. Teams can download data from the AURIN platform, e.g. as
JSON, CSV or Shapefiles, or using the AURIN openAPI (https://aurin.org.au/aurin-apis/). This data
can/should be included into the team’s CouchDB database for analysis with Twitter data.

The teams should develop a Cloud-based solution that exploits a multitude of virtual machines (VMs)
across the UniMelb Research Cloud for harvesting tweets through the Twitter APIs (using both the
Streaming and the Search API interfaces). The teams should produce a solution that can be run (in
principle) across any node of the UniMelb Research Cloud to harvest and store tweets and scale
up/down as required. Teams have been allocated 4 servers (instances) with 8 virtual CPUs and 500Gb
of volume storage. All students have access to the UniMelb Research Cloud as individual users and can
test/develop their applications using their own (small) VM instances, e.g. using personal instances
such as pt-1234. (Remembering that there is no persistence in these small, free and dynamically
allocated VMs).

The solution should include a Twitter harvesting application for any/all of the cities of Australia. The
teams are expected to have multiple instances of this application running on the UniMelb Research
Cloud together with an associated CouchDB database containing the amalgamated collection of
Tweets from the harvester applications. The CouchDB setup may be a single node or based on a cluster
setup. The system should be designed so that duplicate tweets will not arise.
Students may want to explore other sources of data they find on the Internet, e.g. information on
weather, sport events, TV shows, visiting celebrities, stock market rise/falls, official statistics on
Covid-19 however these are not compulsory to complete the work. A large corpus of Twitter posts
will be made available for data analytics, but again teams may decide that they only wish to focus on
Twitter data that they collect.

Teams are expected to develop a range of analytic scenarios, e.g. using the MapReduce capabilities
offered by CouchDB for social media analytics and comparing the data with official data from AURIN.
Teams are free to explore any scenarios that connect “in some way” to the AURIN data. Teams are
encouraged to be creative here. A prize will be awarded for the most interesting scenarios identified!
