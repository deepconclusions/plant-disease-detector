import pathlib

from plants.props import colored
from plants.props import Model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TomatoSerializer


classes = [
    {"prediction": 0, "label": "Bacterial spot", "description": 
     """
     Tomato bacterial spot is a common plant disease caused by the bacterium Xanthomonas campestris pv. vesicatoria. It can cause significant damage to tomato plants and reduce yields if left untreated.
     Symptoms of bacterial spot on tomato plants include dark, water-soaked lesions on leaves, stems, and fruit. These lesions may enlarge and turn brown, and the affected tissue may become sunken. Leaves may also develop yellow halos around the lesions, and they may eventually drop from the plant. In severe cases, the fruit may be disfigured, with raised, scabby lesions that make it unsuitable for market.
     To manage bacterial spot in tomato plants, it is important to use disease-free seed and transplants, rotate crops to prevent the buildup of the bacteria in the soil, and avoid overhead watering, as wet leaves can facilitate the spread of the disease. Copper-based fungicides can also be applied to protect plants from infection. However, it is important to note that once a plant is infected with bacterial spot, there is no cure, and infected plants should be removed and destroyed to prevent the spread of the disease to other plants.
     """
     },
    {"prediction": 1, "label": "Early blight", "description": 
     """
     Tomato early blight is a common fungal disease caused by the fungus Alternaria solani. It can cause significant damage to tomato plants and reduce yields if left untreated.
     Symptoms of early blight on tomato plants usually start as small, dark spots on the lower leaves, which may eventually enlarge and develop a concentric ring pattern, giving them a target-like appearance. The spots may also have yellow halos around them, and the leaves may begin to yellow and wilt. As the disease progresses, it can affect the stems and fruit, causing them to develop dark, sunken lesions.
     To manage early blight in tomato plants, it is important to use disease-free seed and transplants, rotate crops to prevent the buildup of the fungus in the soil, and practice good sanitation by removing and destroying infected plant debris. Fungicides can also be applied to protect plants from infection, but they should be used as part of an integrated pest management program and rotated to prevent the development of resistance.
     Cultural practices, such as proper plant spacing and pruning, can also help to reduce the severity of early blight by improving air circulation and reducing humidity around the plants. It is important to note that while early blight can cause significant damage to tomato plants, it is rarely fatal and can be managed with proper prevention and treatment measures.
     """
     },
    {"prediction": 2, "label": "Late blight", "description": 
     """
     Tomato late blight is a destructive fungal disease caused by the oomycete Phytophthora infestans. It can cause significant damage to tomato plants and reduce yields if left untreated.
    Symptoms of late blight on tomato plants include dark, water-soaked lesions on leaves, stems, and fruit. These lesions may quickly enlarge and become brown and necrotic, and the affected tissue may become soft and mushy. Leaves may also curl and die, and the fruit may rot and become covered in a white, fuzzy mold. In humid conditions, the underside of the leaves may develop a downy mildew-like growth of the pathogen.
    To manage late blight in tomato plants, it is important to use disease-free seed and transplants, rotate crops to prevent the buildup of the fungus in the soil, and practice good sanitation by removing and destroying infected plant debris. Fungicides can also be applied to protect plants from infection, but they should be used preventively before the disease occurs, as late blight can spread rapidly and be difficult to control once it has established.
    Cultural practices, such as proper plant spacing and pruning, can also help to reduce the severity of late blight by improving air circulation and reducing humidity around the plants. It is important to note that late blight can be a serious and difficult-to-control disease, and early detection and prevention are key to minimizing its impact on tomato crops.
     """
     },
    {"prediction": 3, "label": "Leaf Mold", "description": 
     """
     Tomato leaf mold is a fungal disease caused by the pathogen Passalora fulva (formerly known as Fulvia fulva). It is a common disease of tomato plants, particularly in areas with high humidity and warm temperatures.
    Symptoms of tomato leaf mold include yellow spots on the upper surface of the leaves, which may eventually develop a velvety, grayish-white growth on the underside of the leaves. The leaves may also become distorted and may eventually die and drop from the plant. The fruit is not usually affected by the disease.
    To manage tomato leaf mold, it is important to provide good air circulation around the plants by spacing them properly and avoiding overhead watering, which can promote the growth and spread of the fungus. Fungicides can also be applied to protect plants from infection, but they should be used preventively before the disease occurs, as leaf mold can spread rapidly and be difficult to control once it has established.
    Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of leaf mold. It is important to note that while leaf mold can cause significant damage to tomato plants, it is rarely fatal and can be managed with proper prevention and treatment measures.
     """
     },
    {"prediction": 4, "label": "Septoria leaf spot", "description": 
     """
     Tomato septoria leaf spot is a common fungal disease caused by the pathogen Septoria lycopersici. It is one of the most destructive diseases of tomato plants and can cause significant damage to leaves, stems, and fruit, leading to reduced yields.
    Symptoms of septoria leaf spot on tomato plants include small, circular lesions with dark brown centers and yellowish halos on the leaves. As the disease progresses, the lesions may merge, causing the leaves to turn yellow and eventually drop from the plant. The fruit is usually not affected by the disease.
    To manage septoria leaf spot, it is important to provide good air circulation around the plants by spacing them properly and avoiding overhead watering, which can promote the growth and spread of the fungus. Fungicides can also be applied to protect plants from infection, but they should be used preventively before the disease occurs, as septoria leaf spot can spread rapidly and be difficult to control once it has established.
    Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of the disease. In addition, planting resistant varieties can help to reduce the risk of infection. It is important to note that while septoria leaf spot can cause significant damage to tomato plants, it can be managed with proper prevention and treatment measures.
     """
     },
    {"prediction": 5, "label": "Spider mites, Two-spotted spider mite", "description": 
     """
     Two-spotted spider mites are tiny, sap-sucking pests that can cause significant damage to tomato plants. They are typically found on the undersides of leaves and can reproduce rapidly in hot, dry conditions.
    Symptoms of two-spotted spider mite infestation on tomato plants include yellowing and stippling of leaves, which may eventually turn brown and fall from the plant. The mites themselves are usually not visible to the naked eye, but they can be seen with a magnifying glass as small, reddish or greenish dots on the undersides of leaves.
    To manage two-spotted spider mites on tomato plants, it is important to provide good air circulation around the plants by spacing them properly and avoiding overhead watering, which can promote the growth and spread of the mites. Insecticidal soap, neem oil, and other insecticides can also be applied to control mites, but they should be used as part of an integrated pest management program and rotated to prevent the development of resistance.
    Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of mite infestations. In addition, introducing natural predators, such as predatory mites or lacewings, can help to control two-spotted spider mites. It is important to note that early detection and prevention are key to minimizing the impact of two-spotted spider mites on tomato crops, as severe infestations can cause significant damage to plants and reduce yields.
     """
     },
    {"prediction": 6, "label": "Target Spot", "description": 
     """
     Tomato target spot is a fungal disease caused by the pathogen Corynespora cassiicola. It is a common disease of tomato plants, particularly in warm, humid conditions.
    Symptoms of tomato target spot include circular or oval-shaped spots on the leaves, with a dark brown or black center and a yellow or brown halo. The spots may also develop a characteristic "target" pattern, with concentric rings of different colors. As the disease progresses, the spots may merge, causing the leaves to turn yellow and eventually drop from the plant. The fruit may also develop lesions, which can reduce yield and quality.
    To manage tomato target spot, it is important to provide good air circulation around the plants by spacing them properly and avoiding overhead watering, which can promote the growth and spread of the fungus. Fungicides can also be applied to protect plants from infection, but they should be used preventively before the disease occurs, as target spot can spread rapidly and be difficult to control once it has established.
    Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of target spot. In addition, planting resistant varieties can help to reduce the risk of infection. It is important to note that while target spot can cause significant damage to tomato plants, it can be managed with proper prevention and treatment measures.
     """
     },
    {"prediction": 7, "label": "Tomato Yellow Leaf Curl Virus", "description": 
     """
     Tomato Yellow Leaf Curl Virus (TYLCV) is a viral disease that can cause significant damage to tomato plants. It is transmitted by whiteflies, which feed on the plant's sap and spread the virus from infected plants to healthy ones.
    Symptoms of TYLCV on tomato plants include yellowing and curling of leaves, stunted growth, and reduced yields. Infected plants may also develop a characteristic "V" shape or upward curling of the leaves. The symptoms of TYLCV can be similar to other diseases or nutrient deficiencies, so laboratory testing may be needed to confirm the diagnosis.
    To manage TYLCV in tomato plants, it is important to control whitefly populations by using insecticides or introducing natural predators, such as ladybugs or parasitic wasps. The use of reflective mulches, such as aluminum foil or white plastic, can also help to repel whiteflies and reduce the spread of the virus.
    Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of TYLCV. In addition, planting resistant varieties can help to reduce the risk of infection. It is important to note that while TYLCV can cause significant damage to tomato plants, it can be managed with proper prevention and treatment measures.
     """
     },
    {"prediction": 8, "label": "Mosaic virus", "description": 
     """
     Mosaic virus is a viral disease that can affect a wide range of plants, including tomatoes. The virus is usually spread by insect vectors, such as aphids, or through contaminated tools or plant material.
    Symptoms of mosaic virus on tomato plants can vary depending on the severity of the infection and the type of virus involved. In general, the most common symptoms include mottling, yellowing, and distortion of the leaves, as well as stunted growth and reduced yields. The fruit may also develop irregular coloring or streaking.
    To manage mosaic virus in tomato plants, it is important to control insect vectors by using insecticides or introducing natural predators, such as ladybugs or parasitic wasps. Cultural practices, such as removing and destroying infected plant debris and avoiding working with wet plants, can also help to reduce the severity of the disease. In addition, planting resistant varieties can help to reduce the risk of infection.
    Unfortunately, there are no effective treatments for mosaic virus in tomato plants once they are infected. It is important to remove and destroy infected plants as soon as possible to prevent the virus from spreading to healthy plants. Preventing the disease from occurring in the first place through good sanitation practices and the use of resistant varieties is the best approach to managing mosaic virus in tomato plants.
     """
     },
    {"prediction": 9, "label": "Healthy", "description": 
     """
     Tomato plants are considered healthy when they are free of diseases, pests, and nutrient deficiencies, and are producing high-quality fruit. Some key factors that contribute to healthy pepper plants include 
    proper watering, good nutrition, pest and disease control, and adequate sunlight and temperature to thrive. Regular monitoring and control measures, such as removing and destroying infected plant debris, can help to prevent damage to the plants. By providing these optimal conditions, pepper plants can grow and produce high-quality fruit.
     """
     },
]

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
try:
    model = Model()
    model.load(BASE_DIR / 'tomato/models/tomato_modelv2.h5')
except Exception as e:
    print(colored(255, 0, 0, f"Error loading saved model {str(e)}"))

@api_view(['GET', 'POST'])
def singlePrediction(request):
    if request.method == 'POST':
        try: 
            image_file = request.FILES['tomato-image']
            image_array = model.process_image(image_file)
            predictions = model.predict(image_array)
            prediction = model.predicted_class(predictions)
            confidence = model.confidence(predictions)
            data = classes[int(prediction)]
            data["confidence"], data["value_error"] = confidence, "No errors caught"
            serializer = TomatoSerializer(data)
            return Response(serializer.data)
        except:
            return Response("Failed to make prediction")
    else:
        return Response("Only POST requests are allowed to this endpoint")

@api_view(['GET', 'POST'])
def multiplePrediction(request):
    pass
