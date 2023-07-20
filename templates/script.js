// script.js

function makePrediction() {
    // Get the text data from the textarea
    var textData = document.getElementById('text').value;

    // Make an asynchronous request to the server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/predict', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Update the prediction result on the page
            var predictionResult = JSON.parse(xhr.responseText).prediction;
            document.getElementById('predictionResult').innerText = "Prediction: " + predictionResult;
        } else {
            console.error('Error:', xhr.statusText);
        }
    };
    xhr.onerror = function () {
        console.error('Request failed.');
    };
    xhr.send(JSON.stringify({ 'text': textData }));
}
