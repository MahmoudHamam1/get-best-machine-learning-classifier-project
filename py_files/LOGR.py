from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
class LR:
    def __init__(self,df,pred,lda):
        self.df= df.copy()
        self.df1= df.drop(str(pred),axis=1)
        self.y=self.df[pred]
        self.lda=lda
    def get_score(self):
        X_train, X_test, y_train, y_test = train_test_split(self.df1,self.y, test_size=0.33, random_state=42)
        X_train=self.lda.transform(X_train)
        X_test=self.lda.transform(X_test)
        log=LogisticRegression()
        log.fit(X_train,y_train)
        return log.score(X_test,y_test)
    def get_pred(self,test):
        log=LogisticRegression()
        log.fit(self.lda.transform(self.df1),self.y)
        pred=log.predict(self.lda.transform(test))
        return pred
