document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('id_default_country');
    
    function updateColor() {
        const countrySelected = countrySelect.value;
        countrySelect.style.color = countrySelected ? '#000' : '#aab7c4';
    }

    // Initial color set
    updateColor();

    // Listen for changes
    countrySelect.addEventListener('change', updateColor);
});