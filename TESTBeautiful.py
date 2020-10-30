from bs4 import BeautifulSoup

import requests

#strip function
def stripdata(data):
  data= data.string
  data= data.strip()
  return data


RecipeUrl = 'https://www.allrecipes.com/recipe/22281/black-bottom-cupcakes-ii/'


allrecipes = requests.get(RecipeUrl)

soup = BeautifulSoup(allrecipes.text, 'lxml')

tittle=soup.h1.string

URL = RecipeUrl

#Time 

TimePrep = soup.find_all(class_="recipe-meta-item-body")[0]
TimeCook = soup.find_all(class_="recipe-meta-item-body")[1]
TimeTotal = soup.find_all(class_="recipe-meta-item-body")[2]

TimePrep =  stripdata(TimePrep)
TimeCook = stripdata(TimeCook)
TimeTotal = stripdata(TimeTotal)

# Servings and Amount per recipe

Servings = soup.find_all(class_="recipe-meta-item-body")[3]

Servings = stripdata(Servings)

ingredient1 = soup.find_all(class_="ingredients-item-name")[0]
lenght = soup.find_all(class_="ingredients-item-name")


ingredient1 = stripdata(ingredient1)
# Ingredients

i=0
for i in lenght:
 stripdata(i) 
 print(stripdata(i))

   

print(URL)
print
print(tittle)
print    
print(TimePrep)
print  
print(TimeCook)
print  
print(TimeTotal)
print  
print(Servings)
print
print(ingredient1)

