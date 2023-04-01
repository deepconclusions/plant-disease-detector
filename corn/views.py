import pathlib
from plants.props import colored
from plants.props import Model
from django.views.defaults import bad_request, server_error

# django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CornSerializer


# Create your views here.
classes = [{"prediction": 0, 
        "label": "Cercospora", 
        "description": """
        Cercospora is a fungal genus that can cause leaf spot diseases in a wide range of plants, including vegetables, fruits, and ornamental plants. The disease appears as small, circular spots on leaves that can range in color from gray to brown to purple. As the disease progresses, the spots may enlarge and merge, causing the leaves to turn yellow and eventually die off.
        Cercospora leaf spot can be controlled through a combination of cultural, chemical, and biological methods. Cultural methods include removing and destroying infected plant material, planting disease-resistant varieties, and practicing good sanitation in the garden. Chemical control involves using fungicides to prevent the spread of the disease, and biological control involves introducing natural predators or beneficial microorganisms to the affected area.
        The length of time and cost to treat Cercospora will depend on the severity of the disease and the size of the affected area. Mild cases can often be controlled through cultural methods alone, while more severe cases may require a combination of cultural and chemical methods. The cost of treatment will also vary depending on the products used and the size of the affected area. It is best to consult with a local plant specialist or extension agent for specific recommendations for your area and situation.
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

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
try:
    model = Model()
    model.load(BASE_DIR / 'corn/models/corn_modelv4.h5')
except Exception as e:
    print(colored(255, 0, 0, f"Error loading saved model {str(e)}"))

@api_view(['GET', 'POST'])
def singlePrediction(request):
    if request.method == 'POST':
        try: 
            image_file = request.FILES['corn-image']
            image_array = model.process_image(image_file)
            predictions = model.predict(image_array)
            prediction = model.predicted_class(predictions)
            confidence = model.confidence(predictions)
            data = classes[int(prediction)]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = CornSerializer(data)
            return Response(serializer.data)
        except:
            return Response("Failed to make prediction")
    else:
        return Response("Only post requests are allowed to this endpoint")

@api_view(['GET', 'POST'])
def multiplePrediction(request):
    pass
