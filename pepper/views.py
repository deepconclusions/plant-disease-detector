import pathlib

from plants.props import colored
from plants.props import Model

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
    1: {"prediction": 1, "label": "Healthy", "description": 
        """
        Pepper plants are considered healthy when they are free of diseases, pests, and nutrient deficiencies, and are producing high-quality fruit. Some key factors that contribute to healthy pepper plants include 
        proper watering, good nutrition, pest and disease control, and adequate sunlight and temperature to thrive. Regular monitoring and control measures, such as removing and destroying infected plant debris, can help to prevent damage to the plants. By providing these optimal conditions, pepper plants can grow and produce high-quality fruit.
        """
        },
   }

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

@api_view(['GET', 'POST'])
def singlePrediction(request):
    try:
        model = Model()
        model.load(BASE_DIR / 'pepper/models/pepper_modelv4.h5')
    except Exception as e:
        print(colored(255, 0, 0, f"Error loading saved model {str(e)}"))

    if request.method == 'POST':
        try: 
            image_file = request.FILES['pepper-image']
            image_array = model.process_image(image_file)
            predictions = model.predict(image_array)
            prediction = model.predicted_class(predictions)
            confidence = model.confidence(predictions)
            data = classes[int(prediction)]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = PepperSerializer(data)
            return Response(serializer.data)
        except:
            return Response("Failed to make prediction")
    else:
        return Response("Only post requests are allowed to this endpoint")

def multiplePrediction(request):
    pass