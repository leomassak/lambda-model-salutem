from bson import json_util, ObjectId
from mongo_handler import MongoConnection

import json
import main
import clustering

def lambda_handler(event, context):

    print(f"Lambda event: {event}")
    
    request = eval(event['body']) if event.get('headers') else event['body']
    print(f"Request body: {request}")

    try:
        mongo_h = MongoConnection()
        dataset = mongo_h.get_collection('users')
    except Exception as e:
        print(f"Mongo get collection error: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error':e.args})
        }

    try:
        otherUsers = main.removeUserId(request['userId'], dataset)
        print(f"Separated users: {otherUsers}")

        otherUsersKnn = clustering.transformToKnnArray(otherUsers)
        print(f"Other users array: {otherUsersKnn}")

        userKnn = [[
            request['filters']['spec'],
            request['filters']['insurance'],
            request['filters']['lat'],
            request['filters']['long']
            ]]
    except Exception as e:
        print(f"Transformation error: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error':e.args})
        }

    try:
        result = clustering.knn(userKnn, otherUsersKnn, k=4)

        usersByKnn = clustering.getUsersByKnnDoctor(otherUsers, result[0])
        print(f"Recommender result: {usersByKnn}")

        return {
            "statusCode": 200,
            "body": json_util.dumps({"data": usersByKnn}),
            "isBase64Encoded": False
        }
    except Exception as e:
        print(f"Clustering exception: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error':e.args})
        }