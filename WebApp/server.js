

// Import dependencies and create a new express application named 'app'
const express = require('express')
    // , db   = require('nano')('http://admin:1234@172.26.129.212:5984/twitterdata')
    , couchdb =require('nano')('http://admin:1234@172.26.129.212:5984')
    , app     = express()
const db = couchdb.use('twitterdata');
const aurin =couchdb.use('aurin')
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

//set backend port to be either an environment variable or port 5000
const PORT = process.env.PORT || 5000;


// This application level middleware prints incoming requests to the servers console, useful to see incoming requests
app.use((req, res, next) => {
    console.log(`Request_Endpoint: ${req.method} ${req.url}`);
    next();
});

// Configure the bodyParser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

// Configure the CORs middleware
app.use(cors());

// Require Route
const api = require('./routes/routes');
// Configure app to use route
// app.use('/api/v1/', api);


// This middleware informs the express application to serve our compiled React files
if (process.env.NODE_ENV === 'production' || process.env.NODE_ENV === 'staging') {
    app.use(express.static(path.join(__dirname, 'client/build')));

    app.get('*', function (req, res) {
        res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
    });
};

/** Get and fetch Pie data **/

const pie = {
    labels: [],
    datasets: [
        {
            label: 'Percentage of Twitters',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',

            ],
            borderWidth: 1,
        },
    ],
};


//Query Top5 cities with most tweets and display in descending order
app.get("/view", (req, res) => {
    db.view('citiestweets', 'cities',{group:true},function(err, body) {
            let keyList=[];
            let valueList=[];
            if (!err) {

                body.rows.sort(function (a, b) {
                    return b.value - a.value;
                });
                // console.log(body.rows.slice(0,5));
                body.rows.slice(0,4).forEach(element=>keyList.push(element.key));
                body.rows.slice(0,4).forEach(element=>valueList.push(parseInt(element.value)));
                pie.labels=keyList;
                pie.datasets[0].data=valueList;
                res.json(pie);
                // res.json({cities:body.rows.slice(0,5)});
            } else {
                console.log(err);
            }
    }

    );


});

/** Get and fetch Pie data regarding to the population **/
const piepopulation = {
    labels: [],
    datasets: [
        {
            label: '# of population',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',

            ],
            borderWidth: 1,
        },
    ],
};
// fetch population of each cities
app.get("/population", (req, res) => {
    aurin.view('population', 'populationview',{keys:['Melbourne','Sydney','Brisbane','Gold Coast']},function(err, body) {
        let citiesName=[];
        let population=[];
        if (!err) {

            body.rows.forEach(function (item, index){
                if(item.key){
                    citiesName.push(item.key);
                    population.push(item.value);
                }

            })

                piepopulation.labels=citiesName;
                piepopulation.datasets[0].data=population;
                res.json(piepopulation);


            } else {
                console.log(err);
            }
        }

    );

});



/** Get and fetch age distribution data **/
const age = {
    labels: [],
    datasets: [
        {
            label: '# of people age between 15-40',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
            ],
            borderWidth: 1,
        },
    ],
};

app.get("/age", (req, res) => {
    aurin.view('population', 'ageview',{keys:['Melbourne','Sydney','Brisbane','Gold Coast']},function(err, body) {
        let citiesName=[];
        let youngpeople=[];
    if(!err){

        body.rows.forEach(function (item, index){
            if(item.key){
                citiesName.push(item.key);
                youngpeople.push(item.value);
            }

        })

        age.labels=citiesName;
        age.datasets[0].data=youngpeople;
        res.json(age);


    } else {
            console.log(err);
        }

        }

    );

});














//query couchdb example
app.get("/db", function(request,response) {
    db.get("foo", function (error, body, headers) {
        if(error) { return response.status(error['status-code']||500).send(error.message); }
        response.status(200).send(body);
        console.log(body);
        // response.json(body);
    });

});

//

//communication with frontend example
app.get("/api", (req, res) => {
    res.json({ message: "Hello from server!" ,key:"value",rows:[1,2,3,4]});
});





// Catch any bad requests
app.get('*', (req, res) => {
    res.status(200).json({
        msg: 'Catch All'
    });
});

app.listen(PORT, () => {
    console.log(`Backend Sever listening on ${PORT}`);
});





