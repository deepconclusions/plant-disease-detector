import pathlib
from plants.props import colored
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow.compat.v1 as tfcv1
import tensorflow_hub as hub
from django.shortcuts import HttpResponse

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CornSerializer


# Create your views here.
classes = [{"prediction": 0, 
        "label": "Cercospora", 
        "description": """
        <p>Cercospora is a fungal genus that can cause leaf spot diseases in a wide range of plants, including vegetables, fruits, and ornamental plants. The disease appears as small, circular spots on leaves that can range in color from gray to brown to purple. As the disease progresses, the spots may enlarge and merge, causing the leaves to turn yellow and eventually die off.</p>
        <p>Cercospora leaf spot can be controlled through a combination of cultural, chemical, and biological methods. Cultural methods include removing and destroying infected plant material, planting disease-resistant varieties, and practicing good sanitation in the garden. Chemical control involves using fungicides to prevent the spread of the disease, and biological control involves introducing natural predators or beneficial microorganisms to the affected area.</p>
        <p>The length of time and cost to treat Cercospora will depend on the severity of the disease and the size of the affected area. Mild cases can often be controlled through cultural methods alone, while more severe cases may require a combination of cultural and chemical methods. The cost of treatment will also vary depending on the products used and the size of the affected area. It is best to consult with a local plant specialist or extension agent for specific recommendations for your area and situation.</p>
        """
        },
    {"prediction": 1, 
        "label": "Common rust", 
        "description": """
        Northern leaf blight is a fungal disease that affects corn plants. It is caused by the fungus Exserohilum turcicum and can cause significant yield losses if left untreated. The disease typically appears as cigar-shaped lesions on the leaves that are gray-green to brown in color. As the disease progresses, the lesions can enlarge and merge, leading to premature death of the leaves.\n\n
        To control Northern leaf blight, it is important to practice good cultural management techniques such as rotating crops, using disease-free seed, and controlling weeds. Chemical control can also be effective, and several fungicides are available that can be used to prevent or treat the disease. It is important to carefully follow label instructions when using fungicides.\n\n
        The length of time and cost to treat Northern leaf blight will depend on the severity of the disease and the size of the affected area. Mild cases may only require cultural management techniques, while more severe cases may require the use of fungicides. The cost of treatment will also depend on the products used and the size of the affected area. It is best to consult with a local plant specialist or extension agent for specific recommendations for your area and situation.
        """
        },
    {"prediction": 2, 
        "label": "Healthy", 
        "description": "Long description about healthy"},
    {"prediction": 3, 
        "label": "Northern leaf blight", 
        "description": """
        Northern leaf blight is a fungal disease that affects corn plants. It is caused by the fungus Exserohilum turcicum and can cause significant yield losses if left untreated. The disease typically appears as cigar-shaped lesions on the leaves that are gray-green to brown in color. As the disease progresses, the lesions can enlarge and merge, leading to premature death of the leaves.\n\n
        To control Northern leaf blight, it is important to practice good cultural management techniques such as rotating crops, using disease-free seed, and controlling weeds. Chemical control can also be effective, and several fungicides are available that can be used to prevent or treat the disease. It is important to carefully follow label instructions when using fungicides.\n\n
        The length of time and cost to treat Northern leaf blight will depend on the severity of the disease and the size of the affected area. Mild cases may only require cultural management techniques, while more severe cases may require the use of fungicides. The cost of treatment will also depend on the products used and the size of the affected area. It is best to consult with a local plant specialist or extension agent for specific recommendations for your area and situation.
        """
        }
]


@api_view(['GET', 'POST'])
def singlePrediction(request):
    try:
        BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
        print(colored(0, 0, 255, "Trying to load corn_saved_model..."))
        saved_model = tf.saved_model.load(BASE_DIR / 'corn/models/corn_saved_model')
        print(colored(0, 255, 0, "corn_saved_model loaded successfully"))
    except Exception as e:
        print(colored(255, 0, 0, f"Error loading saved model {str(e)}"))
        
    # receive input image
    if request.method == 'POST':
        # open image file using PIL
        if 'corn-image' in request.FILES:
            image_file = request.FILES['corn-image']
            image = Image.open(image_file)
            image_array = tf.image.resize(np.array(image), [224, 224]) / 255
            image_array = tf.expand_dims(image_array, axis=0)
            predictions = saved_model(image_array)
            print(colored(0, 0, 255, str(predictions)))
            prediction = np.argmax(predictions)
            probabilities = tf.nn.softmax(predictions)
            confidence = 1 # tf.reduce_max(probabilities) * 100
            print(colored(0, 0, 255, f"Confidence \n {str(confidence)} \n {str(type(confidence))}"))
            data = classes[prediction]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = CornSerializer(data)
            return Response(serializer.data)
        else:
            data = {"prediction": 999,
                    "label": "No predicton",
                    "confidence": 0.0,
                    "description": "No description",
                    "value_error": "Either No corn image is provided or It is not labelled, make sure to label with 'corn-image'"}
            serializer = CornSerializer(data)
            return Response(serializer.data)
    elif request.method == 'GET':
        data = {"prediction": 999,
                "label": "No label",
                "confidence": 0.0,
                "description": "No description",
                "value_error": "You are probably not making a POST request, contact concerned personnel for advice"}
        serializer = CornSerializer(data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def multiplePrediction(request):
    pass
