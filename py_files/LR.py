from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class LR:
    def __init__(self,df,pred):
        self.df= df.copy()
        self.df1= df.drop(str(pred),axis=1)
        self.y=self.df[pred]
    def get_score(self):
        X_train, X_test, y_train, y_test = train_test_split(self.df1,self.y, test_size=0.33, random_state=42)
        lr=LinearRegression()
        lr.fit(X_train,y_train)
        return lr.score(X_test,y_test)
    def get_pred(self,test):
        lr=LinearRegression()
        lr.fit(self.df1,self.y)
        pred=lr.predict(test)
        return pred
