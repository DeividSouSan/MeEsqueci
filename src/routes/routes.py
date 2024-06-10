from flask import Blueprint, Response, redirect, render_template, session, url_for

from src.entities.category import Category
from src.forms.category_form import CategoryForm
from src.repositories.category_repository import CategoryRepository
from src.use_cases.get_all_categories import GetAllCategories
from src.use_cases.remove_all_categories import RemoveAllCategories
from src.use_cases.save_categories_to_database import SaveCategoriesToDatabase

main_bp = Blueprint("main", __name__)


def redirect_response(route: str):
    response = Response()
    response.headers["hx-redirect"] = url_for(route)
    return response


# View


@main_bp.route("/")
def home():
    form = CategoryForm()

    if "categories" not in session:
        print("Não existe o item 'categories' na sessão. Criando...")
        session["categories"] = []

    if "categories_objects" not in session:
        print("Não existe o item 'categories_objects'. Criando... ")
        session["categories_objects"] = []

    return render_template(
        "home.html", form=form, categories=session["categories_objects"]
    )


# Sessão


@main_bp.route("/add-cat-to-session", methods=["POST"])
def add_cat_to_session():
    form = CategoryForm()

    last_category = Category(form.data["name"])

    session["categories"].append(last_category.__dict__)
    session.modified = True  # Como a lista é uma estrutura mutável, acaba que o flask não percebe que o conteúdo da lista foi modificado pois ela permanece sendo uma lista

    return render_template(
        "partials/categories-list.html", categories=session["categories"]
    )


@main_bp.route("/clear_cat_from_session", methods=["POST"])
def clear_cat_from_session():
    session["categories"] = []
    session.modified = True  # Como a lista é uma estrutura mutável, acaba que o flask não percebe que o conteúdo da lista foi modificado pois ela permanece sendo uma lista

    return "", 204


# Banco de Dados


@main_bp.route("/save-categories-to-database", methods=["POST"])
def save_categories_to_database():

    repository = CategoryRepository()
    use_case = SaveCategoriesToDatabase(repository)

    use_case.execute(session["categories"])

    session["categories"] = []
    session.modified = True

    return redirect(url_for("main.get_all_categories"))


@main_bp.route("/remove_all_categories", methods=["GET", "POST"])
def remove_all_categories():

    repository = CategoryRepository()
    use_case = RemoveAllCategories(repository)

    use_case.execute()

    return redirect(url_for("main.get_all_categories"))


@main_bp.route("/get-categories", methods=["GET", "POST"])
def get_all_categories():

    repository = CategoryRepository()
    use_case = GetAllCategories(repository)

    categories_list = use_case.execute()

    return render_template("partials/categories-board.html", categories=categories_list)


@main_bp.route("/add-item-to-category", methods=["POST"])
def add_item_to_category():
    if "items" not in session:
        session["items"] = []

    session["items"].append("item")

    return render_template("partials/items-list.html", items=session["items"])
