// import logo from './logo.svg';
import './css/App.css';
import React, { useState } from 'react';
import CustomMapComponent from "./components/CustomMapComponent";
import HorizontalBarChart from "./components/HorizontalBarChart";
import { fetchFakeBarChartData } from "./api/fetchFakeMapData";
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
  let [options, setOptions] = useState(optionsLocal);
  let [flipOptions] = useState({ ...optionsLocal, ...{ indexAxis: "x", plugins: { legend: { position: 'bottom', }, title: { display: true, text: 'Peolple aged between 18 and 60' } } } });


  return (
      <div className="App">
        <div className="row">
          <div className="chart-div-container box">
            <Pie data={tweets} options={{ maintainAspectRatio: false ,animation:false, }}/>

          </div>
          <div className="chart-div-container box">
            <Pie data={population} options={{ maintainAspectRatio: false ,animation:false, legend: { display: true, position: "right" },datalabels: {
                display: true,
                color: "black",
              }}}/>
          </div>

        </div>


        {/*row 2*/}
        <div className="row">
          <div className="map-div-container box">
            <CustomMapComponent funcToChange={{ "optionsFunc": setOptions, "dataFunc": setData }} />
          </div>
          <div className="chart-div-container box">
            <HorizontalBarChart data={age} options={flipOptions} />
          </div>

        </div>


      </div>
  );
}

export default App;
