import streamlit as st
import pandas as pd
from PIL import Image
import uuid
import os

IMAGES_DIR = "plane_cartoon.jpg"

# st.set_page_config(
#     page_title = ' SkyWatchHub',
#     page_icon = '✈️',
#     layout = 'wide'
# )
# def save_image(image_data):
#     image_id = str(uuid.uuid4())
#     image_path = os.path.join(IMAGES_DIR, f"{image_id}.png")
#     image_data.save(image_path)
#     return st.experimental_get_server_url() + image_path
# # "C:\\Users\\Rald999\\Documents\\GitHub\\Keyword_Generator_and_Translator\\DTI\\plane_cartoon.jpg"
# image = Image.open("plane_cartoon.jpg")
# image_url = save_image(image)



page_bg_image = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://lh3.googleusercontent.com/pw/AP1GczNDopwibjriOhDpSa1_WZEcbf0Ug1KhUWfwtGOAZQnjLLA_9TfEcwSaj1v8TUFJd8wqcJpedE6IGNH0osRLrB3ZYJKUv6SsCFw9Oj3UBnRyv-UEpIOdoIPeMSGfY2FQpFn7Cd0imW6pkjZBcLDKLhOWmw=w879-h879-s-no-gm");
background-repeat: no-repeat;
    background-size: cover;
}

</style>

"""
st.markdown(page_bg_image, unsafe_allow_html= True)
plane_data = pd.read_csv("plane_data.csv")
plane_data_departure = pd.read_csv("plane_data_departure.csv")

plane_data["arrival_scheduled"] = pd.to_datetime(plane_data["arrival_scheduled"])
plane_data_departure["departure_estimated"] = pd.to_datetime(plane_data_departure["departure_estimated"])
plane_data["timeline"] = plane_data["arrival_scheduled"].dt.time
plane_data_departure['timeline'] = plane_data_departure["departure_estimated"].dt.time
plane_data["direction"] = "Arriving at Changi"
plane_data_departure["direction"] = "Departing from Changi"
data1 = plane_data[["airline_name","timeline","direction"]]
data2 = plane_data_departure[["airline_name","timeline","direction"]]
df = pd.concat([data1,data2])
df = df.sort_values(by=['timeline'])

st.title("🛬 Welcome to SkyWatchHub")

placeholder = st.empty()
placeholder2 = st.empty()

dud_col1, main_col, dud_col2 = st.columns([1,6, 1])
with dud_col1:
        for x in range(5):
            st.title(":drum_with_drumsticks:")


with dud_col2:
        for x in range(5):
            st.title(":drum_with_drumsticks:")


with main_col:
            planename = plane_data_departure["airline_name"][0]
            planename2 = plane_data_departure["airline_name"][1]
            planename3 = plane_data_departure["airline_name"][2]
            planetimeline = plane_data_departure['timeline'][0]
            mehmeh = f"{planename}, {planename2},{planename3} plane is gonna pass by at around {planetimeline}"
            st.title("LOOK UP!!!!!!")
            st.title(mehmeh)
            st.title("Hit the drums to light up the surroundings!!!")
            col1,col2 = st.columns(2)
            with col1:
                st.dataframe(data1.head())
            with col2:
                st.dataframe(data2.head())
            