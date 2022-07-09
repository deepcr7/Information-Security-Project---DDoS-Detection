# Training data
"""
Training the different protocols with the best chosen models from the analysis

"""
import numpy as np
import pandas as pd
import sys
import pickle

df = pd.read_csv(r"revised_kddcup_dataset.csv",index_col=0)

def train_icmp(df, classifier=0):
    """
    Only two best classifiers have been employed on these datasets
    """
    icmp_df = df[df.loc[:,"protocol_type"] == "icmp"]
    icmp_features = ["duration","src_bytes","wrong_fragment","count","urgent","num_compromised","srv_count"]
    icmp_target = "result"
    X = icmp_df.loc[:,icmp_features]
    y = icmp_df.loc[:,icmp_target]
    classes = np.unique(y)
    from sklearn import preprocessing
    label_encoder = preprocessing.LabelEncoder()
    icmp_df['result']= label_encoder.fit_transform(icmp_df['result'])
    icmp_df['result'].unique()

   
    
    y = icmp_df.loc[:,icmp_target] #updating the y variables
    print("Data preprocessing done.")
    
    #choose DT if classifier == 0 else choose RF
    if str(classifier) == "0":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    elif str(classifier) == "1":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
    else:
        print("Wrong model chosen! Placing default model 0 to model training!")
        model = DecisionTreeClassifier()
    
    
    #fitting our model
    model.fit(X,y)
    print("The model has been fit.")
    
    print("Save the fitted model?(y/n):")
    choice = input().lower()
    if choice == "y":
        pickle.dump(model, open("./saved_model/icmp_data.sav", 'wb'))

def train_tcp_syn(df, classifier=0):
    """
    Only two best classifiers have been employed on these datasets
    """
    tcp_syn_df = df[df.loc[:,"protocol_type"] == "tcp"]
    tcp_syn_df = tcp_syn_df[tcp_syn_df.loc[:,"srv_serror_rate"] > 0.7]
    
    service_values = np.unique(tcp_syn_df.loc[:,"service"])
    mid = (len(service_values)+1)/2
    for i in range(len(service_values)):
        tcp_syn_df = tcp_syn_df.replace(service_values[i], (i-mid)/10)
    
    features = ["service","count","srv_count","src_bytes","serror_rate"]
    target = "result"
    
    X = tcp_syn_df.loc[:,features]
    y = tcp_syn_df.loc[:,target]
    classes = np.unique(y)
    from sklearn import preprocessing
    label_encoder = preprocessing.LabelEncoder()
    tcp_syn_df['result']= label_encoder.fit_transform(tcp_syn_df['result'])
 
    
    y = tcp_syn_df.loc[:,target] #updating the y variables
    
    print("Data preprocessing done.")
    
    #choose DT if classifier == 0 else choose RF
    if str(classifier) == "0":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    elif str(classifier) == "1":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
    else:
        print("Wrong model chosen! Placing default model 0 to model training!")
        model = DecisionTreeClassifier()
    
    
    #fitting our model
    model.fit(X,y)
    print("The model has been fit.")
    
    print("Save the fitted model?(y/n):")
    choice = input().lower()
    if choice == "y":
        pickle.dump(model, open("./saved_model/tcp_syn_data.sav", 'wb'))

def train_udp(df, classifier=0):
    """
    Only two best classifiers have been employed on these datasets
    """
    udp_df = df[df.loc[:,"protocol_type"] == "udp"]
    
    service_values = np.unique(udp_df.loc[:,"service"])
    mid = (len(service_values)+1)/2
    for i in range(len(service_values)):
        udp_df = udp_df.replace(service_values[i], (i-mid)/10)
    
    udp_features = ["dst_bytes","service","src_bytes","dst_host_srv_count","count"]
    udp_target = "result"
    
    X = udp_df.loc[:,udp_features]
    y = udp_df.loc[:,udp_target]
    classes = np.unique(y)
    from sklearn import preprocessing
    label_encoder = preprocessing.LabelEncoder()
    udp_df['result']= label_encoder.fit_transform(udp_df['result'])
    udp_df['result'].unique()
    
    #turning the service attribute to categorical values
    #icmp_df=icmp_df.replace("eco_i",-0.1)
    #icmp_df=icmp_df.replace("ecr_i",0.0)
    #icmp_df=icmp_df.replace("tim_i",0.1)
    #icmp_df=icmp_df.replace("urp_i",0.2)
    
    y = udp_df.loc[:,udp_target] #updating the y variables
    print("Data preprocessing done.")
    
    #choose DT if classifier == 0 else choose DT
    if str(classifier) == "0":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    elif str(classifier) == "1":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
    else:
        print("Wrong model chosen! Placing default model 0 to model training!")
        
        model = DecisionTreeClassifier()
    
    
    #fitting our model
    model.fit(X,y)
    print("The model has been fit.")
    
    print("Save the fitted model?(y/n):")
    choice = input().lower()
    if choice == "y":
        pickle.dump(model, open("./saved_model/udp_data.sav", 'wb'))


if __name__ == "__main__":
    if str(sys.argv[1]) == "icmp":
        train_icmp(df,sys.argv[2])
    elif str(sys.argv[1]) ==  "tcp_syn":
        train_tcp_syn(df,sys.argv[2])
    elif str(sys.argv[1]) == "udp":
        train_udp(df,sys.argv[2])
    else:
        print("Did not select correct protocol. Try again.")
        
