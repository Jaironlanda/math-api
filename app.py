from fastapi import FastAPI
from urllib.request import urlopen
from random import sample
import ijson


app = FastAPI()

async def loadJson(q_lvl: str, q_op: str = None):
  file = urlopen(url="https://raw.githubusercontent.com/Jaironlanda/json-data/main/math/question.json")
  
  load_questions = ijson.items(file, 'item')
  
  if q_lvl == 'mix' and q_op == 'mix':
    question_file = (o for o in load_questions)
  elif q_lvl == 'mix':
    question_file = (o for o in load_questions if o['op'] == q_op)
  elif q_op == 'mix':
    question_file = (o for o in load_questions if o['level'] == q_lvl)
  else:
    question_file = (o for o in load_questions if o['level'] == q_lvl and o['op'] == q_op)

  return question_file


@app.get('/question')
async def get_question(no_ques: int, level: str = 'mix', op: str = 'mix'):
  data = await loadJson(q_lvl=level, q_op=op)

  data_sheet = []

  for x in data:
    data_sheet.append(dict(x))

  list_ques = sample(data_sheet, no_ques)

  return {'data': list_ques}
