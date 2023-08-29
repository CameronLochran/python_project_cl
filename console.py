import pdb
from models.tag import Tag
from models.merchant import Merchant
from models.transactions import Transactions

import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo
import repositories.transactions_repo as transactions_repo

tag_repo.delete_all()
merchant_repo.delete_all()
transactions_repo.delete_all()

tag1 = Tag("Mike Dean Merch")
tag_repo.save(tag1)

tag2 = Tag("Jocelyn Merch")
tag_repo.save(tag2)

tag3 = Tag("Tedros Merch")
tag_repo.save(tag3)

merchant1 = Merchant("DistroKid.com")
merchant_repo.save(merchant1)
pdb.set_trace()