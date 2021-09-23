/*********************************************************************************
load the page
**********************************************************************************/

// hide output preloader until button click
var outputLoader = document.querySelector('#outputLoader');
outputLoader.style.display = "none";

// the page displays today's date - js build m/d/y format
n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
document.getElementById("date").innerHTML = m + "/" + d + "/" + y;

// preloader - started on page load - removed when promise hitting "/import" route kept
var inputLoader = document.querySelector('#inputLoader');
inputLoader.classList.add('spin');

// the Flask app "/import" route reads from the api and sends the data to this page
// we display these in an html table in buildTable function
// remove the preloader and load the data

d3.json("/import").then(function(myData) {
    inputLoader.style.display = "none";
    buildTable(myData);
});

// select the table body - table will be populated with data from api - Flask route "/import"
var forecast_body = d3.select("#forecast_body");

// Function to populate table
// Build table by looping myData (the api data) and get keys/vals write cells
function buildTable(forecastData){
    forecast_body.html("");//remove any rows of data from the table - start fresh each time
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

/*********************************************************************************
call prediction model on button click 
**********************************************************************************/

// select the button - users click to predict solar panel array output
var button = d3.select("#predict-btn");
//handler calls "apiCall" function
button.on("click", apiCall);

// make api call to Flask rout "/predict2" - the ML model lives here and returns an output prediction
// start preloader on click and remove when promise kept
// call outputTable function passing api result
function apiCall() {
    
    // preloader - started on button click - removed when promise hitting "/predict2" route kept
    outputLoader.style.display = "block";
    outputLoader.classList.add('spin');

    d3.json("/predict2").then(function(result) {
        console.log(result);
        console.log(result.result);
        outputLoader.style.display = "none";
        outputTable(result.result);
    });
    
};

// select the table body - build output prediction table here
var output_body = d3.select("#output_body");

// Build table by looping result and getting keys/vals write cells
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
