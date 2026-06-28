import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("titanic.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop("Cabin", axis=1)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]

# Logistic Regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
print(f"Logistic Regression - Train: {model.score(X_train_scaled, y_train):.2f}, Test: {model.score(X_test_scaled, y_test):.2f}")

y_pred = model.predict(X_test_scaled)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Decision Tree - testing different depths
depths = [2, 3, 5, 10, 15, 20]
train_scores = []
test_scores = []

for d in depths:
    tree_model = DecisionTreeClassifier(max_depth=d, random_state=42)
    tree_model.fit(X_train, y_train)
    train_scores.append(tree_model.score(X_train, y_train))
    test_scores.append(tree_model.score(X_test, y_test))

plt.figure(figsize=(8, 5))
plt.plot(depths, train_scores, marker='o', label="Train Score")
plt.plot(depths, test_scores, marker='o', label="Test Score")
plt.xlabel("Max Depth")
plt.ylabel("Accuracy")
plt.title("Overfitting: Train vs Test Score")
plt.legend()
plt.show()