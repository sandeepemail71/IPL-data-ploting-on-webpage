function plot(x,y){
    
    console.log(x)
    
    console.log(y)
    var chart = {
        type: 'column'
    };
    var title = {
        text: 'Matches per Year'
        
    };
    var subtitle = {
        text: 'Source: CSV file'
    };
    var xAxis = {
        categories: x ,
        crosshair: true
    };
    var yAxis = {
        min: 0,
        title: {
            text: 'Years'
        }
    };

    var plotOptions = {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    };
    var credits = {
        enabled: false
    };
    var series = [
        {
            name: 'matches',
            data: y
        }
    ];

    var json = {};
    json.chart = chart;
    json.title = title;
    json.subtitle = subtitle;
    //json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    json.credits = credits;
    return json;
}