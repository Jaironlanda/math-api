from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
from random import sample
import ijson, random


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def loadJson(ques_setting: str, ques_ops: str):
    file_1digit = urlopen('https://raw.githubusercontent.com/Jaironlanda/json-data/main/mathv2/1digit_ques.json')
    file_2digit = urlopen('https://raw.githubusercontent.com/Jaironlanda/json-data/main/mathv2/2digit_ques.json')
    file_3digit = urlopen('https://raw.githubusercontent.com/Jaironlanda/json-data/main/mathv2/3digit_ques_100200.json')
    
    if ques_setting == '1digit':
        load_questions = ijson.items(file_1digit, "item")
        
        if not ques_ops == 'rand':
            question_file = (o for o in load_questions if o["op"] == ques_ops)
            
        else:
            question_file = (o for o in load_questions)
            
    elif ques_setting == '2digit':
        load_questions = ijson.items(file_2digit, "item")
        if not ques_ops == 'rand':
            question_file = (o for o in load_questions if o["op"] == ques_ops)

        else:
            question_file = (o for o in load_questions)

    elif ques_setting == '3digit':
        load_questions = ijson.items(file_3digit, "item")
        
        if not ques_ops == 'rand':
            question_file = (o for o in load_questions if o["op"] == ques_ops)

        else:
            question_file = (o for o in load_questions)

    
    # elif ques_setting == 'rand' and ques_ops == 'rand':
    #     load_questions_1 = ijson.items(file_1digit, "item")
    #     load_questions_2 = ijson.items(file_2digit, "item")
    #     load_questions_3 = ijson.items(file_3digit, "item")
        
    #     question_file_1 = (o for o in load_questions_1)
    #     question_file_2 = (o for o in load_questions_2)
    #     question_file_3 = (o for o in load_questions_3)
        
    #     # print(type(question_file))
    #     question_file = question_file_1 + question_file_2 + question_file_3
    
    return question_file

    # elif ques_setting == 'rand':
    #     # comming soon
    #     temp = []
    #     # take 15 questions each file
    #     # 5/5/5 1 digit (addition, substract, multiply)
    #     # 5/5/5 2 digit (addition, substract, multiply)
    #     # 5/5/5 3 digit (addition, substract, multiply)
    #     list_ques = sample(data_sheet, no)
    #     pass
    
    # load_questions = ijson.items(file_2digit, "item")
    # if not ques_ops == 'rand':
    #     question_file = (o for o in load_questions if o["op"] == ques_ops)
    #     # return question_file
    # else:
    #     question_file = (o for o in load_questions)
    #     # return question_file
    


@app.get("/")
def root():
    return {
        "message": "valid API url 👉🏼 https://math.newbapi.com/question",
        "doc": "📖 https://math.newbapi.com/docs",
        "dev": "Jairon Landa (jaironlanda.com)",
    }


@app.get("/question")
async def get_question(setting: str, ops: str, no: int, qkseed: Optional[str] = None):
    """
        Parameter: \n
        setting - 1digit , 2digit , 3 digit \n
        ops - addition, substract, multiply \n
        no - Minimum: 1, Maximum: 100 \n
        qkseed - random text or number (Optional) \n

        \nExample:\n
        1digit\n
        addition\n
        10\n
        hh214xcw\n
    """
    random.seed(qkseed)
    data = await loadJson(ques_setting=setting, ques_ops=ops)

    data_sheet = []

    for x in data:
        data_sheet.append(dict(x))

    list_ques = sample(data_sheet, no)

    return {"data": list_ques}

