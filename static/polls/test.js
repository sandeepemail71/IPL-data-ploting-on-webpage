function plotMatchesPerYear(x, y) {
  console.log(x);
  console.log(y);
  var chart = {
    type: "column"
  };
  var title = {
    text: "Matches per Year"
  };
  var subtitle = {
    text: "Source: CSV file"
  };
  var xAxis = {
    categories: x,
    crosshair: true,
    title: {
        text: "Years",
        margin: 10,
        style: {
            color: 'blue',
            fontWeight: 'bold'
        
        }
      }
  };
  var yAxis = {
    min: 0,
    title: {
        text: "No of Matches",
        margin: 10,
        style: {
            color: 'blue',
            fontWeight: 'bold'
        
        }
      }
  };

  var plotOptions = {
    column: {
      pointPadding: 0.05,
      borderWidth: 0
    }
  };
  var credits = {
    enabled: false
  };
  var series = [
    {
      name: "Matches",
      data: y
    }
  ];

  var json = {};
  json.chart = chart;
  json.title = title;
  json.subtitle = subtitle;
  json.xAxis = xAxis;
  json.yAxis = yAxis;
  json.series = series;
  json.plotOptions = plotOptions;
  json.credits = credits;
  return json;
}

function economicalBowler(x, y) {
  console.log(x);
  console.log(y);
  var chart = {
    type: "column"
  };
  var title = {
    text: "Economical Bowlers"
  };
  var subtitle = {
    text: "Source: CSV file"
  };
  var xAxis = {
    categories: x,
    crosshair: true,

    title: {
      text: "Bowlers",
      margin: 10,
      style: {
        color: "blue",
        fontWeight: "bold"
      }
    }
  };
  var yAxis = {
    min: 0,
    title: {
        text: "Average Runs",
        margin: 10,
        style: {
            color: 'blue',
            fontWeight: 'bold'
        
        }
      }
  };

  var plotOptions = {
    column: {
      pointPadding: 0.05,
      borderWidth: 0
    }
  };
  var credits = {
    enabled: false
  };
  var series = [
    {
      name: "Avg Runs",
      data: y
    }
  ];

  var json = {};
  json.chart = chart;
  json.title = title;
  json.subtitle = subtitle;
  json.xAxis = xAxis;
  json.yAxis = yAxis;
  json.series = series;
  json.plotOptions = plotOptions;
  json.credits = credits;
  return json;
}


function extraRun(x, y) {
  console.log(x);
  console.log(y);
  var chart = {
    type: "column"
  };
  var title = {
    text: "Extra Runs in 2016"
  };
  var subtitle = {
    text: "Source: CSV file"
  };
  var xAxis = {
    categories: x,
    crosshair: true,
    title: {
      text: "Bowling Teams",
      margin: 10,
      style: {
        color: "blue",
        fontWeight: "bold"
      }
    }
  };
  var yAxis = {
    min: 0,
    title: {
      text: "Runs",
      margin: 10,
      style: {
        color: "blue",
        fontWeight: "bold"
      }
    }
  };

  var plotOptions = {
    column: {
      pointPadding: 0.05,
      borderWidth: 0
    }
  };
  var credits = {
    enabled: false
  };
  var series = [
    {
      name: "Runs",
      data: y
    }
  ];

  var json = {};
  json.chart = chart;
  json.title = title;
  json.subtitle = subtitle;
  json.xAxis = xAxis;
  json.yAxis = yAxis;
  json.series = series;
  json.plotOptions = plotOptions;
  json.credits = credits;
  return json;
}
