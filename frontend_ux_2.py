import streamlit as st
import tkinter as tk
from tkinter import ttk
import serial
import time #Required to use delay functions
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from streamlit_extras.stylable_container import stylable_container
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
# .big-font {
#     font-size:300px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown('<p class="big-font">Is </p>', unsafe_allow_html=True)
placeholder = st.empty()
placeholder2 = st.empty()
dud_col1, main_col, dud_col2 = st.columns([0.5,4, 0.5])
mehmeh = 0

# ser = serial.Serial('COM4', 9600)  # Adjust 'COM4' to your Arduino's serial port    
# time.sleep(2)
def arduino_handler():
    
    while True:
        data = ser.readline().decode().strip()
        # print(data)
        if data == "A" or data == "B" :
            return data
        
        elif data == "C" or data == "D":
             return data

        else: 
            return "Nothing"

        # st.write(ser.readline().decode().strip())

# thread = threading.Thread(target=arduino_handler, daemon=True)
# add_script_run_ctx(thread)
# thread.start()
no_of_question_answered = 0

def game_question(no_of_qna_answered):
    if no_of_qna_answered == 0:
        return question_template[0]
    elif no_of_qna_answered == 1:
        return question_template[1]
    else:  
        return question_template[2]


def front_end(no_of_question_answered, panel_display ):
    
    with main_col:
            questions = game_question(no_of_question_answered)
            placeholder.title(questions)

    placeholder2.empty()
    with placeholder2.container():
        col1,col2 = st.columns(2)
        with col1:
                with stylable_container(
                    key=panel_display[0],
                    css_styles=panel_display[1]
                    ,
                        
                ):
                    st.markdown(
                        "Step LEFT if you think the answer is TRUE"
                    )
        

        with col2:
            with stylable_container(
            key=panel_display[2],
            css_styles=panel_display[3],
            
            ):
                st.markdown(
                    "Step RIGHT if you think the answer is FALSE"
                )
            
    



def panel(input):
    if input == "Nothing": 
        return "truth_container",["""
                {
                    
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    margin-top: 70px;
                    

                    p{  
                    font-size: 48px;
                    color: black;
                    text-align: center;
                    }
                }""", 
                    """
                        .stMarkdown {
                            padding-right: 1.5em;
                        }
                        """,
                        ], "false_container",["""
                {
                    
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    margin-top: 70px;
                    

                    p{  
                    font-size: 48px;
                    color: black;
                    text-align: center;
                    }
                }""", 
                    """
                        .stMarkdown {
                            padding-right: 1.5em;
                        }
                        """,
                        ],

    elif input == "A" or input == "C":
        return "truth_container",["""
        {
            
            background-color: green;
            padding: 0.5em;
            border-radius: 1em;
            margin-top: 70px;

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
                        ], "false_container",["""
                            {
                                
                                border: 1px solid rgba(49, 51, 63, 0.2);
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px);
                                margin-top: 70px;
                                

                                p{  
                                font-size: 48px;
                                color: black;
                                text-align: center;
                                }
                            }""", 
                                """
                                    .stMarkdown {
                                        padding-right: 1.5em;
                                    }
                                    """,
                                    ],
    elif input == "B" or input == "D":
        return "truth_container",["""
                {
                    
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    margin-top: 70px;
                    

                    p{  
                    font-size: 48px;
                    color: black;
                    text-align: center;
                    }
                }""", 
                    """
                        .stMarkdown {
                            padding-right: 1.5em;
                        }
                        """,
                        ], "false_container",["""
                            {
                                
                                background-color: red;
                                padding: 0.5em;
                                border-radius: 1em;
                                margin-top: 70px;

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
            
        
def plane_spotting_game():
    # while True:
    #     arduino_output = arduino_handler()
        panel_display = panel("B")
    #     print(panel_display)
    #     if panel_display != "Nothing":
    #         for counter in range(10):
    #             front_end(no_of_question_answered, panel_display )
    #             counter += 1
        front_end(no_of_question_answered, panel_display )

plane_spotting_game()
