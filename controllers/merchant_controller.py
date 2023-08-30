from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repo as merchant_repo
import repositories.tag_repo as tag_repo

merchant_blueprint = Blueprint("merchants", __name__)

@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repo.select_all() # NEW
    return render_template("/merchant/index.html", merchants = merchants)

@merchant_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repo.select(id)
    return render_template("merchant/show.html", merchant = merchant)

@merchant_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repo.select(id)
    tags = tag_repo.select_all()
    return render_template('merchants/edit.html', merchant = merchant, all_tags = tags)

# UPDATE
# PUT '/tasks/<id>'