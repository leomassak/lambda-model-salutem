from pymongo import MongoClient
class MongoConnection:
    def __init__(self):
        mongo_url = 'mongodb+srv://salutem:salutem@salutem.50eqm.mongodb.net/salutemDb?retryWrites=true&w=majority'
        self.client = MongoClient(mongo_url)
        self.database = self.client['salutemDb']
        self.query_result = []
        self.collection = []

    def get_collection(self, coll_name):
        self.__load_collection(coll_name)
        self.__query(self.collection.find({"profileType": 3}))
        return self.ret_query_json()

    def __load_collection(self, coll_name):
        self.collection = self.database[coll_name]

    def __query(self, cursor):
        self.query_result = []
        for each_row in cursor:
            self.query_result.append(each_row)

    def ret_query_json(self):
        list_row = []
        for each_row in self.query_result:
            list_row.append(each_row)
        return list_row
        
    def info(self):
        return 'client: {}, db: {}, query_result: {}'.format(self.client,
                                                            self.database,
                                                            self.query_result)