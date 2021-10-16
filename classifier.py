# from pyspark.ml.recommendation import ALS


# def tune_ALS(train_data, validation_data, maxIter, regParams, ranks):
#     """
#     grid search function to select the best model based on RMSE of
#     validation data
#     Parameters
#     ----------
#     train_data: spark DF with columns ['userId', 'movieId', 'rating']
    
#     validation_data: spark DF with columns ['userId', 'movieId', 'rating']
    
#     maxIter: int, max number of learning iterations
    
#     regParams: list of float, one dimension of hyper-param tuning grid
    
#     ranks: list of float, one dimension of hyper-param tuning grid
    
#     Return
#     ------
#     The best fitted ALS model with lowest RMSE score on validation data
#     """
#     # initial
#     min_error = float('inf')
#     best_rank = -1
#     best_regularization = 0
#     best_model = None
#     for rank in ranks:
#         for reg in regParams:
#             # get ALS model
#             als = ALS().setMaxIter(maxIter).setRank(rank).setRegParam(reg)
#             # train ALS model
#             model = als.fit(train_data)
#             # evaluate the model by computing the RMSE on the validation data
#             predictions = model.transform(validation_data)
#             evaluator = RegressionEvaluator(metricName="rmse",
#                                             labelCol="rating",
#                                             predictionCol="prediction")
#             rmse = evaluator.evaluate(predictions)
#             print('{} latent factors and regularization = {}: '
#                   'validation RMSE is {}'.format(rank, reg, rmse))
#             if rmse < min_error:
#                 min_error = rmse
#                 best_rank = rank
#                 best_regularization = reg
#                 best_model = model
#     print('\nThe best model has {} latent factors and '
#           'regularization = {}'.format(best_rank, best_regularization))
#     return best_model

# # import os
# # from sklearn.model_selection import train_test_split
# # from sklearn.model_selection import GridSearchCV
# # from sklearn.neighbors import NearestNeighbors
# # from sklearn.neighbors import BallTree
# # from sklearn.cluster import KMeans
# # from sklearn import metrics
# # from sklearn.metrics import roc_auc_score
# # from sklearn.metrics import silhouette_score
# # from sklearn.preprocessing import StandardScaler
# # class ClassifierSalutem:
# #     def __init__(self, dataset):
# #         self.get_scores(dataset)

# #     # def cv_silhouette_scorer(self, estimator, X):
# #     #     gs_res = estimator.fit(X)
# #     #     print(f'gs_res: {gs_res}')
# #     #     cluster_labels = estimator.labels_
# #     #     num_labels = len(set(cluster_labels))
# #     #     num_samples = len(X.index)
# #     #     if num_labels == 1 or num_labels == num_samples:
# #     #         return -1
# #     #     else:
# #     #         return silhouette_score(X, cluster_labels)

# #     def get_scores(self, dataset):
# #         print(f"Start split with features: {dataset}")
# #         scaler = StandardScaler()
# #         X_scaled = scaler.fit_transform(dataset)
# #         kmeans = KMeans(n_clusters=2, random_state=0).fit(X_scaled)
# #         # X_train, X_test, y_train, y_test = train_test_split(dataset, ['spec', 'insurance', 'lat', 'long'], test_size=0.2, random_state = 5)
# #         # print(f"X train: {X_train} | X test: {X_test} | y train: {y_train} | y_test: {y_test}")

# #         #for e in range(1,iteration_nn,2):
# #         # estimator_knn = NearestNeighbors(algorithm='ball_tree')

# #         grid_params = { 
# #                         'n_clusters' : [4,8,9,11,13,15],
# #                         'leaf_size': [10,20,30,40],
# #                         'metric' : ['minkowski','euclidean','manhattan'],
# #                         'p': [1,2]
# #                       }

# #         gs = GridSearchCV(
# #                             estimator=kmeans,
# #                             param_grid=grid_params,
# #                             scoring='adjusted_mutual_info_score',
# #                             n_jobs = -1,
# #                             #cv = [(slice(None), slice(None))]
# #                         )

# #         g_res = gs.fit(dataset)
# #         g_pred = gs.predict(dataset)
# #         print(f"Res full dict: {g_res} | Predict: {g_pred}")
# #         #print(f"Best score: {g_res.best_score_} | Best params: {g_res.best_params_} | Predict: {g_pred}")

# #         # print('BEST K-NEAREST NEIGHBORS MODEL')
# #         # print("Silhouette score:",silhouette_score(dataset, g_pred))
# #         # print('Accuracy Score - KNN:', metrics.accuracy_score(y_test, g_pred))  
# #         # print('Average Precision - KNN:', metrics.average_precision_score(y_test, g_pred)) 
# #         # print('F1 Score - KNN:', metrics.f1_score(y_test, g_pred)) 
# #         # print('Precision - KNN:', metrics.precision_score(y_test, g_pred)) 
# #         # print('Recall - KNN:', metrics.recall_score(y_test, g_pred))
# #         # print('ROC Score - KNN:', roc_auc_score(y_test, g_pred))

# #         return g_res

