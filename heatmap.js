var mapbox = 'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ';

var myMap = L.map('map', {
    center: [39.25, -99.75],
    zoom: 6
});

L.tileLayer(mapbox).addTo(myMap);

var url = "/awards";

d3.json(url, function(response){

    console.log(response);

    var heatArray = [];

    for (var i = 0; i < 100; i++) {
        var location = response[i];

        // console.log(location);

        if (location) {
            heatArray.push([location.latitude, location.longitude]);
        }
    }

    L.heatLayer(heatArray, {
        radius: 20,
        blur: 35
    }).addTo(myMap);

});