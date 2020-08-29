import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score,roc_auc_score

df = pd.read_csv('./data/income_after_pearson.csv')
print(df.info())
train_data = df[df['date']<1074]
test_data = df[df['date']>=1074]

X_train = train_data.loc[:,"營業收入":"綜合損益總額歸屬於共同控制下前手權益"].values
y_train = train_data['label'].values
X_test = test_data.loc[:,"營業收入":"綜合損益總額歸屬於共同控制下前手權益"].values
y_test = test_data['label'].values

rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, random_state=42)
rnd_clf.fit(X_train, y_train)

print('train score:',accuracy_score(y_train,rnd_clf.predict(X_train)))
print('test score:',accuracy_score(y_test,rnd_clf.predict(X_test)))