import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from smart_open import open
import pickle

class ClassifierFindU:
    def __init__(self, values, label, algor, user_id):
        self.S3_PATH = os.environ['s3_path_model']
        print(self.knn_classifier(values, label, 3, algor, user_id))

    def knn_classifier(self, features, labels, k_nn, algor, user_id):
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

        #for e in range(1,iteration_nn,2):
        knn = KNeighborsClassifier(n_neighbors=k_nn)

        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)
        str_return = f"Accuracy: {metrics.accuracy_score(y_test, y_pred)} for {k_nn}NN"

        #knn = KNeighborsClassifier(n_neighbors=k_nn)
        #knn.fit(X_train)

        knn_model_p = open(f'{self.S3_PATH}knn_model_{algor}_{user_id}', 'wb')
        pickle.dump(knn, knn_model_p)
        return str_return