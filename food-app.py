import streamlit as st

st.title("Food Donation Calculator")
st.header("Wanna know which of the food in your kitchen to donate?")
st.subheader("This is the right place for you!")

food_name= st.text_input('Food', 'Mangoes')
st.write('Food #1 is', food_name)

food_option = st.selectbox(
     'What type of food is food #1',
 ('Dairy and Egg Products', 'Baby Foods', 'Fats and Oils', 'Poultry Products', 'Soups, Sauces, and Gravies', 'Sausages and Luncheon Meats', 'Breakfast Cereals', 'Fruits and Fruit Juices', 'Pork Products', 'Vegetables and Vegetable Products', 'Nut and Seed Products', 'Beef Products', 'Beverages', 'Finfish and Shellfish Products', 'Legumes and Legume Products', 'Lamb, Veal, and Game Products', 'Baked Products', 'Sweets', 'Cereal Grains and Pasta', 'Fast Foods', 'Meals, Entrees, and Side Dishes', 'Snacks', 'American Indian/Alaska Native Foods', 'Restaurant Foods'))

st.write('You selected:', food_option)

option = st.selectbox(
     'How would you like to be contacted?',
 ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
