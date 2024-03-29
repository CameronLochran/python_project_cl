import pdb
from models.tag import Tag
from models.merchant import Merchant
from models.transactions import Transactions

import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo
import repositories.transactions_repo as transactions_repo

# pdb.set_trace()
transactions_repo.delete_all()
tag_repo.delete_all()
merchant_repo.delete_all()


tag1 = Tag("Mike Dean")
tag_repo.save(tag1)

tag2 = Tag("Jocelyn")
tag_repo.save(tag2)

tag3 = Tag("Tedros")
tag_repo.save(tag3)

merchant1 = Merchant("DistroKid.com")
merchant_repo.save(merchant1)

merchant2 = Merchant("Republic Records")
merchant_repo.save(merchant2)

merchant3 = Merchant("M.W.A Music")
merchant_repo.save(merchant3)

transaction1 = Transactions(merchant1, tag1, 22.99)
transactions_repo.save(transaction1)

transaction2 = Transactions(merchant1, tag2, 39.99)
transactions_repo.save(transaction2)

transaction3 = Transactions(merchant2, tag3, 89.99)
transactions_repo.save(transaction3)

pdb.set_trace()