# Titanic ML Classifier

A professional machine learning project that predicts passenger survival on the Titanic using classic classification algorithms. The project features data preprocessing, feature engineering, exploratory visualizations, and performance comparison of Logistic Regression, Decision Trees, and Random Forests under a 5-fold cross-validation scheme.

## 📋 Table of Contents
- [Overview](#overview)
- [Dataset Details](#dataset-details)
- [Data Preprocessing Pipeline](#data-preprocessing-pipeline)
- [Models Compared](#models-compared)
- [Performance Evaluation](#performance-evaluation)
- [Project Structure](#project-structure)
- [Installation & Usage](#installation--usage)
- [License](#license)

---

## 🔍 Overview
The sinking of the Titanic is one of the most infamous shipwreck disasters in history. This project applies machine learning techniques to analyze passenger data and predict whether a passenger survived the disaster. It cleans clinical characteristics, handles missing demographic details, encodes categorical variables, and benchmarks multiple classification models to find the most accurate predictor.

## 📊 Dataset Details
The dataset used is `titanic.csv`, containing details of the Titanic passengers. The model is trained on the following features:

| Feature | Description | Encoding / Preprocessing |
|---|---|---|
| **Pclass** | Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd) | Numeric |
| **Sex** | Gender of the passenger | Mapped to: `0` (male), `1` (female) |
| **Age** | Age in years | Missing values imputed with the mean age |
| **SibSp** | Number of siblings or spouses aboard the Titanic | Numeric |
| **Parch** | Number of parents or children aboard the Titanic | Numeric |
| **Fare** | Passenger fare | Numeric |
| **Embarked** | Port of Embarkation | Mapped to: `0` (S), `1` (C), `2` (Q). Missing values filled with mode. |
| **Survived** | **Target Class** (0 = No, 1 = Yes) | Target variable |

---

## ⚙️ Data Preprocessing Pipeline
1. **Handling Missing Values**:
   - Imputed missing **Age** values with the mean age.
   - Dropped the high-cardinality **Cabin** column.
   - Filled missing **Embarked** values with the mode port (`S`).
2. **Feature Mappings**:
   - Encoded gender: `{"male": 0, "female": 1}`.
   - Encoded port of embarkation: `{"S": 0, "C": 1, "Q": 2}`.
3. **Feature Scaling**:
   - Scaled variables for scale-sensitive models (like Logistic Regression) using `StandardScaler`.

---

## 🤖 Models Compared
The project compares three classification models:
* **Logistic Regression** (Standardized inputs)
* **Decision Tree Classifier** (Optimized max depth to prevent overfitting)
* **Random Forest Classifier** (100 estimators, max depth of 5)

---

## 📈 Performance Evaluation
Models are validated using a 5-fold cross-validation scheme to ensure generalizability:

| Classifier Model | Mean 5-Fold CV Accuracy | Standard Deviation |
| :--- | :---: | :---: |
| **Random Forest Classifier** | **82.00%** | ± 3.00% |
| **Decision Tree Classifier** | **81.00%** | ± 3.00% |
| **Logistic Regression** | **79.00%** | ± 2.00% |

---

## 📁 Project Structure
```
titanic-ml-classifier/
├── tit.py             # Main model training and evaluation script
├── titanic.csv        # Dataset containing passenger information
├── README.md          # Project documentation
└── .gitignore         # Version control exclusion file
```

---

## 🚀 Installation & Usage

### Prerequisites
Make sure you have Python 3.8+ installed.

### Dependencies
Install the required libraries:
```bash
pip install pandas numpy scikit-learn matplotlib
```

### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Ravi20051/titanic-ml-classifier.git
   cd titanic-ml-classifier
   ```
2. Execute the prediction script:
   ```bash
   python tit.py
   ```
