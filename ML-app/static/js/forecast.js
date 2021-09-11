// Fetch the JSON data and console log it
mockData = []

d3.json("/import").then(function(myData) {
    // load all data
    buildTable(myData);
    mockData = myData
});

// Use D3 to select the table body
var forecast_body = d3.select("#forecast_body");

//Function to populate table with all or user filtered data
// Build table by loop myData and get keys/vals write cells
function buildTable(forecastData){
    forecast_body.html("");//remove any rows of data from the table
    forecastData.forEach((date) => {
        // Append one table row per object
        var row = forecast_body.append("tr");
        // append one td for each key value
        Object.entries(date).forEach(([key, value]) => {
        var cell = row.append("td");
        //set the td value to the key value
        cell.text(value);
        });
    });
};

var button = d3.select("#predict-btn");

// //handler
button.on("click", apiCall);

function apiCall() {
    
    d3.json("/predict2").then(function(result) {
        console.log(result);
        outputTable(result.result);
    });
    
};

// Use D3 to select the table body
var output_body = d3.select("#output_body");

//Function to populate table with all or user filtered data
// Build table by loop myData and get keys/vals write cells
function outputTable(prediction){
    output_body.html("");//remove any rows of data from the table
    console.log(prediction);
    prediction.forEach((hour) => {
        // Append one table row per object
        var row = output_body.append("tr");
        // append one td for each key value
        Object.entries(hour).forEach(([key, value]) => {
            var keyCell = row.append("td");
            var valCell = row.append("td");
            //set the td value to the value
            keyCell.text(key);
            valCell.text(value);
        });
    });
};


