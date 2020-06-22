import os
from flask import Flask, request, abort, jsonify
from flask import redirect, url_for, Response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
import custom_functions as cfunc
import json

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db = SQLAlchemy(app)

    @app.after_request
    def add_cors_headers(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, PUT, POST, PATCH, DELETE, OPTIONS')
        return response

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET ALL CATEGORIES - COMPLETED  ++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route('/categories')
    @cross_origin()
    def all_categories():
        all_categories = [item.format() for item in Category.query.all()]
        cat_list = []
        for x in all_categories:
            cat_list.append(x["type"])
        formatted_response = {
            "question": "",
            "answer": "",
            "difficulty": 1,
            "category": 1,
            "categories": cat_list
        }
        return jsonify(formatted_response)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET ALL QUESTIONS  ++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route('/questions')
    @cross_origin()
    def all_questions():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10
        all_categories = [item.format() for item in Category.query.all()]
        all_questions = [item.format() for item in Question.query.all()]
        paginated_questions = all_questions[start:end]
        categories_list = []
        for x in all_categories:
            categories_list.append(x["type"])

        formatted_questions = {
            "questions": paginated_questions,
            "categories": categories_list
        }

        for x in formatted_questions["questions"]:
            category_name = Category.query.get(x["category"])
            x["category"] = str(category_name.type)

        formatted_questions["total_questions"] = len(
            formatted_questions["questions"])
        formatted_questions["current_category"] = None
        return jsonify(formatted_questions)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  DELETE QUESTION - COMPLETED  +++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route('/questions/<int:question_id>/delete',
               methods=["DELETE", "GET"])
    @cross_origin()
    def delete_question(question_id):

        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            Question.query.get(question_id).delete()
            db.session.commit()
            flash('Question has been successfully deleted!')
        except BaseException:
            db.session.rollback()
            flash('There was an error deleting this question.')
        finally:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            all_categories = [item.format() for item in Category.query.all()]
            all_questions = [item.format() for item in Question.query.all()]
            paginated_questions = all_questions[start:end]
            categories_list = []
            for x in all_categories:
                categories_list.append(x["type"])

            formatted_questions = {
                "questions": paginated_questions,
                "categories": categories_list
            }

            for x in formatted_questions["questions"]:
                category_name = Category.query.get(x["category"])
                x["category"] = str(category_name.type)

            formatted_questions["total_questions"] = len(
                formatted_questions["questions"])
            formatted_questions["current_category"] = None
            return jsonify(formatted_questions)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  POST NEW QUESTION - COMPLETED  +
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route("/questions/new", methods=["POST"])
    @cross_origin()
    def create_question():
        res_data = json.loads(request.data.decode("utf-8"))
        try:
            category = Category.query.filter(
                Category.id == int(res_data["category"])).all()
            format_cat = [item.format() for item in category]

            new_question = Question(
                question=res_data["question"],
                answer=res_data["answer"],
                category=format_cat[0]["id"],
                difficulty=res_data["difficulty"]
            )
        except Exception as e:
            print(e)
            print("Missing required question data. Is this a negative test?")

        try:
            db.session.add(new_question)
            db.session.commit()
            return jsonify({"data": "Question was successfully posted!"})
        except Exception as e:
            db.session.rollback()
            cfunc.cprint("Error", e)
            abort(404)
        finally:
            db.session.close()

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  SEARCH FOR A QUESTION - COMPLETED  +
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route('/questions/search', methods=["POST"])
    @cross_origin()
    def search_for_questions():
        try:
            search_term = json.loads(request.data.decode("utf-8"))
            search_term = str(search_term["searchTerm"])

            all_questions = [item.format() for item in Question.query.all()]
            all_categories = [item.format() for item in Category.query.all()]
            filtered_questions = []

            for x in all_questions:
                if search_term.lower() in x["question"].lower():
                    cat_id = Category.query.get(int(x["category"]))
                    x["category"] = cat_id.type
                    filtered_questions.append(x)

            formatted_response = {
                "questions": filtered_questions,
                "total_questions": len(filtered_questions),
                "current_category": None
            }


            return jsonify(formatted_response)
        except Exception as e:
            cfunc.cprint("Error", e)
            abort(404)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  GET QUESTIONS BY CATEGORY - COMPLETE
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route('/categories/<int:category_id>', methods=["GET"])
    @cross_origin()
    def single_category(category_id):
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            all_categories = [item.format() for item in Category.query.all()]
            all_questions = [
                item.format() for item in Question.query.filter(
                    Question.category == category_id).all()]
            paginated_questions = all_questions[start:end]
            categories_list = []
            for x in all_categories:
                categories_list.append(x["type"])

            formatted_questions = {
                "questions": paginated_questions,
                "categories": categories_list
            }

            for x in formatted_questions["questions"]:
                category_name = Category.query.get(x["category"])
                x["category"] = str(category_name.type)

            formatted_questions["total_questions"] = len(
                formatted_questions["questions"])
            formatted_questions["current_category"] = None
            return jsonify(formatted_questions)
        except Exception as e:
            cfunc.cprint("Error", e)
            abort(404)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     ++++++++++++++++++++++++++++++  PLAY QUIZ - COMPLETED  +
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @app.route("/quizzes", methods=["GET", "POST"])
    @cross_origin()
    def quizzes():
        try:
            data = json.loads(request.data.decode("utf-8"))
            category_id = data["quiz_category"]
            previous_questions = data["previous_questions"]

            all_categories = [item.format() for item in Category.query.all()]
            all_questions = [
                item.format() for item in Question.query.filter(
                    Question.category == category_id).all()]
            next_question = {}

            for x in all_questions:
                if x["id"] not in previous_questions:
                    next_question = x

            if next_question == {}:
                next_question = None

            categories_list = []

            for x in all_categories:
                categories_list.append(x["type"])

            formatted_questions = {
                "question": next_question,
                "categories": categories_list
            }
            return jsonify(formatted_questions)
        except BaseException:
            cfunc.cprint("Error", e)
            abort(404)

    return app
