var mapbox = 'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ';

var myMap = L.map('map', {
    center: [39.25, -99.75],
    zoom: 6
});

L.tileLayer(mapbox).addTo(myMap);

var url = "https://data.sfgov.org/resource/gxxq-x39z.json?$limit=1000";

// EXAMPLE ARRAY OF DICTIONARIES TO PULL FROM FLASK APP:
// [ {
//     "date" : "2005-04-20T00:00:00",
//     "address" : "18TH ST / CASTRO ST",
//     "pddistrict" : "MISSION",
//     "incidntnum" : "050436712",
//     "x" : "-122.435002864271",
//     "dayofweek" : "Wednesday",
//     "y" : "37.7608878061245",
//     "location" : {
//       "latitude" : "37.7608878061245",
//       "human_address" : "{\"address\":\"\",\"city\":\"\",\"state\":\"\",\"zip\":\"\"}",
//       "needs_recoding" : false,
//       "longitude" : "-122.435002864271"
//     },
//     "time" : "04:00",
//     "category" : "ASSAULT",
//     "descript" : "BATTERY",
//     "resolution" : "NONE"

// SUBJECT ITEMS:
// awards = (session.query(Awards).limit(5))
// for award in awards:
//     print(award.total_obligation)
//     print(award.awarding_agency)
//     print(award.recipient_name)
//     print(award.recipient_zip)
//     print(award.date_signed)

// 500.0
// Department of Agriculture
// FIRST SERVICE APPRAISAL INC
// 57201
// 2017-08-23
// 9048.0


d3.json(url, function(response){

    console.log(response);

    for (var i = 0; i < response.length; i++) {
        var location = response[i].location;

        if (location) {
            L.marker([location.latitude, location.longitude])
                .addTo(myMap);
        }
    }

});