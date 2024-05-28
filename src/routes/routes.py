from flask import Blueprint, redirect, render_template, session, url_for

from ..forms.category_form import CategoryForm

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    form = CategoryForm()
    return render_template("home.html", form=form)


@main_bp.route("/add-cat-to-session", methods=["POST"])
def add_cat_to_session():
    form = CategoryForm()
    form["name"]

    if "categories" not in session:
        print("Não existe o item 'categories' ")
        session["categories"] = []

    session["categories"].append(form.data["name"])
    session.modified = True  # Como a lista é uma estrutura mutável, acaba que o flask não percebe que o conteúdo da lista foi modificado pois ela permanece sendo uma lista

    return render_template("categories-list.html", categories=session["categories"])


@main_bp.route("/clear_session", methods=["POST"])
def clear_session():
    # Todo: a sessão está sendo limpa, mas o html não é atualizado
    session.clear()

    return "", 204


"""
O que acontece é o seguinte, eu vou bater na rota add_cat_to_session e não vou fazer redirecionamento nenhum, eu vou apenas acessar uma variável com todos as cat adicionadas até agora e usar elas para alterar a segunda parte do modal. Depois, quando todas as cetegoria que eu quiser estiverem adicionadas o 'save change' vai bater em outra rota que vai adicionar as categorias ao banco de dados.
"""
