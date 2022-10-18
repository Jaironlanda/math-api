## Math API

This API is develop for education purpose only. 

## Basic Usage

### Available Endpoint

- `/question` or `https://math.newbapi.com/question`

### Parameter

- `no_ques` : required `integer` only.
- `level`: difficulty of question. Available parameter:  `easy`, `medium`, and `hard`. Default is `mix`
- `op`: operation of question. available parameters:  `addition`, `multiply`,`substract` and `division`. Default is `mix`

### Example Usage (Basic)

```bash
curl -X 'GET' \
  'https://math.newbapi.com/question?no_ques=10&level=mix&op=mix' \
  -H 'accept: application/json'
```

#### Output

```
{
  "data": [
    {
      "op": "multiply",
      "level": "medium",
      "question": "33 X 85",
      "answer": 2805
    },
    {
      "op": "substract",
      "level": "easy",
      "question": "5 - 56",
      "answer": -51
    },
    {
      "op": "substract",
      "level": "hard",
      "question": "98 - 89",
      "answer": 9
    },
    ...
    ....
  ]
}
```

### Example Usage (Axios)

```bash
  axios.get('https://math.newbapi.com/question?no_ques=10&level=mix&op=mix')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
```

### Run local or self hosting (Docker)

```bash
docker compose build && docker compose up
```

# NewbAPI Project (https://newbapi.com)