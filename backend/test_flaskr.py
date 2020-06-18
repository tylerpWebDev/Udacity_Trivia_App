import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import custom_functions as cfunc

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
                        "question": "This is a test question",
                        "answer": "This is a test answer",
                        "category": 1, 
                        "difficulty": 3
                        }


    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET ALL QUESTIONS  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_get_questions(self):
        res = self.client().get("/questions")
        data = [json.loads(res.data)]

        self.assertTrue(len(data) > 0)
        self.assertEqual(res.status_code, 200)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET ALL CATEGORIES  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_get_categories(self):
        res = self.client().get("/categories")
        data = [json.loads(res.data)]
        cat = data[0]["categories"]

        self.assertTrue(len(cat) > 3)
        self.assertEqual(res.status_code, 200)


    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  POST NEW QUESTION  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def test_post_new_question(self):
        res = self.client().post("/questions/new", json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res != None)
        self.assertTrue(data["data"] == 'Question was successfully posted!')

    def test_post_new_question_negative(self):
        res = self.client().post("/questions/new", json={})
        self.assertEqual(res.status_code, 404)

    def test_post_wrong_route_negative(self):
        res = self.client().post("/questions", json=self.new_question)
        self.assertEqual(res.status_code, 405)



    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  SEARCH FOR A QUESTION  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_search_for_questions(self): 
      searchData = {"searchTerm": "which"} 
      res = self.client().post("/questions/search", json=searchData)
      data = json.loads(res.data)
      ques = data["questions"]
  
      self.assertEqual(res.status_code, 200)
      self.assertTrue(res.data != None)
      self.assertTrue(len(ques) > 0)

    def test_search_for_questions_negative(self): 
      searchData = {"searchTerm": "asdfasdafsadfasdf"} 
      res = self.client().post("/questions/search", json=searchData)
      data = json.loads(res.data)
      ques = data["questions"]
  
      self.assertEqual(res.status_code, 200)
      self.assertTrue(res.data != None)
      self.assertTrue(len(ques) == 0)


    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  DELETE QUESTION  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_delete_a_question(self):
        all_questions = [item.format() for item in Question.query.all()]
        all_ids = []
        
        for x in all_questions:
            all_ids.append(x["id"])

        latest_id = max(all_ids)
        delete_url = '/questions/' + str(latest_id) + '/delete'
        res = self.client().delete(delete_url)
        check_question_existence = Question.query.get(latest_id)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(check_question_existence, None)
  
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET QUESTIONS BY CATEGORY  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_get_questions_by_category_1(self):
        request_url = '/categories/1'
        res = self.client().get(request_url)
        data = json.loads(res.data)
        ques = data["questions"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(ques) > 0)

    def test_get_questions_by_category_2(self):
        request_url = '/categories/2'
        res = self.client().get(request_url)
        data = json.loads(res.data)
        ques = data["questions"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(ques) > 0)

    def test_get_questions_by_category_3(self):
        request_url = '/categories/3'
        res = self.client().get(request_url)
        data = json.loads(res.data)
        ques = data["questions"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(ques) > 0)

    def test_get_questions_by_category_negative(self):
        request_url = '/categories/32934723957349538746286'
        res = self.client().get(request_url)
        data = json.loads(res.data)
        ques = data["questions"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(ques) == 0)
        self.assertTrue(data["total_questions"] == 0)

  
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  PLAY QUIZ  ++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_play_quiz_category_1(self):
        res = self.client().post("/quizzes", json={'previous_questions': [], 'quiz_category': 1})
        data = json.loads(res.data)
        ques = data["question"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(ques != None)
        self.assertTrue(ques["category"] == 1)

    def test_play_quiz_category_2(self):
        res = self.client().post("/quizzes", json={'previous_questions': [], 'quiz_category': 2})
        data = json.loads(res.data)
        ques = data["question"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(ques != None)
        self.assertTrue(ques["category"] == 2)

    def test_play_quiz_category_3(self):
        res = self.client().post("/quizzes", json={'previous_questions': [], 'quiz_category': 3})
        data = json.loads(res.data)
        ques = data["question"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(ques != None)
        self.assertTrue(ques["category"] == 3)

    def test_play_quiz_category_4(self):
        res = self.client().post("/quizzes", json={'previous_questions': [], 'quiz_category': 4})
        data = json.loads(res.data)
        ques = data["question"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(ques != None)
        self.assertTrue(ques["category"] == 4)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()