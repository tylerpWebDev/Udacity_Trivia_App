# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
	{
		'1' : "Science",
		'2' : "Art",
		'3' : "Geography",
		'4' : "History",
		'5' : "Entertainment",
		'6' : "Sports"
	}

GET '/questions'
- Fetches all questions and returns a dictionar where the keys are a list of questions, the included categories, the total number of questions as an integer value, and the current category
-Arguments: None
- Example Body:
	{
	  'questions': [{
	    'id': 5,
	    'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
	    'answer': 'Maya Angelou',
	    'category': 'History',
	    'difficulty': 2
	  }, {
	    'id': 9,
	    'question': "What boxer's original name is Cassius Clay?",
	    'answer': 'Muhammad Ali',
	    'category': 'History',
	    'difficulty': 1
	  }, {
	    'id': 2,
	    'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?',
	    'answer': 'Apollo 13',
	    'category': 'Entertainment',
	    'difficulty': 4
	  }, {
	    'id': 4,
	    'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?',
	    'answer': 'Tom Cruise',
	    'category': 'Entertainment',
	    'difficulty': 4
	  }, {
	    'id': 6,
	    'question': 'What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?',
	    'answer': 'Edward Scissorhands',
	    'category': 'Entertainment',
	    'difficulty': 3
	  }, {
	    'id': 10,
	    'question': 'Which is the only team to play in every soccer World Cup tournament?',
	    'answer': 'Brazil',
	    'category': 'Sports',
	    'difficulty': 3
	  }, {
	    'id': 11,
	    'question': 'Which country won the first ever soccer World Cup in 1930?',
	    'answer': 'Uruguay',
	    'category': 'Sports',
	    'difficulty': 4
	  }, {
	    'id': 12,
	    'question': 'Who invented Peanut Butter?',
	    'answer': 'George Washington Carver',
	    'category': 'History',
	    'difficulty': 2
	  }, {
	    'id': 13,
	    'question': 'What is the largest lake in Africa?',
	    'answer': 'Lake Victoria',
	    'category': 'Geography',
	    'difficulty': 2
	  }, {
	    'id': 14,
	    'question': 'In which royal palace would you find the Hall of Mirrors?',
	    'answer': 'The Palace of Versailles',
	    'category': 'Geography',
	    'difficulty': 3
	  }],
	  'categories': ['Science', 'Art', 'Geography', 'History', 'Entertainment', 'Sports'],
	  'total_questions': 10,
	  'current_category': None
	}


DELETE '/questions/<int:question_id>/delete'
- Deletes a single question from the Questions table
- Request Arguments: The ID of the question to be deleted is passed into the endpoint URL
-Returns: The list of all remaining questions is returned as a dictionary  where the keys are a list of remaining questions, the included categories, the total number of questions as an integer value, and the current category
- Example Body: 
	{
	  'questions': [{
	    'id': 5,
	    'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
	    'answer': 'Maya Angelou',
	    'category': 'History',
	    'difficulty': 2
	  }, {
	    'id': 9,
	    'question': "What boxer's original name is Cassius Clay?",
	    'answer': 'Muhammad Ali',
	    'category': 'History',
	    'difficulty': 1
	  }, {
	    'id': 2,
	    'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?',
	    'answer': 'Apollo 13',
	    'category': 'Entertainment',
	    'difficulty': 4
	  }, {
	    'id': 4,
	    'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?',
	    'answer': 'Tom Cruise',
	    'category': 'Entertainment',
	    'difficulty': 4
	  }, {
	    'id': 6,
	    'question': 'What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?',
	    'answer': 'Edward Scissorhands',
	    'category': 'Entertainment',
	    'difficulty': 3
	  }, {
	    'id': 10,
	    'question': 'Which is the only team to play in every soccer World Cup tournament?',
	    'answer': 'Brazil',
	    'category': 'Sports',
	    'difficulty': 3
	  }, {
	    'id': 11,
	    'question': 'Which country won the first ever soccer World Cup in 1930?',
	    'answer': 'Uruguay',
	    'category': 'Sports',
	    'difficulty': 4
	  }, {
	    'id': 12,
	    'question': 'Who invented Peanut Butter?',
	    'answer': 'George Washington Carver',
	    'category': 'History',
	    'difficulty': 2
	  }, {
	    'id': 13,
	    'question': 'What is the largest lake in Africa?',
	    'answer': 'Lake Victoria',
	    'category': 'Geography',
	    'difficulty': 2
	  }, {
	    'id': 15,
	    'question': 'The Taj Mahal is located in which Indian city?',
	    'answer': 'Agra',
	    'category': 'Geography',
	    'difficulty': 2
	  }],
	  'categories': ['Science', 'Art', 'Geography', 'History', 'Entertainment', 'Sports'],
	  'total_questions': 10,
	  'current_category': None
	}


