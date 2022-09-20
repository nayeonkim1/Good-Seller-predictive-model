# -*- coding: utf-8 -*-
"""goodseller_predict.ipynb

Automatically generated by Colaboratory.
"""

#나눔 폰트 설치후 런타임 재시작

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import numpy as np
import pandas as pd
from google.colab import drive


drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/data")
del df['Unnamed: 0']
df.head()

X = pd.DataFrame(df.iloc[:,1:-1])
y = pd.DataFrame(df['y'])

y.tail()

df['y'].value_counts()

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


#시각화
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
matplotlib.rcParams['axes.unicode_minus'] = False


#한글 폰트 설정
plt.rc('font', family='NanumBarunGothic')


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2022)

print(f'Train set dimension is {X_train.shape}')
print(f'Test set dimension is {X_test.shape}')

df.info()

"""## XGBOOST 모형"""

import xgboost as xgb

model = xgb.XGBClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## GradientBoosting"""

from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## Adaboost"""

from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## lightgbm"""

from lightgbm import LGBMClassifier

model = LGBMClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## randomforest"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""# resampling - SMOTE

"""

from imblearn.over_sampling import SMOTE 

sme = SMOTE(sampling_strategy=1,random_state=2022)
X, y = sme.fit_resample(X, y)

print(f'Train set dimension is {X.shape}')
print(f'Test set dimension is {y.shape}')

y['y'].value_counts()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2022)

"""## XGBOOST 모형"""

model = xgb.XGBClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## GradientBoosting"""

model = GradientBoostingClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## Adaboost"""

model = AdaBoostClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

"""## lightgbm"""

model = LGBMClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))

# Commented out IPython magic to ensure Python compatibility.
from lightgbm import plot_importance
import matplotlib.pyplot as plt
# %matplotlib inline

model.fit(X, y)
fig, ax = plt.subplots(figsize=(5,7))
plot_importance(model, ax=ax)

"""## randomforest"""

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, scoring="roc_auc", cv=5, verbose=False)
# print('교차 검증별 AUC:', np.round(scores,4))
print('평균 검증 AUC:', np.round(np.mean(scores),4))