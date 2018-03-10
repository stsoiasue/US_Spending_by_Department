var light = L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
    "T6YbdDixkOBWH_k9GbS8JQ"
);
var dark = L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
    "T6YbdDixkOBWH_k9GbS8JQ"
);

var myMap = L.map('map', {
    center: [39.25, -99.75],
    zoom: 5,
    layers: [light]
});

var url = "/awards";

d3.json(url, function(response){

    var heatArray1 = [];
    var heatArray2 = [];
    var heatArray3 = [];
    
for (var i = 0; i < response.length; i++) {
    var location_lat = +response[i].Latitude;
    var location_lon = +response[i].Longitude;
    var obligation = +response[i].Total_Obligation;

    if (response[i].Awarding_Agency === "Department of Transportation") {
        heatArray1.push([location_lat, location_lon, obligation]);
    }

     else if (response[i].Awarding_Agency === "Department of Agriculture") {
        heatArray2.push([location_lat, location_lon, obligation]);
    }

    else (response[i].Awarding_Agency === "Department of Interior") ;{
        heatArray3.push([location_lat, location_lon, obligation]);
    };
   
    }

    var heat = L.heatLayer(heatArray1, {
        radius: 3,
        blur: 3
    });
    
    var heat2 = L.heatLayer(heatArray2, {
        radius: 3,
        blur: 2
    });

    var heat3 = L.heatLayer(heatArray3, {
        radius: 3,
        blur: 2
    });

    var overlaybase ={
        Satellite: light,
        Dark: dark
    };

    var overlayLayers2 ={
        Department_of_Transportation: heat,
        Department_of_Agriculture: heat2,
        Deprartment_of_Interior: heat3
    };

    L.control
        .layers(overlaybase, overlayLayers2)
        .addTo(myMap)})


