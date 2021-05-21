import streamlit as st
import pandas as pd

st.title("Food Donation Scorer")
st.header("Should you donate your food?")
st.subheader("Please input information about your food below.")
st.text("")

food_name= st.text_input('What is the food item?', '')
st.write('You entered', food_name)

df=pd.read_csv('final.csv',index_col=0)

word=food_name
index_list=[]
for indx,item in enumerate(df['Food Names']):
    if word.lower() in item.lower():
        index_list.append(indx)
new_df = df.loc[index_list,:]
new_df

show_df = st.checkbox("Would you like to filter by food group?")

if show_df:
    food_option = st.selectbox('What is the type of food?',
 ('American Indian/Alaska Native Foods',
 'Baby Foods',
 'Baked Products',
 'Beef Products',
 'Beverages',
 'Breakfast Cereals',
 'Cereal Grains and Pasta',
 'Dairy and Egg Products',
 'Fast Foods',
 'Fats and Oils',
 'Finfish and Shellfish Products',
 'Fruits and Fruit Juices',
 'Lamb, Veal, and Game Products',
 'Legumes and Legume Products',
 'Meals, Entrees, and Side Dishes',
 'Nut and Seed Products',
 'Pork Products',
 'Poultry Products',
 'Restaurant Foods',
 'Sausages and Luncheon Meats',
 'Snacks',
 'Soups, Sauces, and Gravies',
 'Spices and Herbs',
 'Sweets',
 'Vegetables and Vegetable Products'))

    filtered_df = new_df[new_df['Food Group']==food_option]
    filtered_df

st.subheader("Our Guidelines:")
st.text("If the donation score is 3.5 or higher, we recommend donating your food.")
st.text("If the donation score is less than 3.5, we do NOT recommend donating.")