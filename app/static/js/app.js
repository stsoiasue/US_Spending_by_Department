// Mapbox API
var mapbox = "https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ";

// Creating map object
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Adding tile layer to the map
L.tileLayer(mapbox).addTo(myMap);

var awardsURL = '/awards';

d3.json(awardsURL, function(error, awards) {
    if (error) {
        console.warn(error);
    };

    var coord_dict = {};

    for (i=0; i<awards.length; i++) {

        if (awards.POP_Zip in coord_dict) {
            coord_dict[awards.POP_Zip] = coord_dict[awards.POP_Zip] + awards.Total_Obligation
        }

    }

})