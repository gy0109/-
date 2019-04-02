from pymongo import MongoClient


def base_use():
    client = MongoClient('localhost', 27017)
    collection = client['test3']['t3']
    item_list = [{'_id': '{}'.format(_id), 'name': 'py{}'.format(_id)} for _id in range(1000)]
    collection.insert(item_list)

    # t1 = collection.find({'_id': {'$all': [i for i in range(1000) if i % 100 == 0]}})
    # for i in t1:
    #     print(i)


if __name__ == '__main__':
    base_use()


