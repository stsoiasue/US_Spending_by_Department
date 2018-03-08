anychart.onDocumentReady(function() {
    anychart.theme('darkBlue')

    var url = 'https://api.usaspending.gov/api/v1/awards/?limit=10&page=1';

    d3.json(url, function(error, response) {
        if (error) {
            console.warn(error)
        };

        console.log(response);

        var contracts = response.results;
    
        var data = [];

        for (j=0; j<contracts.length; j++) {
            
            var sLat, sLong;
            state = contracts[j].place_of_performance.state_name.toLowerCase();

            for (i=0; i<stateDict.length; i++) {
                if (stateDict[i]['state_name'].toLowerCase() === state) {
                   
                    sLat = stateDict[i].latitude;
                    sLong = stateDict[i].longitude;
                    break;

                };
            } ;
            
            contractDict = {
                lat: sLat,
                long: sLong,
                name: contracts[j].awarding_agency.toptier_agency.name,
                recipient: contracts[j].recipient.recipient_name,
                amount: +contracts[j].total_obligation + (j + 1),
                description: contracts[j].description,
                depShare: 10,
                totalShare: 5
            };

            data.push(contractDict);

        };
        

        function drawMapChart() {
            // creates map chart
            var map = anychart.map();

            // sets geodata
            map.geoData(anychart.maps.united_states_of_america);

            // sets Chart Title
            map.title()
                .enabled(true)
                .useHtml(true)
                .padding([0, 0, 10, 0])
                .text('Top 10 Government Contracts<br/><span style="color:#929292; font-size: 12px;">' +
                'Department of Transportation, Department of Interior, Department of Agriculture</span>');

            // sets marker series
            var series = map.marker(data);

            series.tooltip().format(function(e){
                return "Recipient: " + e.getData("recipeint") +"\n"+
                "Dollars Obligated: " + e.getData("amount") +"\n"+
                "Dscription: " + e.getData("description")
             });

            // sets container id for the chart
            map.container('container');
            map.listen('pointsselect', function(e) {
                selectedPoint = e.currentPoint;
                if (selectedPoint) {
                  changeContents(selectedPoint.index);
                };
            });
            // return map var
            return map

        };

        function createSolidChart() {
            var gauge = anychart.gauges.circular();
            gauge.background(null);
            gauge.fill(null);
            gauge.stroke(null);
            gauge.padding([30, 0, 0, 0]);
            gauge.title().enabled(true).useHtml(true).padding([0, 0, 15, 0]);
            var axis = gauge.axis().radius(70).width(1).fill(null);
            axis.scale()
              .minimum(0)
              .maximum(100)
              .ticks({
                interval: 1
              })
              .minorTicks({
                interval: 1
              });
            axis.labels().enabled(false);
            axis.ticks().enabled(false);
            axis.minorTicks().enabled(false);
            var stroke = '1 #e5e4e4';
            gauge.bar(0).dataIndex(0).radius(70).width(40).fill('#64b5f6').stroke(null).zIndex(5);
            gauge.bar(1).dataIndex(1).radius(70).width(40).fill('#F5F4F4').stroke(stroke).zIndex(4);
            gauge.label()
              .text('')
              .fontSize(20)
              .hAlign('center')
              .anchor('center')
              .padding(0)
              .zIndex(1);
            return gauge
        }

        function changeContents(index) {
            totalShareChart.data([data[index].totalShare, 100]);
            totalShareChart.label().text(data[index].totalShare + '%');
            totalShareChart.title().text('Percentage of Total Contracts<br/><span style="color: #212121; text-decoration: underline">' + data[index].description.toLowerCase() + '</span>');
            departmentShareChart.data([data[index].depShare, 100]);
            departmentShareChart.label().text(data[index].depShare + '%');
            departmentShareChart.title().text('Percentage of Department Contracts<br/><span style="color: #212121; text-decoration: underline">Department: ' + data[index].name + '</span>');
        };

        var mapChart = drawMapChart();
        var totalShareChart = createSolidChart();
        var departmentShareChart = createSolidChart();

        // Setting layout table
        var layoutTable = anychart.standalones.table();
        layoutTable.cellBorder(null);
        layoutTable.container('container');


        
        function fillInMainTable(flag) {
            if (flag == 'wide') {
                layoutTable.contents([
                    [mapChart, totalShareChart],
                    [null, departmentShareChart]
                ], true);
                layoutTable.getCell(0, 0).rowSpan(2);
            } else {
                layoutTable.contents([
                    [mapChart, null],
                    [totalShareChart, departmentShareChart]
                ], true);
                layoutTable.getCell(0, 0).colSpan(2);
            }
            layoutTable.draw();
        }

        window.onresize = function() {
            if (layoutTable.colsCount() == 2 && window.innerWidth > 767) {
              fillInMainTable('wide');
            } else if (layoutTable.colsCount() == 2 && window.innerWidth <= 767) {
              fillInMainTable('slim');
            }
        };

        if (window.innerWidth > 768)
            fillInMainTable('wide');
        else {
            fillInMainTable('slim');
        };
    });
});
