from plants.props import colored
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
    0: {"prediction": 0, "label": "Bacterial Spot", 
        "description": """
        Bacterial spot is a common disease that affects peppers and other plants in the Solanaceae family. It is caused by the bacteria Xanthomonas campestris pv. vesicatoria and can lead to significant crop losses if left untreated.
        Symptoms of bacterial spot on pepper plants include water-soaked lesions on leaves, stems, and fruit, which may eventually turn brown and become sunken. The lesions may also have a yellow halo around them, and leaves may curl or drop prematurely. In severe cases, the fruit may be distorted or cracked, making it unsuitable for market.
        To manage bacterial spot in pepper plants, it is important to use disease-free seed and transplants, rotate crops to prevent the buildup of the bacteria in the soil, and avoid overhead watering, as wet leaves can facilitate the spread of the disease. Copper-based fungicides can also be applied to protect plants from infection. However, it is important to note that once a plant is infected with bacterial spot, there is no cure, and infected plants should be removed and destroyed to prevent the spread of the disease to other plants.
        """
        },
    1: {"prediction": 1, "label": "Healthy", "description": "No disease detected in this"},
   }

@api_view(['GET', 'POST'])
def singlePrediction(request):
    # load model
    try:
        BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
        model = tf.keras.models.load_model(BASE_DIR / 'pepper/models/pepper_modelv2.h5',
                                        custom_objects={'KerasLayer': hub.KerasLayer})
        print(colored(0, 255, 0, "Pepper model loaded successfully"))
    except Exception as e:
        print(colored(255, 0, 0, "Error loading model or importing tensorflow"))
        print(colored(255, 0, 0, str(e)))
    # receive input image
    if request.method == 'POST':
        # open image file using PIL
        if 'pepper-image' in request.FILES:
            image_file = request.FILES['pepper-image']
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
            serializer = PepperSerializer(data)
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
        serializer = PepperSerializer(data)
        return Response(serializer.data)


def multiplePrediction(request):
    pass