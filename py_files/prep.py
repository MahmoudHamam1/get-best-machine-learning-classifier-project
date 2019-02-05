from sklearn.preprocessing import LabelEncoder #importing labelEncoder
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
def cleaning(df):
    for col in df.columns:
        if df[col].dtype == "object" or len(df[col].value_counts()) < 10 :
            df[col].fillna(df[col].mode()[0],inplace=True)
        else:
            df[col].fillna(df[col].mean(),inplace=True)
            
    for col in df.columns:
        if df[col].dtype != "object":
            df[[col]] =sc.fit_transform(df[[col]])
        
    data_dic = {}
    for col in df.columns:
        if df[col].dtype == "object":
            data_dic[col] = LabelEncoder()
            data_dic[col].fit(df[col])
            df[col] =data_dic[col].transform(df[col])
    
    return {"data":df,"d":data_dic}
