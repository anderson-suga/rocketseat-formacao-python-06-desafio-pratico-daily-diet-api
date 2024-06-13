from flask import Blueprint, request, jsonify
from models.meal import Meal
from database import db

main = Blueprint("main", __name__)


@main.route("/meals", methods=["POST"])
def add_meal():
    data = request.get_json()
    new_meal = Meal(
        name=data["name"],
        description=data["description"],
        in_diet=data["in_diet"],
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({"message": "Refeição adicionada com sucesso"}), 201


@main.route("/meals/<int:id>", methods=["PUT"])
def edit_meal(id):
    data = request.get_json()
    meal = Meal.query.get_or_404(id)

    meal.name = data["name"]
    meal.description = data["description"]
    meal.date_time = data["date_time"]
    meal.in_diet = data["in_diet"]

    db.session.commit()
    return jsonify({"message": "Refeição atualizada com sucesso"}), 200


@main.route("/meals/<int:id>", methods=["DELETE"])
def delete_meal(id):
    meal = Meal.query.get_or_404(id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": "Refeição deletada com sucesso"}), 200


@main.route("/meals", methods=["GET"])
def get_meals():
    meals = Meal.query.all()
    meals_list = [
        {
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time,
            "in_diet": meal.in_diet,
        }
        for meal in meals
    ]
    return jsonify(meals_list), 200


@main.route("/meals/<int:id>", methods=["GET"])
def get_meal(id):
    meal = Meal.query.get_or_404(id)
    meal_data = {
        "id": meal.id,
        "name": meal.name,
        "description": meal.description,
        "date_time": meal.date_time,
        "in_diet": meal.in_diet,
    }
    return jsonify(meal_data), 200
