// Get temperature and wind speed from the DOM
let getTemp = document.getElementById('temperature').textContent;
let getWind = document.getElementById('windspeed').textContent;

// Parse the text content to integers
let temperature = parseInt(getTemp, 10);
let windSpeed = parseInt(getWind, 10);

// Function to calculate wind chill
function calculateWindChill(temperature, windSpeed) {
    return 35.74 + (0.6215 * temperature) - (35.75 * (windSpeed ** 0.16)) + (0.4275 * temperature * (windSpeed ** 0.16));
}

// Check if the values meet the specification limits
if (temperature <= 50 && windSpeed > 3) {
    let windChill = calculateWindChill(temperature, windSpeed);
    document.getElementById('windchill').textContent = windChill.toFixed(1) + '°F';
} else {
    document.getElementById('windchill').textContent = 'N/A';
}