POST '/questions/new'
- Creates a new trivia question in the Questions table of the database
- Request Arguments: The endpoint takes in an object with the keys "question," "answer," "category," and "difficulty" where all values are strings except for "difficulty," which is an integer value.  The endpoint formats this object as an instance of the Question class.
- Returns: A success message is returned as a string upon successfully creating the new record in the database and an error message is returned in the event of a failure.
- Example Response:
	"Success!" appears in text input field on the front end.


POST '/questions/search'
- Uses a string value to return questions containing said value
- Request Arguments: A search term is passed along in the request as a string value.
- Returns: A dictionary is returned with the keys "questions," "total_questions," and "current_category" where "questions" is a list of questions that contain the string value passed in as an argument and "total_questions" is an integer value.
- Example Body:
	{
	  'questions': [{
	    'id': 5,
	    'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
	    'answer': 'Maya Angelou',
	    'category': 'History',
	    'difficulty': 2
	  }],
	  'total_questions': 1,
	  'current_category': None
	}


GET '/categories/<int: category_id>'
- Fetches a list of questions that match a category provided by the user.
- Request Arguments: A category ID is passed into the URL endpoint as an integer
- Returns: A dictionary is returned with the keys "questions," "total_questions," and "current_category" where "questions" is a list of questions that match the category ID passed in as an argument and "total_questions" is an integer value.
- Example Body: 
	{
	  'questions': [{
	    'id': 20,
	    'question': 'What is the heaviest organ in the human body?',
	    'answer': 'The Liver',
	    'category': 'Science',
	    'difficulty': 4
	  }, {
	    'id': 21,
	    'question': 'Who discovered penicillin?',
	    'answer': 'Alexander Fleming',
	    'category': 'Science',
	    'difficulty': 3
	  }, {
	    'id': 22,
	    'question': 'Hematology is a branch of medicine involving the study of what?',
	    'answer': 'Blood',
	    'category': 'Science',
	    'difficulty': 4
	  }, {
	    'id': 63,
	    'question': 'This is a test',
	    'answer': 'This is a test',
	    'category': 'Science',
	    'difficulty': 1
	  }],
	  'categories': ['Science', 'Art', 'Geography', 'History', 'Entertainment', 'Sports'],
	  'total_questions': 4,
	  'current_category': None
	}


POST '/quizzes'
- Fetches a list of questions matching the category selected by the user.
- Request Arguments: A category ID is passed along in the request which is used to filter a list of questions that match said ID.
- Returns: Questions that match the category ID provided in the request are returned one at a time, allowing the user to answer them.  Once a question has been answered it is appended to a list, which is then used to prevent the same question from appearing more than once.
- Example Body:
	{
	  'question': {
	    'id': 63,
	    'question': 'This is a test',
	    'answer': 'This is a test',
	    'category': 1,
	    'difficulty': 1
	  },
	  'categories': ['Science', 'Art', 'Geography', 'History', 'Entertainment', 'Sports']
	}



```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```