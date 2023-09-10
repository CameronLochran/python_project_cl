from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transactions import Transactions
import repositories.transactions_repo as transaction_repo
import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo
import pdb

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    # pdb.set_trace()
    transactions = transaction_repo.select_all() # NEW
    return render_template("transactions/index.html", transactions = transactions)

@transactions_blueprint.route("/transactions/<id>")
def show(id):
    transaction = transaction_repo.select(id) 
    return render_template("transactions/show.html", transaction = transaction)

@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def edit(id):
    transaction = transaction_repo.select(id)
    # transaction.amount = request.form['amount']
    # transaction_repo.update(transaction)
    return render_template("transactions/edit.html", transaction = transaction)

@transactions_blueprint.route("/transactions/new")
def new_task():
    tags = tag_repo.select_all()
    merchants = merchant_repo.select_all()
    return render_template("transactions/new.html", tags = tags, merchants = merchants)

@transactions_blueprint.route("/transactions",  methods=['POST'])
def create_task():
    print("triggered")
    tag_id = request.form['tag_id']
    merchant_id = request.form['merchant_id']
    amount = request.form['amount']
    tag = tag_repo.select(tag_id)
    merchant = merchant_repo.select(merchant_id)
    transaction = Transactions(merchant, tag, amount)
    transaction_repo.save(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>",  methods=['POST'])
def update_transaction(id):
    transaction = transaction_repo.select(id)
    amount = request.form['amount']
    transaction.amount = amount
    transaction_repo.update(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_task(id):
    transaction_repo.delete(id)
    return redirect('/transactions')

