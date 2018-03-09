var mapbox = 'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ';

var myMap = L.map('map', {
    center: [39.25, -99.75],
    zoom: 6
});

L.tileLayer(mapbox).addTo(myMap);

var url = "/awards";

d3.json(url, function(response){

    // console.log(response);

    var heatArray = [];

    for (var i = 0; i < response.length; i++) {
        var location_lat = +response[i].Latitude;
        var location_lon = +response[i].Longitude;
        var obligation = +response[i].Total_Obligation
         
        heatArray.push([location_lat, location_lon, obligation]);
    }

    L.heatLayer(heatArray, {
        radius: 3,
        blur: 2
    }).addTo(myMap);

});