function uploadAudio() {
    console.log("Hiiii 1")
    const fileInput = document.getElementById('audioFile');
    console.log("Hiiii 2")
    const resultElement = document.getElementById('result');
    console.log("Hiiii 3")
    if (fileInput.files.length === 0) {
        resultElement.innerText = "Please select an audio file.";
        return;
    }

    console.log("Hiiii 5")
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('audioFile', file);
    console.log("Hiiii 6")
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        resultElement.innerText = result;
    })
    .catch(error => {
        console.error('Error:', error);
        resultElement.innerText = "An error occurred. Please try again.";
    });
}
