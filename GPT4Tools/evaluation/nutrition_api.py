import requests
import json
from pprint import pprint

class NutritionAnalysis:
    base_url = "https://api.edamam.com/api/nutrition-details"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    params = {
        'app_id': "641bd86a",
        'app_key': "9bbec066f338da546a0e164c06183cc3"
    }

    @staticmethod
    def analyze(food_name):
        # Prepare the food details for Edamam API
        food_details = {
            "title": food_name,
            "ingr": [f"1 {food_name}"]
        }

        # Post the food details to Edamam API and return the response
        response = requests.post(NutritionAnalysis.base_url,
                                 headers=NutritionAnalysis.headers,
                                 params=NutritionAnalysis.params,
                                 json=food_details)
        if response.status_code == 200:
            return response.json()
        else:
            return '{}'

if __name__ == '__main__':
    pprint(NutritionAnalysis.analyze('1 slice of pizza'))



"""
    # "How many calories are there in a typical slice of pizza?"
    pizza_nutrition = api.analyze('slice of pizza')
    print(f'Calories in a slice of pizza: {pizza_nutrition["calories"]}')
    
    # "What are the main nutrients in an apple?"
    apple_nutrition = api.analyze('apple')
    print(f'Main nutrients in an apple: {apple_nutrition["totalNutrients"]}')
    
    # "What is the protein content in 100 grams of chicken breast?"
    chicken_breast_nutrition = api.analyze('100 grams chicken breast')
    print(f'Protein in 100 grams of chicken breast: {chicken_breast_nutrition["totalNutrients"]["PROCNT"]}')
    
    # "Could you tell me the number of carbohydrates in a cup of white rice?"
    rice_nutrition = api.analyze('1 cup white rice')
    print(f'Carbohydrates in a cup of white rice: {rice_nutrition["totalNutrients"]["CHOCDF"]}')
    
    # "How much fat is in a medium-sized avocado?"
    avocado_nutrition = api.analyze('medium-sized avocado')
    print(f'Fat in a medium-sized avocado: {avocado_nutrition["totalNutrients"]["FAT"]}')
    
    # "How can I calculate the calories in a homemade lasagna?"
    # You would need to provide the ingredients for the homemade lasagna
    lasagna_nutrition = api.analyze('homemade lasagna')
    print(f'Calories in a homemade lasagna: {lasagna_nutrition["calories"]}')
    
    # "What's the nutritional breakdown of a McDonald's Big Mac?"
    big_mac_nutrition = api.analyze('Big Mac')
    print(f'Nutritional breakdown of a Big Mac: {big_mac_nutrition}')
    
    # "Can you give me the nutrition facts for a serving of sushi?"
    sushi_nutrition = api.analyze('serving of sushi')
    print(f'Nutrition facts for a serving of sushi: {sushi_nutrition}')
    
    # "What's the sugar content in a can of Coke?"
    coke_nutrition = api.analyze('can of Coke')
    print(f'Sugar content in a can of Coke: {coke_nutrition["totalNutrients"]["SUGAR"]}')
    
    # "How much sodium is there in a packet of instant ramen noodles?"
    ramen_nutrition = api.analyze('packet of instant ramen')
    print(f'Sodium content in a packet of instant ramen: {ramen_nutrition["totalNutrients"]["NA"]}')
    
    # "Could you tell me the calorie content of a homemade green smoothie?"
    # You would need to provide the ingredients for the homemade green smoothie
    smoothie_nutrition = api.analyze('homemade green smoothie')
    print(f'Calories in a homemade green smoothie: {smoothie_nutrition["calories"]}')
    
    # "Can you help me calculate the calories in my favorite recipe for chicken tikka masala?"
    # You would need to provide the ingredients for chicken tikka masala
    tikka_nutrition = api.analyze('chicken tikka masala')
    print(f'Calories in chicken tikka masala: {tikka_nutrition["calories"]}')
    
    # "How many calories are there in a cup of quinoa?"
    quinoa_nutrition = api.analyze('1 cup quinoa')
    print(f'Calories in a cup of quinoa: {quinoa_nutrition["calories"]}')
    
    # "How much protein is there in a cup of cooked lentils?"
    lentils_nutrition = api.analyze('1 cup cooked lentils')
    print(f'Protein in a cup of cooked lentils: {lentils_nutrition["totalNutrients"]["PROCNT"]}')
    
    # "Can you tell me about the nutritional values in a serving of baked salmon?"
    salmon_nutrition = api.analyze('serving of baked salmon')
    print(f'Nutritional values in a serving of baked salmon: {salmon_nutrition}')
"""