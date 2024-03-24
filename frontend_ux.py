import streamlit as st
import serial
import time #Required to use delay functions
import threading
from streamlit_extras.stylable_container import stylable_container
# from streamlit.runtime.scriptrunner import add_script_run_ctx
# from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

# try:
#     from streamlit.scriptrunner import get_script_run_ctx
# except ModuleNotFoundError:
#     # streamlit < 1.8
#     try:
#         from streamlit.script_run_context import get_script_run_ctx  # type: ignore
#     except ModuleNotFoundError:
#         try:
#         # streamlit < 1.4
#             from streamlit.report_thread import (  # type: ignore
#                 get_report_ctx as get_script_run_ctx,
#             )
#         except ModuleNotFoundError:
#             from streamlit.runtime.scriptrunner import add_script_run_ctx

st.set_page_config(
    page_title = ' SkyWatchHub',
    page_icon = '✈️',
    layout = 'wide'
)

question_template = ["Is Singapore Airlines was founded in 1968?", 
                     "Is Singapore Changi Airport consistently ranked as one of the busiest airports in the world?",
                     "Does Singapore Airlines operates the world's longest commercial flight?",
                     "Does Changi Airport have a rooftop swimming pool available for passengers to use?", 
                     "Does Changi Airport have its own butterfly garden?", 
                     "Is Changi Airport the primary hub for AirAsia?",
                     "Does Changi Airport offer a 24-hour complimentary shuttle service between terminals?"
]
question_answer =[False, True, True, True, True, True, True]
st.title("🛬 Welcome to SkyWatchHub")

# st.markdown("""
# <style>
# background:
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown('<p class="big-font">Is </p>', unsafe_allow_html=True)
placeholder = st.empty()
dud_col1, main_col, dud_col2 = st.columns([0.5,4, 0.5])
mehmeh = 0
col1,col2 = st.columns(2)
# ser = serial.Serial('COM4', 9600)  # Adjust 'COM4' to your Arduino's serial port    
# time.sleep(2)
# def arduino_handler():
    
#     while True:
#         data = ser.readline().decode().strip()
#         print(data)
#         if data == "A" or data == "B" :
#             return "mehmeh"
        
#         elif data == "C" or data == "D":
#              return "mehmeh2"

#         st.write(ser.readline().decode().strip())

# thread = threading.Thread(target=arduino_handler, daemon=True)
# add_script_run_ctx(thread)
# thread.start()

with main_col:
        placeholder.title(question_template[0])
with col1:
    with stylable_container(
        key="truth_container",
        css_styles=[
            """
        {
            
            background-color: green;
            padding: 0.5em;
            border-radius: 1em;

            p{
            font-size: 48px;
            color: whitesmoke;
            text-align: center;
            }
        }
        """,
            """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """,
        ],
    ):
        st.markdown(
            "Step LEFT if you think the answer is TRUE"
        )

    



with col2:
     with stylable_container(
        key="false_container",
        css_styles=[
            """
        {
            
            background-color: red;
            padding: 0.5em;
            border-radius: 1em;

            p{
            font-size: 48px;
            color: whitesmoke;
            text-align: center;
            }
        }
        """,
            """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """,
        ],
    ):
        st.markdown(
            "Step RIGHT if you think the answer is FALSE"
        )
    

# sus = arduino_handler()
# if sus == "mehmeh" :
#     placeholder.empty()
#     placeholder.title(question_template[2])

# sus2 = arduino_handler() 

# if sus2 == "mehmeh2":
#     placeholder.empty()
#     placeholder.title(question_template[3])
     
# st.write(sus)
     
            # box_widgets[-1].config(bg="red")
        # elif data == "R2":
            # box_widgets[-3].config(bg="green")
        # else:
        #     for i in box_widgets:
        #         i.config(bg="white")

# if st.button("mehmeh"):
#     placeholder.empty()
#     with main_col:
#         placeholder.title(question_template[1])
#         if st.button("mehmeh2"):
#              placeholder.empty()
#              with main_col:
#                     placeholder.title(question_template[2])
            
# while True:
#     if mehmeh == 0:
#          questions = question_template[1]
        

        

#     elif mehmeh == 1:
#         questions = question_template[2]