import pdb
from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def save(merchant):
    sql = "INSERT INTO locations(name, category) VALUES ( %s, %s ) RETURNING id"
    values = [merchant.name, merchant.id]
    results = run_sql( sql, values )
    merchant.id = results[0]['id']
    return merchant

def select(id):
    merchant = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['category'], result['id'] )
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)