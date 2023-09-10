from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repo as merchant_repo
import repositories.tag_repo as tag_repo
import repositories.transactions_repo as trans_repo

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
    return render_template('merchant/edit.html', merchant = merchant)

@merchant_blueprint.route("/merchants/<id>",  methods=['POST'])
def update_transaction(id):
    merchant = merchant_repo.select(id)
    name = request.form['name']
    merchant.name = name
    merchant_repo.update(merchant)
    return redirect('/merchants')