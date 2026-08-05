const button = document.getElementById("favourite-btn");

const id = button.dataset.id

button.addEventListener("click", function(){
    fetch(`/favourites/${id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {

        if (data.favourite) {
            button.textContent = "Unfavourite";
        }

        else {
            button.textContent = "Favourite"
        }
    });
});