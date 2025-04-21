// Initialize Google Map
function initMap() {
    const map = new google.maps.Map(document.getElementById('google-map'), {
        center: { lat: 37.7749, lng: -122.4194 }, // Default to San Francisco
        zoom: 12,
    });

    // Add markers for cafes (example)
    const cafes = [
        { name: "Cafe 1", location: { lat: 37.7749, lng: -122.4194 } },
        { name: "Cafe 2", location: { lat: 37.7849, lng: -122.4294 } },
    ];

    cafes.forEach(cafe => {
        new google.maps.Marker({
            position: cafe.location,
            map: map,
            title: cafe.name,
        });
    });
}

// Delete cafe (admin only)
function deleteCafe(cafeId) {
    if (confirm("Are you sure you want to delete this cafe?")) {
        fetch(`/delete/${cafeId}`, { method: 'GET' })
            .then(response => window.location.reload());
    }
}
