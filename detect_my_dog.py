from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

def predict_breed(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Make a prediction
    preds = model.predict(x)

    # Decode the prediction
    print('Predicted:', decode_predictions(preds, top=3)[0])

predict_breed('my_dog_biting.jpg')