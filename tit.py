import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv("titanic.csv")

# Clean missing values.
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop("Cabin", axis=1)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Embarked"]=df["Embarked"].map({"S":0,"C":1,"Q":2})

print(df["Sex"].head())
print(df["Embarked"].head())
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]
print(X.head())
print(y.head())
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
print(model.score(X_train,y_train))
print(model.score(X_test,y_test))
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]})

print(coefficients.sort_values("Coefficient", ascending=False))
print(f"intercept:{model.intercept_}")