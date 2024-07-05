const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('capture');
const recaptureButton = document.getElementById('recapture');
const resultText = document.getElementById('result');
const capturedImage = document.getElementById('capturedImage');

// Access the device camera and stream to video element
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(error => {
        console.error('Error accessing the camera', error);
    });

captureButton.addEventListener('click', () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('image', blob, 'capture.png');

        // Display captured image
        capturedImage.src = URL.createObjectURL(blob);
        capturedImage.style.display = 'block';
        video.style.display = 'none';
        captureButton.style.display = 'none';
        recaptureButton.style.display = 'block';

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultText.innerText = 'Expression: ' + data.expression;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, 'image/png');
});

recaptureButton.addEventListener('click', () => {
    video.style.display = 'block';
    captureButton.style.display = 'block';
    recaptureButton.style.display = 'none';
    capturedImage.style.display = 'none';
    resultText.innerText = '';
});
