from pymongo import MongoClient


def base_mongo():
    client = MongoClient('localhost', 27017)
    collection = client['test3']['py_col']
    # collection.insert([{'name': 'gy', 'age': 23}, {'name': 'dushiqiang', 'age': 24}])
    # collection.insert({'name': 'duwenqing', 'age': 19})
    item_list = [{'name': 'test1000{}'.format(i)} for i in range(10)]
    # t1 = collection.insert_many(item_list)
    t2 = collection.find({'name': 'test10003'})
    print(t2)
    t3 = collection.find()
    for j in t3:
        print(j)
    collection.update({'name': ' dushiqiang'}, {'$set': {'name': '大肥子'}})
    t4 = collection.find({'name': '大肥子'})
    # print(t4)
    item_list1 = [{'name': 'test1000{}'.format(i)} for i in range(10, 20)]
    t5 = collection.find({'name': {'$regex': '^test1000.*'}})
    # for l in t5:
    #     print(l)
    # collection.update_many({'name': {'$regex': '^test1000.*'}}, {'$inc': {'name': 'test'}})
    collection.update_one({'name': 'gy'}, {'$set': {'name': 'gaoyan'}})
    collection.update({'name': 'test100008'}, {'$set': {'name': 'test190832'}})
    #
    # collection.delete_one({'name': 'test10000'})
    # collection.delete_many({'name': {'$regex': '^test1000.*'}})



if __name__ == '__main__':
    base_mongo()
