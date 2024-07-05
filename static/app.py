import io
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
from flask import Flask, request, jsonify, render_template
import timm


# Define your model class
class FaceModel(nn.Module):
    def __init__(self):
        super(FaceModel, self).__init__()
        self.eff_net = timm.create_model('efficientnet_b0', pretrained=False, num_classes=7)

    def forward(self, images):
        logits = self.eff_net(images)
        return logits

# Load the model
model = FaceModel()
model.load_state_dict(torch.load('best-weights.pt', map_location=torch.device('cpu')))
model.eval()

# Define the transform to preprocess the image
transform = transforms.Compose([
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# Initialize Flask app
app = Flask(__name__, static_folder='static') 
# Route to serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    classes = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))
    img = img.convert('RGB')  # Convert to RGB
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output.data, 1)
        expression = classes[predicted.item()]

    return jsonify({'expression': expression})

if __name__ == '__main__':
    app.run(debug=True)
