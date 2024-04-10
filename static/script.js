document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('tweetForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        // Get the text input from the form
        const text = document.getElementById('tweetText').value;

        // Send AJAX request to Flask server
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            resultDiv.innerText = `Predicted class: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerText = 'An error occurred.';
        });
    });
});

