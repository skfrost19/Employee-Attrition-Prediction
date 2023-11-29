window.onload = function () {
    // Get all input elements
    let inputs = document.querySelectorAll('input[type="number"]');

    // Assign random values to number inputs
    inputs.forEach((input) => {
        input.value = Math.floor(Math.random() * 100);
    });

    // Get all select elements
    let selects = document.querySelectorAll("select");

    // Assign random values to select inputs
    selects.forEach((select) => {
        let options = select.options;
        let randomIndex = Math.floor(Math.random() * options.length);
        select.selectedIndex = randomIndex;
    });
};

function isNumeric(str) {
    if (typeof str != "string") return false; // we only process strings!
    return (
        !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
        !isNaN(parseFloat(str))
    ); // ...and ensure strings of whitespace fail
}

document.querySelector(".atr").addEventListener("submit", function (e) {
    e.preventDefault();

    // Get form data
    let formData = new FormData(e.target);

    // Convert form data to JSON
    let data = {};
    formData.forEach((value, key) => (data[key] = value));

    // try to convert the values to int (use try catch to avoid errors) (if not integer then leave it as it is)
    for (let key in data) {
        if (isNumeric(data[key])) {
            data[key] = parseInt(data[key]);
        }
    }

    let json = JSON.stringify(data);
    console.log(json);

    // Send a POST request to the server
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: json,
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("output").value = data;
        })
        .catch((error) => console.error("Error:", error));
});
