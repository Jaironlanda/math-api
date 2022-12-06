## Math API

API to generate math questions and answers. Supported math operations include addition, subtraction, ~~division~~ and multiplication.
> NewbAPI Project (https://newbapi.com)

##### Showcase
- ## [Qkmath.com](http://qkmath.com)
![qkmath.com](/assets/showcase-1.png "qkmath.com")


## Basic Usage

### Available Endpoint
- `/question` 
#### Server
- `https://math.newbapi.com/question` (Deta Server)
- `https://api.qkmath.com/question` (official)

### Parameter
- `setting` - `1digit` , `2digit` , `3digit`
- `ops` - `addition`, `substract`, `multiply` 
- `no` - Minimum: `1`, Maximum: `100`
- `qkseed` - random text or number (Optional) 

### Example (cURL)

```bash
curl -X 'GET' \
  'https://api.qkmath.com/question?setting=1digit&ops=addition&no=5&qkseed=abc123' \
  -H 'accept: application/json'
```
### Example (Axios)

```bash
  axios.get('https://api.qkmath.com/question?setting=1digit&ops=addition&no=5&qkseed=abc123')
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

#### Output

```
{
  "data": [
    {
      "op": "addition",
      "question": "0 + 2",
      "answer": 2
    },
    {
      "op": "addition",
      "question": "7 + 5",
      "answer": 12
    },
    {
      "op": "addition",
      "question": "2 + 4",
      "answer": 6
    },
    {
      "op": "addition",
      "question": "1 + 5",
      "answer": 6
    },
    {
      "op": "addition",
      "question": "1 + 8",
      "answer": 9
    }
  ]
}
```
### Run local or self hosting (Docker)

```bash
docker compose build && docker compose up
```

## License

[MIT](https://github.com/Jaironlanda/math-api/blob/main/LICENSE.md)
