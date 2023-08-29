from db.run_sql import run_sql
from models.transactions import Transactions
from models.tag import Tag
import repositories.merchant_repo as merchant_repo
import repositories.tag_repo as tag_repo

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        tag = Tag(result['name'], result['id'] )
    return tag

def select_all():
    transactions = []

    sql = "SELECT * FROM transaction"
    results = run_sql(sql)

    for row in results:
        tag = tag_repo.select(row['tag_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        transaction = Transactions(tag, merchant, row['review'], row['id'])
        transactions.append(transaction)
    return transactions



   

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)