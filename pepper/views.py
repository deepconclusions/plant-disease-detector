from django.shortcuts import render
import pathlib
import numpy as np
from PIL import Image
import tensorflow_hub as hub

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PepperSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def getPredictions(request):
    # load model
    import tensorflow as tf
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    model = tf.keras.models.load_model(BASE_DIR / 'pepper/models/pepper_model.h5',
                                       custom_objects={'KerasLayer': hub.KerasLayer})

    # receive
    if request.method == 'POST':
        image_file = request.FILES['pepper-image']
        image = Image.open(image_file)
        image_array = np.array(image.resize((224, 224)))
        # predict
        prediction = np.argmax(model.predict(np.array([image_array])))
        data = {"Prediction": f"{prediction}",
                "ValueError": "No Errors Caught"}
        serializer = PepperSerializer(data)
        return Response(serializer.data)
    elif request.method == 'GET':
        data = {"Prediction": "No predicton",
                "ValueError": "No pepper image provided"}
        serializer = PepperSerializer(data)
        return Response(serializer.data)
