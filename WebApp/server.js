

// Import dependencies and create a new express application named 'app'
const express = require('express')
    , db    = require('nano')('http://admin:1234@172.26.129.212:5984/my_couch')
    , app     = express()
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
app.use('/api/v1/', api);


// This middleware informs the express application to serve our compiled React files
if (process.env.NODE_ENV === 'production' || process.env.NODE_ENV === 'staging') {
    app.use(express.static(path.join(__dirname, 'client/build')));

    app.get('*', function (req, res) {
        res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
    });
};




app.get("/db", function(request,response) {
    db.get("foo", function (error, body, headers) {
        if(error) { return response.status(error['status-code']||500).send(error.message); }
        response.status(200).send(body);
        console.log(body);
        // response.json(body);
    });

});


app.get("/api", (req, res) => {
    res.json({ message111: "Hello from server!" });
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





