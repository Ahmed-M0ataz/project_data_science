document.addEventListener("DOMContentLoaded", function () {
    const predictionForm = document.getElementById("prediction-form");
    const predictionResult = document.getElementById("prediction-result");

    // Get today's date in "yyyy-MM-ddTHH:mm" format
    const today = new Date().toISOString().slice(0, 16);

    // Set initial value for the datetime-local input
    const dateInput = document.getElementById("date");
    dateInput.value = today;

    predictionForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(predictionForm);
        const response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        predictionResult.textContent = `Predicted Appliances: ${data.prediction.toFixed(2)}`;
    });
});
