import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score,roc_auc_score

def rf(path):
    df = pd.read_csv(path)
    #print(df.info())
    train_data = df[df['date']<1074]
    test_data = df[df['date']>=1074]

    X_train = train_data.iloc[:,3:-2].values
    y_train = train_data['label'].values
    X_test = test_data.iloc[:,3:-2].values
    y_test = test_data['label'].values

    rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, random_state=42)
    rnd_clf.fit(X_train, y_train)

    print('train score:',accuracy_score(y_train,rnd_clf.predict(X_train)))
    print('test score:',accuracy_score(y_test,rnd_clf.predict(X_test)))
    return

rf('./data/income_sheet_clean_after_pearson.csv')
print('========================')
rf('./data/balance_sheet_clean_after_pearson.csv')

# df = pd.read_csv('./data/income_sheet_clean_after_pearson.csv')
# print(df.iloc[:,3:-2])