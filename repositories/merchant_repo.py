import pdb
from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES ( %s ) RETURNING id"
    values = [merchant.name]
    results = run_sql( sql, values )
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants "
    results = run_sql(sql)

    for row in results:
        location = Merchant(row['name'], row['id'])
        merchants.append(location)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'] )
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def merchants_for_tag(tag):
    merchants = []
    sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE location_id = %s"
    sql = "SELECT merchants.* FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchant.id WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        merchant = Merchant(row["name"], row["id"])
        merchants.append(merchant)

    return merchants
    
def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql( sql, values )