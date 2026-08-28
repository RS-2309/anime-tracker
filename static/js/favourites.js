const filter = document.getElementById("Filter");

filter.addEventListener('change', function() {
    const value = filter.value;

    fetch(`/favourites/filter/${value}`)
    .then(response => response.text())
    .then(html => {
        document.getElementById('favourites-container').innerHTML = html;
    });
});

const sort = document.getElementById("Sort");

sort.addEventListener('change', function() {
    const value = sort.value;

    fetch(`/favourites/sort/${value}`)
    .then(response => response.text())
    .then(html => {
        document.getElementById(`favourites-container`).innerHTML = html
    });
});