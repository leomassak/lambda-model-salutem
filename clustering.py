from sklearn.neighbors import BallTree

def getUsersByKnnDoctor(otherUsers, result):
    temp = []
    for i in range(len(result)):
        x = int(result[i])
        string_id = str(otherUsers[x]['_id'])
        temp.append({
            "id": string_id, 
            "doctor_name": otherUsers[x]['name'],
            "doctor_info": otherUsers[x]['doctorInfo'],
            "insurance": otherUsers[x]['insurance'],
            "address": otherUsers[x]['adress'],
            "location": otherUsers[x]['location'],
            "review": otherUsers[x].get('review')
        })
    return temp

def getKnnPills(otherPills, result):
    temp = []
    for i in range(len(result)):
        x = int(result[i])
        temp.append({
            "id": otherPills[x]._id, 
            "pill_name": otherPills[x].name,
            "review": otherPills[x].review
        })
    return temp

def transformToKnnArray(data):
    temp = []
    for i in range(len(data)):
        if data[i].get('doctorInfo') and data[i].get('insurance') and data[i].get('location'):
            temp.append([data[i]['doctorInfo']['spec'],data[i]['insurance'][0],data[i]['location']['coordinates'][0],data[i]['location']['coordinates'][1]])
    return temp

def knn(user, otherUsers, k):
    tree = BallTree(otherUsers, leaf_size=30)
    dist, ind = tree.query(user, k=k)
    
    return ind

