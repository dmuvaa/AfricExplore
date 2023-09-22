async function fetchAndDisplayProperties(destinationId) {
    // If destinationId is not passed in, fetch it from the dropdown
    if (!destinationId) {
        destinationId = document.getElementById('destinationDropdown').value;
    }
    
    // Use the selected destination to construct the API endpoint URL
    const apiUrl = `/get_properties?destinationId=${destinationId}`;
  
    try {
        const response = await fetch(apiUrl);
  
        // Check if response was successful
        if (!response.ok) {
            console.error("Server responded with an error:", response.statusText);
            return;  // Exit from the function
        }
  
        const data = await response.json();
  
        // Check if data exists and it doesn't have an error property
        if (!data) {
            console.error("Received null or undefined data from the server.");
            return;
        }
  
        if (data.error) {
            console.error("Error from server:", data.error);
            return;
        }
  
        let propertyResults = document.getElementById('propertyResults');
        propertyResults.innerHTML = "";  // Clear current listings
  
        data.forEach(property => {
            let propertyItem = document.createElement('div');
            propertyItem.className = 'property-box';  // Add CSS class for styling
            propertyItem.innerHTML = `
                <img src="${property.main_photo_url}" alt="Hotel Image">
                <h2>${property.hotel_id}</h2>  <!-- Replace with property.name if it exists -->
                <p>Location: ${property.city_in_trans}</p>
                <p>Distance: ${property.distance} km</p>
                <p>District: ${property.district}</p>
                <p>Price: ${property.min_total_price} USD</p>
                <button onclick="bookProperty('${property.name}')">Book Now</button>
            `;
            propertyResults.appendChild(propertyItem);
        });
    } catch (error) {
        console.error("There was an error fetching the properties:", error);
    }
  }
  
  function bookProperty(propertyName) {
    // Your booking logic here
    // As an example:
    alert(`Booking for ${propertyName} initiated!`);
  }
  
  // Optionally, you can add an event listener for when the document is fully loaded:
  document.addEventListener('DOMContentLoaded', (event) => {
    // This code runs once the DOM is ready. You can add any startup scripts here.
  });
  