// import logo from './logo.svg';
import './css/App.css';
import React, { useState } from 'react';
import CustomMapComponent from "./components/CustomMapComponent";
import HorizontalBarChart from "./components/HorizontalBarChart";
import { fetchFakeBarChartData } from "./api/fetchFakeMapData";
import LineChart from "./components/LineChart";
import {Pie} from 'react-chartjs-2';


function App() {


  // Get the pie data from database regarding to numbers of tweets
  const [tweets, setTweets] = React.useState(null);
  React.useEffect(() => {
    fetch("/view")
        .then((body) => body.json())
        .then((tweets) => setTweets(tweets))

  },[]);



  //Get the pie data regarding to the population
  const [population, setpopulation] = React.useState(null);
  React.useEffect(() => {
    fetch("/population")
        .then((body) => body.json())
        .then((population) => setpopulation(population))

  },[]);

  //Get the age distribution of each cities
  const [age, setage] = React.useState(null);
  React.useEffect(() => {
    fetch("/age")
        .then((body) => body.json())
        .then((age) => setage(age))

  },[]);


  //Get vertical date from database


  let [labels] = useState(['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']);
  let [data, setData] = useState([12, 19, 3, 5, 2, 3]);


  //Get horizontal data
  let { horizontalBarData, optionsLocal } = fetchFakeBarChartData(labels, data);
  let [options, setOptions] = useState({ ...optionsLocal, ...{ indexAxis: "x", plugins: { legend: { position: 'bottom', }, title: { display: true, text: 'Number of people' } } } });
  let [flipOptions] = useState({ ...optionsLocal, ...{ indexAxis: "x", plugins: { legend: { position: 'bottom', }, title: { display: true, text: 'Number of twitters' } } } });
  console.log(tweets)

  return (
      <div className="App">
  <div class="header">
  <h1>COMP90024-S1-2021-A2</h1>
  <h3>Correlating tweets from Australian cities to its demographics </h3>
</div>
      <div className="row">
        <div className="map-div-container box">
          <CustomMapComponent funcToChange={{ "optionsFunc": setOptions, "dataFunc": setTweets,"dataFunc2": setpopulation, "dataFunc3": setage }} changeData={population}/>
        </div>
        <div className="chart-div-container box">
          <HorizontalBarChart data={tweets} options={flipOptions} />
        </div>
      </div>
      <div className="row">
        <div className="chart-div-container box">
          <HorizontalBarChart data={population} options={options} />
        </div>
        <div className="chart-div-container box">
          <LineChart data={age} />
        </div>
      </div>
    </div>
  );
}

export default App;
