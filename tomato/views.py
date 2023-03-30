import pathlib
from plants.props import colored
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TomatoSerializer

# Create your views here.
classes = {
    0: {"prediction": 0, "label": "Bacterial spot", "description": "Long description about healthy"},
    1: {"prediction": 1, "label": "Early blight", "description": "Long description about cercospora"},
    2: {"prediction": 2, "label": "Late blight", "description": "Long description about Northern leaf blight"},
    3: {"prediction": 3, "label": "Leaf Mold", "description": "Long description about Common rust"},
    4: {"prediction": 3, "label": "Septoria leaf spot", "description": "Long description about Common rust"},
    5: {"prediction": 3, "label": "Spider mites, Two-spotted spider mite", "description": "Long description about Common rust"},
    6: {"prediction": 3, "label": "Target Spot", "description": "Long description about Common rust"},
    7: {"prediction": 3, "label": "Tomato Yellow Leaf Curl Virus", "description": "Long description about Common rust"},
    8: {"prediction": 3, "label": "Mosaic virus", "description": "Long description about Common rust"},
    9: {"prediction": 3, "label": "Healthy", "description": "Long description about Common rust"},
}


@api_view(['GET', 'POST'])
def singlePrediction(request):
    # load model
    try:
        BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
        model = tf.keras.models.load_model(BASE_DIR / 'tomato/models/tomato_modelv2.h5',
                                        custom_objects={'KerasLayer': hub.KerasLayer})
        print(colored(0, 255, 0, "Tomato model loaded successfully"))
    except:
        print(colored(255, 0, 0, "Error loading model or importing tensorflow"))

    # receive input image
    if request.method == 'POST':
        # open image file using PIL
        if 'tomato-image' in request.FILES:
            image_file = request.FILES['tomato-image']
            image = Image.open(image_file)
            # convert image to numpy array
            image_array = np.array(image.resize((224, 224)))
            image_array = image_array / 255
            # predict
            predictions = model.predict(np.array([image_array]))
            prediction = np.argmax(predictions)
            confidence = np.max(predictions)
            data = classes[prediction]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = TomatoSerializer(data)
            return Response(serializer.data)
        else:
            data = {"prediction": 999,
                    "label": "No predicton",
                    "confidence": 0.0,
                    "description": "No description",
                    "value_error": "Either No tomato image is provided or It is not labelled, make sure to label with 'tomato-image'"}
            serializer = TomatoSerializer(data)
            return Response(serializer.data)
    elif request.method == 'GET':
        data = {"prediction": 999,
                "label": "No label",
                "confidence": 0.0,
                "description": "No description",
                "value_error": "You are probably not making a POST request, contact concerned personnel for advice"}
        serializer = TomatoSerializer(data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def multiplePrediction(request):
    pass
