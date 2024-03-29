from db.run_sql import run_sql
from models.transactions import Transactions
from models.tag import Tag
from models.merchant import Merchant 
import repositories.merchant_repo as merchant_repo
import repositories.tag_repo as tag_repo
import pdb

def save(transaction):
    sql = "INSERT INTO transactions ( tag_id, merchant_id, amount ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [transaction.tag.id, transaction.merchant.id, transaction.amount]
    results = run_sql( sql, values )
    transaction.id = results[0]['id']
    return transaction

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            tag = tag_repo.select(row['tag_id'])
            merchant = merchant_repo.select(row['merchant_id'])
            transaction = Transactions(merchant, tag,  row['amount'], row['id'])
    return transaction

def select_all():
    # pdb.set_trace()
    transactions = []

    sql = "SELECT * FROM transactions ORDER BY amount DESC;"
    results = run_sql(sql)

    for row in results:
        
        tag = tag_repo.select(row['tag_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        transaction = Transactions(merchant, tag,  row['amount'], row['id'])
        transactions.append(transaction)
    return transactions


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET ( tag_id, merchant_id, amount )  = ( %s, %s, %s ) WHERE id = %s"
    values = [transaction.tag.id, transaction.merchant.id, transaction.amount, transaction.id]
    run_sql( sql, values )