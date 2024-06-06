document.addEventListener('DOMContentLoaded', (event) => {
    function calculateWindChill(temperature, windSpeed) {
        // Wind chill formula
        return 35.74 + (0.6215 * temperature) - (35.75 * Math.pow(windSpeed, 0.16)) + (0.4275 * temperature * Math.pow(windSpeed, 0.16));
    }

    function updateWindChill() {
        const temperatureElement = document.getElementById('temperature');
        const windSpeedElement = document.getElementById('windspeed');
        const windChillElement = document.getElementById('windchill');

        const temperature = parseFloat(temperatureElement.textContent);
        const windSpeed = parseFloat(windSpeedElement.textContent);

        // Check if the values meet the specification limits
        if (temperature <= 50 && windSpeed > 3) {
            const windChill = calculateWindChill(temperature, windSpeed);
            windChillElement.textContent = windChill.toFixed(2) + '°F';
        } else {
            windChillElement.textContent = 'N/A';
        }
    }

    updateWindChill();
});
