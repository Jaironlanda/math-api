from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
from random import sample
import ijson


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
        
        if not ques_ops == 'mix':
            question_file = (o for o in load_questions if o["op"] == ques_ops)
            
        else:
            question_file = (o for o in load_questions)

    elif ques_setting == '2digit':
        load_questions = ijson.items(file_2digit, "item")
        if not ques_ops == 'mix':
            question_file = (o for o in load_questions if o["op"] == ques_ops)
            
        else:
            question_file = (o for o in load_questions)
            
    elif ques_setting == '3digit':
        load_questions = ijson.items(file_3digit, "item")
        
        if not ques_ops == 'mix':
            question_file = (o for o in load_questions if o["op"] == ques_ops)
            
        else:
            question_file = (o for o in load_questions)
            
    # elif ques_setting == 'mix':
        # comming soon
        # temp = []
        # take 15 questions each file
        # 5/5/5 1 digit (addition, substract, multiply)
        # 5/5/5 2 digit (addition, substract, multiply)
        # 5/5/5 3 digit (addition, substract, multiply)
        # pass
    

    return question_file


@app.get("/")
def root():
    return {
        "message": "valid API url 👉🏼 https://math.newbapi.com/question",
        "doc": "📖 https://math.newbapi.com/docs",
        "dev": "Jairon Landa (jaironlanda.com)",
    }


@app.get("/question")
async def get_question(setting: str, ops: str, no: int):
    data = await loadJson(ques_setting=setting, ques_ops=ops)
    print(data)
    data_sheet = []

    for x in data:
        data_sheet.append(dict(x))

    list_ques = sample(data_sheet, no)

    return {"data": list_ques}
