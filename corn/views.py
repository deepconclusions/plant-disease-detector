from django.shortcuts import render
import pathlib
import numpy as np
from PIL import Image
import tensorflow_hub as hub

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CornSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def getPredictions(request):
    # load model
    import tensorflow as tf
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    model = tf.keras.models.load_model(BASE_DIR / 'corn/corn_model.h5',
                                       custom_objects={'KerasLayer': hub.KerasLayer})

    # receive
    if request.method == 'POST':
        image_file = request.FILES['corn-image']
        # open image file using PIL
        image = Image.open(image_file)
        # convert image to numpy array
        image_array = np.array(image.resize((224, 224)))
        # predict
        prediction = np.argmax(model.predict(np.array([image_array])))
        data = {"Prediction": f"{prediction}",
                "ValueError": "No Errors Caught"}
        serializer = CornSerializer(data)
        return Response(serializer.data)
    elif request.method == 'GET':
        data = {"Prediction": "No predicton",
                "ValueError": "No corn image provided"}
        serializer = CornSerializer(data)
        return Response(serializer.data)
