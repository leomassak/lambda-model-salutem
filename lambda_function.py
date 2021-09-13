import json
from mongo_handler import MongoConnection
import os
import main
import clustering

def lambda_handler(event, context):
    
    request = eval(event['body'])
    print(request)
    
    mongo_h = MongoConnection()
    print(mongo_h.info())

    dataset, id_str = mongo_h.get_collection('user')

    otherUsers = main.removeUserId(request['userId'], dataset)
    user = main.onlyById(request['userId'], dataset)

    #otherUsers = main.removeUserWithoutInfo(otherUsers)

    otherUsers = main.removeUnnecessaryProperty(otherUsers)
    user = main.removeUnnecessaryProperty(user)

    otherUsersKnn = clustering.transformToKnnArray(otherUsers)
    userKnn = clustering.transformToKnnArray(user)

    result = clustering.knn(userKnn, otherUsersKnn, k=4)

    usersByKnn = clustering.getUsersByKnnDoctor(otherUsers, result[0])
    print(usersByKnn)

    return {
        'statusCode': 200,
        'body': json.dumps({'result':usersByKnn})
    }

    #cluster = ClusterSalutem(id_str, dataset)
    #cluster.run_cluster()