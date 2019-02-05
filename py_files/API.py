import prep
import LR
import LOGR
import RF
import KNN
import SVM
import Dtree
import naiv
import pandas as pd
import json
from flask import Flask,jsonify,request,render_template
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

df=prep.cleaning(pd.read_csv("dataset.csv")) #load the dataset

lda = LDA(n_components = 8)   #select 8 feature
X=df["data"].drop("Churn",axis=1)  
Y=df["data"]["Churn"]
lda.fit(X,Y)   #fit the data to select the best feature

clf_log=LOGR.LR(df["data"].copy(),"Churn",lda)  #intiate object from logisticRegression Class
clf_KNN=KNN.KNN(df["data"].copy(),"Churn",lda)  #intiate object from K-NN Class
clf_RF=RF.RF(df["data"].copy(),"Churn",lda)   #intiate object from RandomForest Class
clf_SVM=SVM.SV(df["data"].copy(),"Churn",lda)   #intiate object from RandomForest Class
clf_Dt=Dtree.DT(df["data"].copy(),"Churn",lda)   #intiate object from RandomForest Class
clf_naiv=naiv.RF(df["data"].copy(),"Churn",lda)   #intiate object from RandomForest Class

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():
    data={"data":pd.read_csv("dataset.csv").head(500).to_json()}
    return jsonify(data)
############################################################### PreProcessing  ###################################################

@app.route("/prep",methods=["GET","POST"])
def prp():
    df=prep.cleaning(pd.read_csv("dataset.csv"))["data"]
    data={"data":df.head(500).to_json()}
    return jsonify(data)
############################################################### Logistic Classifire ###################################################
@app.route("/logistic/score",methods=["GET"])
def log_score():
    data={"score":round(clf_log.get_score()*100)}
    return jsonify(data)

@app.route("/logistic/predect",methods=["GET"])
def log_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        #return jsonify({"data":list(X.columns)})
        te=pd.DataFrame(data=dic)
        #return jsonify({"data":dic})
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_log.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    #te.to_csv("out.csv",index=False)
    return jsonify(data)

############################################################### RF Classifire ###################################################
@app.route("/RF/score",methods=["GET"])
def RF_score():
    data={"score":round(clf_RF.get_score()*100)}
    return jsonify(data)

@app.route("/RF/predect",methods=["GET"])
def RF_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_RF.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    #te.to_csv("out.csv",index=False)
    return jsonify(data)

############################################################### KNN Classifire ###################################################
@app.route("/KNN/score",methods=["GET"])
def KNN_score():
    data={"score":round(clf_KNN.get_score()*100)}
    return jsonify(data)

@app.route("/KNN/predect",methods=["GET"])
def KNN_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_KNN.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    #te.to_csv("out.csv",index=False)
    return jsonify(data)
############################################################### KNN Classifire ###################################################
@app.route("/SVM/score",methods=["GET"])
def SVM_score():
    data={"score":round(clf_SVM.get_score()*100)}
    return jsonify(data)

@app.route("/SVM/predect",methods=["GET"])
def SVM_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_SVM.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    return jsonify(data)
################################################################################################ DTree #############################################################
@app.route("/Dtree/score",methods=["GET"])
def DT_score():
    data={"score":round(clf_Dt.get_score()*100)}
    return jsonify(data)

@app.route("/Dtree/predect",methods=["GET"])
def DT_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_Dt.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    return jsonify(data)

################################################################################################ Naive  #############################################################
@app.route("/naiv/score",methods=["GET"])
def naiv_score():
    data={"score":round(clf_naiv.get_score()*100)}
    return jsonify(data)

@app.route("/naiv/predect",methods=["GET"])
def naiv_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["Churn"]=df["d"]["Churn"].inverse_transform(clf_naiv.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    return jsonify(data)


############################################################### Comparing between Classifires ###################################################
@app.route("/compare/score",methods=["GET"])
def com_score():
    data={"LOGR_score":round(clf_log.get_score()*100),"KNN_score":round(clf_KNN.get_score()*100),"Dtree_score":round(clf_Dt.get_score()*100),"naiv_score":round(clf_naiv.get_score()*100),"RF_score":round(clf_RF.get_score()*100),"SVM_score":round(clf_SVM.get_score()*100)}
    return jsonify(data)

@app.route("/compare/predect",methods=["GET"])
def com_pred():
    flag=int(request.args.get('flag'))
    li=[]
    te=pd.read_csv("test.csv")
    if(flag):
        li.append(request.args.get('customerID'))
        li.append(request.args.get('Gender'))
        li.append(request.args.get('SeniorCitizen'))
        li.append(request.args.get('Partner'))
        li.append(request.args.get('Dependents'))
        li.append(request.args.get('tenure'))
        li.append(request.args.get('PhoneService'))
        li.append(request.args.get('MultipleLines'))
        li.append(request.args.get('InternetService'))
        li.append(request.args.get('OnlineSecurity'))
        li.append(request.args.get('OnlineBackup'))
        li.append(request.args.get('DeviceProtection'))
        li.append(request.args.get('TechSupport'))
        li.append(request.args.get('StreamingTV'))
        li.append(request.args.get('StreamingMovies'))
        li.append(request.args.get('Contract'))
        li.append(request.args.get('PaperlessBilling'))
        li.append(request.args.get('BaymentMrthod'))
        li.append(request.args.get('MonthlyCharges'))
        li.append(request.args.get('TotalCharges'))
        dic={}
        c=0
        for i in X.columns:
            dic[i]=[li[c]]
            c+=1
        te=pd.DataFrame(data=dic)
    te_c=prep.cleaning(te.copy())["data"]
    te["LOG_Churn"]=df["d"]["Churn"].inverse_transform(clf_log.get_pred(te_c))
    te["KNN_Churn"]=df["d"]["Churn"].inverse_transform(clf_KNN.get_pred(te_c))
    te["RF_Churn"]=df["d"]["Churn"].inverse_transform(clf_RF.get_pred(te_c))
    data={"pred":te.head(500).to_json()}
    #te.to_csv("out.csv",index=False)
    return jsonify(data)

#################################### For solving cross ##########################
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

###################################  Runnting the server #################################################
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9090)
