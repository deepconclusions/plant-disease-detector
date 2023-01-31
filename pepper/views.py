from django.shortcuts import render
import pathlib
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PepperSerializer

# Create your views here.
classes = {
    0: {"prediction": 0, "label": "Healthy", "description": "Long description about healthy"},
    1: {"prediction": 1, "label": "Cercospora", "description": "Long description about cercospora"},
    2: {"prediction": 2, "label": "Northern leaf blight", "description": "Long description about Northern leaf blight"},
    3: {"prediction": 3, "label": "Common rust", "description": "Long description about Common rust"}
}


@api_view(['GET', 'POST'])
def singlePrediction(request):
    # load model
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    # receive input image
    if request.method == 'POST':
        # open image file using PIL
        if 'pepper-image' in request.FILES:
            model = tf.keras.models.load_model(BASE_DIR / 'pepper/models/pepper_model.h5',
                                               custom_objects={'KerasLayer': hub.KerasLayer})
            image_file = request.FILES['pepper-image']
            image = Image.open(image_file)
            # convert image to numpy array
            image_array = np.array(image.resize((224, 224)))
            # predict
            predictions = model.predict(np.array([image_array]))
            prediction = np.argmax(predictions)
            confidence = np.max(predictions)
            data = classes[prediction]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = pepperSerializer(data)
            return Response(serializer.data)
        else:
            data = {"prediction": 999,
                    "label": "No predicton",
                    "confidence": 0.0,
                    "description": "No description",
                    "value_error": "Either No pepper image is provided or It is not labelled, make sure to label with 'pepper-image'"}
            serializer = PepperSerializer(data)
            return Response(serializer.data)
    elif request.method == 'GET':
        data = {"prediction": 999,
                "label": "No label",
                "confidence": 0.0,
                "description": "No description",
                "value_error": "You are probably not making a POST request, contact concerned personnel for advice"}
        serializer = pepperSerializer(data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def multiplePrediction(request):
    pass
