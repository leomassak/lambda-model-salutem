from sklearn.neighbors import BallTree

def getUsersByKnnDoctor(otherUsers, result):
    temp = []
    for i in range(len(result)):
        x = int(result[i])
        temp.append({
            "id": otherUsers[x].id, 
            "doctor_name": otherUsers[x].name,
            "crm": otherUsers[x].crm,
            "address": otherUsers[x].address,
            "location": otherUsers[x].location,
            "review": otherUsers[x].review
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
        temp.append([data[i].spec,data[i].insurance,data[i].location.coordinates.lat,data[i].location.coordinates.long])
    return temp

def knn(user, otherUsers, k):
    tree = BallTree(otherUsers, leaf_size=30)
    dist, ind = tree.query(user, k=k)
    
    return ind


# # birch clustering
# #import pandas as pd
# from classifier import ClassifierFindU
# import sklearn.cluster as sk_cl
# from sklearn.mixture import GaussianMixture

# class ClusterFindU:
#     def __init__(self, user_id, df):
#         self.user_id = user_id
#         self.dataset = df

#     def run_cluster(self): #self, func, df
#         #BIRCH
#         mdl = self.clust_BIRCH(0.05)
#         yhat = mdl.fit_predict(self.dataset)
#         print(f'BIRCH, {(yhat,len(yhat))}')
#         ClassifierFindU(self.dataset, yhat,'BIRCH', self.user_id)

#         #DBSCAN
#         mdl = self.clust_DBSCAN(0.05, 5)
#         yhat = mdl.fit_predict(self.dataset)
#         print(f'DBSCAN, {(yhat,len(yhat))}')
#         ClassifierFindU(self.dataset, yhat,'DBSCAN', self.user_id)

#         #OPTICS
#         mdl = self.clust_OPTICS(0.05, 50)
#         yhat = mdl.fit_predict(self.dataset)
#         print(f'OPTICS, {(yhat,len(yhat))}')
#         ClassifierFindU(self.dataset, yhat, 'OPTICS', self.user_id)


#     def clust_BIRCH(self, thresh): # 0.05
#         # define the model
#         return sk_cl.Birch(threshold=thresh)


#     def clust_DBSCAN(self, eps, min_samp): # 0.05, 5
#         # define the model
#         return sk_cl.DBSCAN(eps=eps, min_samples=min_samp)


#     def clust_affinity_prop(self, damp): # 0.9
#         # define the model
#         return sk_cl.AffinityPropagation(damping=damp)


#     def clust_OPTICS(self, eps, min_samp): # 0.05, 50
#         return sk_cl.OPTICS(eps=eps, min_samples=min_samp)  


#     # def dataset_categorized(self, df, col):
#     #     for each_arr in df:
#     #         each_arr.append(col)
#     #     return df


#     # gen_vis_3d(clust_BIRCH, dataset)
#     # values = run_cluster(clust_DBSCAN, dataset)
#     # values = pd.Series(values,name='lbl')
#     # ds_labeled = pd.concat([dataset,values],axis=1)
#     # print(ds_labeled)
#     # ds_labeled.to_csv('DBSCAN.csv',index=False)
#     # #gen_vis_3d(clust_affinity_prop, dataset)
#     # #gen_vis_3d(clust_agglom, dataset)
#     # #gen_vis_3d(clust_feature_agglom, dataset)
#     # #gen_vis_3d(clust_kmeans, dataset)
#     # #gen_vis_3d(clust_mini_batch_kmeans, dataset)
#     # #gen_vis_3d(clust_mean_shift, dataset)
#     # values = gen_vis_3d(clust_optics, dataset)
#     # values = pd.Series(values,name='lbl')
#     # ds_labeled = pd.concat([dataset,values],axis=1)
#     # print(ds_labeled)
#     # ds_labeled.to_csv('OPTICS.csv',index=False)

# def transformToHospitalKnn(data):
    #     temp = []
#     for i in range(len(data)):
#         temp.append([int(data[i].cancer),data[i].gender,data[i].sentimentos, data[i].sintomas])
#     return temp


