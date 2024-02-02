from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo
import repositories.transactions_repo as transaction_repo

tag_blueprint = Blueprint("tags", __name__)

@tag_blueprint.route("/tags")
def tags():
    tags = tag_repo.select_all() # NEW
    return render_template("tag/index.html", tags = tags)

@tag_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repo.select(id)
    merchants = merchant_repo.merchants_for_tag(tag)
    print(tag.name)
    print(tag.id)
    return render_template("tag/show.html", tag=tag, merchants = merchants)

@tag_blueprint.route("/tags/new", methods=['GET'])
def new_tag():
    merchants = merchant_repo.select_all()
    transactions = transaction_repo.select_all()
    print(merchants, transactions)
    return render_template("/tags/new", transactions = transactions, merchants = merchants)

#On tag page
#creating a tag
#On rendered input transaction id, merchant id and amount
#sets tag to new tag
#saves tag
#redirects to /tags
@tag_blueprint.route("/tags", methods=['POST'])
def create_tag():
    print("triggered")
    transactions_id = request.form['transactions_id']
    merchant_id = request.form['merchant_id']
    amount = request.form['amount]']
    transactions = transaction_repo.select(transactions_id)
    merchant = merchant_repo.select(merchant_id)
    tag = Tag(merchant, transactions, amount)
    tag_repo.save(tag)
    return redirect('/tags')

@tag_blueprint.route("/tags/<id>/delete", methods=['POST'])
def delete_task(id):
    tag_repo.delete(id)
    return redirect('/tags')

