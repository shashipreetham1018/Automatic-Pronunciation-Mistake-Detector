
function checkPronunciation() {
    const word = document.getElementById("word").value.trim();
    const resultDiv = document.getElementById("result");

    if (!word) {
        resultDiv.textContent = "Please enter a word.";
        resultDiv.style.color = "red";
        return;
    }

    resultDiv.textContent = "Listening...";

    fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `target_word=${word}`,
    })
        .then((response) => response.json())
        .then((data) => {
            resultDiv.textContent = data.message;
            resultDiv.style.color = data.status === "success" ? "limegreen" : "red";
        })
        .catch(() => {
            resultDiv.textContent = "Error occurred. Please try again.";
            resultDiv.style.color = "red";
        });
}
