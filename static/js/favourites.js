const filter = document.getElementById("Filter");

filter.addEventListener('change', function() {
    const value = filter.value;

    fetch(`/favourites/filter/${value}`)
    .then(response => response.text())
    .then(html => {
        document.getElementById('favourites-container').innerHTML = html;
    })
})