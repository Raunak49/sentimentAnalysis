document.getElementById("analyze-button").addEventListener("click", function() {
    const dreamDescription = document.getElementById("dream-input").value;
  
    // Replace YOUR_NGROK_URL with the actual ngrok URL
    const apiUrl = 'https://sentimentanalysis-dl55.onrender.com/backend/';
  
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin':'*',
      },
      body: JSON.stringify({text: dreamDescription}),
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
       document.querySelector(".sentiment-analysis-display h2").textContent = `Your dream emotion is: ${data.result}`;
    })
    .catch((error) => {
       console.error('Error:', error);
    });
  })