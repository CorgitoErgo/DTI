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


placeholder = st.empty()
placeholder2 = st.empty()
dud_col1, main_col, dud_col2 = st.columns([0.5,4, 0.5])
mehmeh = 0

ser = serial.Serial('COM4', 9600)  # Adjust 'COM4' to your Arduino's serial port    
time.sleep(2)
def arduino_handler():
    
    while True:
        data = ser.readline().decode().strip()
        print(data)
        if data == "A" or data == "B" :
            return data
        
        elif data == "C" or data == "D":
             return data

        else: 
            return "Nothing"

        # st.write(ser.readline().decode().strip())

thread = threading.Thread(target=arduino_handler, daemon=True)
add_script_run_ctx(thread)
thread.start()
global no_of_question_answered, checker
no_of_question_answered = 0

checker = None

def game_question(no_of_qna_answered):
    if no_of_qna_answered == 0:
        return question_template[0]
    elif no_of_qna_answered == 1:
        return question_template[1]
    elif no_of_qna_answered == 2: 
        return question_template[2]
    else: 
        return "You have answered all questions available"


def front_end(no_of_question_answered, panel_display, checker ):
    
    with main_col:
        if checker == None:
                questions = game_question(no_of_question_answered)
                placeholder.title(questions)
        elif checker == True: 
            placeholder.title("You have answer the question correctly. Moving on to the next question......")

        elif checker == False: 
            placeholder.title("You got the answer wrong. Moving on to the next question......")
            

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
                        ], "truth_container",["""
                {
                    
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    

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
            
def answer_checker(input):
    if input == "A" or "D":
        return False  
    else:  
        return True   

def plane_spotting_game(no_of_question_answered, checker):
    while True:
        # global no_of_question_answered, checker
        arduino_output = arduino_handler()
        panel_display = panel(arduino_output)
        print(arduino_output)
        # print(panel_display)
        if arduino_output != "Nothing":
            front_end(no_of_question_answered, panel_display, checker )
            print("hello mehmeh")
            
            time.sleep(15)
            checker =  answer_checker(arduino_output)
            panel_display = panel("Nothing")
            front_end(no_of_question_answered, panel_display, checker )
            time.sleep(15)
            no_of_question_answered =no_of_question_answered + 1
            checker = None
        

        front_end(no_of_question_answered, panel_display, checker )
        # if no_of_question_answered >= 3:

if st.button("Rerun the game"):
    plane_spotting_game(no_of_question_answered = 0, checker = None)

plane_spotting_game(no_of_question_answered, checker)



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