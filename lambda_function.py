from bson import json_util, ObjectId
from mongo_handler import MongoConnection

import json
import main
import clustering

def lambda_handler(event, context):
    
    request = event['body']
    
    mongo_h = MongoConnection()

    dataset = mongo_h.get_collection('users')

    otherUsers = main.removeUserId(request['userId'], dataset)

    otherUsersKnn = clustering.transformToKnnArray(otherUsers)
    print(f"Other users array: {otherUsersKnn}")

    userKnn = [[
        request['filters']['spec'],
        request['filters']['insurance'],
        request['filters']['location']['coordinates']['lat'],
        request['filters']['location']['coordinates']['long']
        ]]

    try:
        result = clustering.knn(userKnn, otherUsersKnn, k=4)

        usersByKnn = clustering.getUsersByKnnDoctor(otherUsers, result[0])
        print(f"Recommender result: {usersByKnn}")

        return {
            'statusCode': 200,
            'body': json.loads(json_util.dumps(usersByKnn))
        }
    except Exception as e:
        print(f"Clustering exception: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error':e})
        }