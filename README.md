
## Report by DSI322 Team 2
#### AV David, Anthony Reid, Paul Fenchak

<br>

### Problem Statement

During natural disasters, food donation is crucial to helping survivors. Our team's goal is to determine the usability of a donated food for a disaster relief effort.  We developed a model to predict a donation usability score based on nutrition data plus a storage score to account for storage factores(i.e., lean meats are high in nutrition but do not travel well vs. nuts that are high in nutrition and travel well). In short, we are addressing the problem, **"Which food should be donated to disaster survivors?"**

---

### Target Audience

This project is intended for an audience of non-technical executives.

---

### Executive Summary

We wanted to determine the usability of a donated food for a disaster relief effort. We developed a model to predict a donation usability score based on nutritarian data plus storage factors. The nutrition score was determined by taking the nutrition density of each food based on 12 nutrients including various vitamins, protein, calcium, iron density. [(Source)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489367/) Storage was scored based on shelf life. Nutrition density and storage score were then used to get a donation score. Our recommendation is to consider foods with high shelf life and nutrition to yield a higher score.


---

### File Directory

We have included the following in this report:

- README.md
- requirements.txt
- Data and Code folder
    - data_donation
    - food_score
- Streamlit app folder
    - App code
    - Final dataframe for the app
- Presentation pdf

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**Food Group**|*object*|Food|The type of food|
|**Food Names**|*object*|Food|The food items included|
|**Nutrition Density**|*float*|Food|Nutrition score based on content|
|**Storage**|*float*|Food|Storage score based on shelf life|
|**Donation Score**|*float*|Food|Final score based on nutrient and storage scores|

---

### Conclusions and Recommendations

We created a model that considers food groups and nutrition components of specific foods and returns a donation score. In addition to the model, a streamlit app was developed to show users what the score of their food will be. In this app, a user will specify the food group and type a one word description. The app will then return a table of foods similar to their input and the scores.

---

### References

- Ideas for this project were inspired by this study ["Food selection criteria for disaster response planning in urban societies"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489367/) 
- Sources: USDA National Nutrient Database. Dataworld links are below which we used for the project. 
    - [Old Version Version 1](https://data.world/craigkelly/usda-national-nutrient-db/workspace/file?filename=nndb_flat.csv) 
    - [Updated New Version](https://data.world/awram/food-nutritional-values/workspace/file?filename=ABBREV.xlsx)