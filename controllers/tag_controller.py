from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo
tag_blueprint = Blueprint("tags", __name__)

@tag_blueprint.route("/tags")
def users():
    tags = tag_repo.select_all() # NEW
    return render_template("tags/index.html", tags = tags)

@tag_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repo.select(id)
    merchants = merchant_repo.tag_for_merchant(tag)
    return render_template("tags/show.html", tag=tag, merchants = merchants)