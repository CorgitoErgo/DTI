question_template = ["Is Singapore Airlines was founded in 1968?", 
                     "Is Singapore Changi Airport consistently ranked as one of the busiest airports in the world?",
                     "Does Singapore Airlines operates the world's longest commercial flight?",
                     "Does Changi Airport have a rooftop swimming pool available for passengers to use?", 
                     "Does Changi Airport have its own butterfly garden?", 
                     "Is Changi Airport the primary hub for AirAsia?",
                     "Does Changi Airport offer a 24-hour complimentary shuttle service between terminals?"
]
question_answer =[False, True, True, True, True, True, True]


def game_question(no_of_qna_answered):
    if no_of_qna_answered == 0:
        return question_template[0]
    elif no_of_qna_answered == 1:
        return question_template[1]
    else:  
        return question_template[2]