import React, { useRef, useEffect } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import "../css/map.css";
import fetchFakeMapData from "../api/fetchFakeMapData";

mapboxgl.accessToken = 'pk.eyJ1Ijoibml0aGlua25qYWluIiwiYSI6ImNrb2xjaDlnZTA0NmUyb3F0NWZjZnp0ZzYifQ.TGtgvNrOO3DnuNwmdXeWvA';

export default function CustomMapComponent(props) {
    const mapContainerRef = useRef(null);
    const lng = 135.6387;
    const lat = -25.6170;
    const zoom = 3;
     const [tweets, setTweets] = React.useState(null);
    useEffect(() => {
        const map = new mapboxgl.Map({
            container: mapContainerRef.current,
            // See style options here: https://docs.mapbox.com/api/maps/#styles
            style: "mapbox://styles/mapbox/light-v10",
            center: [lng, lat],
            zoom: zoom
        });


        // add navigation control (zoom buttons)
        map.addControl(new mapboxgl.NavigationControl(), "bottom-right");
        // map.addControl(new mapboxgl.FullscreenControl({container: mapContainerRef.current.querySelector('body')}));

        map.on("load", async (input, init) => {
            // const results = await fetchMapData({ longitude: lng, latitude: lat });
            const results = await fetchFakeMapData({longitude: lng, latitude: lat })
            console.log(results);
            map.addSource("random-points-data", {
                type: "geojson",
                data: results
            });
            map.addSource('urban-areas', {
                'type': 'geojson',
                'data': 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_urban_areas.geojson'
            });


            map.addLayer({
                'id': 'random-points-data',
                'type': 'symbol',
                'source': 'random-points-data',
                'layout': {
                    'icon-image': '{icon}',
                    'icon-allow-overlap': false
                }
            });


            map.addLayer(
                {
                    'id': 'urban-areas-fill',
                    'type': 'fill',
                    'source': 'urban-areas',
                    'layout': {},
                    'paint': {
                        'fill-color': '#f08',
                        'fill-opacity': 0.4
                    }
// This is the important part of this example: the addLayer
// method takes 2 arguments: the layer as an object, and a string
// representing another layer's name. if the other layer
// exists in the stylesheet already, the new layer will be positioned
// right before that layer in the stack, making it possible to put
// 'overlays' anywhere in the layer stack.
// Insert the layer beneath the first symbol layer.
                },
                // firstSymbolId
            );
            
            




            map.on('click', 'random-points-data', function (e) {
                console.log("***")
                console.log(props);
                //props.funcToChange.dataFunc([1000])
                fetch("/view")
        .then((body) => body.json())
        .then((tweets) => {
            setTweets(tweets);
            // var description = e.features[0].properties.description;
            console.log(description)
                var getIndex = tweets["labels"].indexOf(description);
                tweets["datasets"][0]["data"] = tweets["datasets"][0]["data"].slice(getIndex, getIndex + 1);
                tweets["labels"] = tweets["labels"].slice(getIndex, getIndex + 1);
                props.funcToChange.dataFunc(tweets);
        }
                )
                fetch("/population")
        .then((body) => body.json())
        .then((population) => {
            //setTweets(population);
            // var description = e.features[0].properties.description;
            console.log(description)
                var getIndex = population["labels"].indexOf(description);
                population["datasets"][0]["data"] = population["datasets"][0]["data"].slice(getIndex, getIndex + 1);
                population["labels"] = population["labels"].slice(getIndex, getIndex + 1);
                props.funcToChange.dataFunc2(population);
        }
                )
                fetch("/age")
        .then((body) => body.json())
        .then((age) => {
            //setTweets(population);
            // var description = e.features[0].properties.description;
            console.log(description)
                var getIndex = age["labels"].indexOf(description);
                age["datasets"][0]["data"] = age["datasets"][0]["data"].slice(getIndex, getIndex + 1);
                age["labels"] = age["labels"].slice(getIndex, getIndex + 1);
                props.funcToChange.dataFunc3(age);
        }
                )
                var coordinates = e.features[0].geometry.coordinates.slice();
                var description = e.features[0].properties.description;
                console.log(description, tweets)


                // Ensure that if the map is zoomed out such that multiple
                // copies of the feature are visible, the popup appears
                // over the copy being pointed to.
                while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
                    coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
                }

                new mapboxgl.Popup()
                    .setLngLat(coordinates)
                    .setHTML(description)
                    .addTo(map);
            });
        });
        return () => map.remove();
    }, [lat]);

    return (
        <div ref={mapContainerRef} className="map-container" />
    );
}
