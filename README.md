# HR Analytics – Employee Promotion Prediction

This project focuses on predicting whether an employee will be promoted based on historical HR data.  
It demonstrates an **end-to-end machine learning workflow**, from data analysis to model deployment readiness, following industry-standard practices.

---

## 📌 Problem Statement
Employee promotion decisions are influenced by multiple factors such as performance ratings, training scores, experience, and department.  
The objective of this project is to build a **binary classification model** to predict promotion outcomes (`is_promoted`) and handle challenges such as **class imbalance** and **categorical feature dominance**.

---

## 📂 Dataset Overview
The dataset contains employee-level information with the following features:

- Categorical: `department`, `region`, `education`, `gender`, `recruitment_channel`
- Numerical: `age`, `no_of_trainings`, `previous_year_rating`, `length_of_service`, `avg_training_score`
- Binary: `awards_won?`
- Target: `is_promoted`

`employee_id` was removed as it has no predictive value.

---

## 🔍 Exploratory Data Analysis (EDA)
- Analyzed class imbalance in the target variable
- Studied feature distributions and outliers
- Checked missing values and applied appropriate imputation
- Observed strong relationships between:
  - Training score & promotion
  - Previous year rating & promotion
  - Awards won & promotion

EDA was performed using **Pandas, Matplotlib, and Seaborn**.

---

## ⚙️ Data Preprocessing Strategy

### 1. Base Preprocessing
- Missing value imputation
- Dropping non-informative features
- Saved as:
  - `train_base_preprocessed.csv`
  - `test_base_preprocessed.csv`

This base dataset was reused across multiple notebooks.

---

### 2. Machine Learning Preprocessing
For classical ML models:
- One-Hot Encoding for categorical variables
- Feature scaling using `StandardScaler`
- Ensured train and test consistency

---

### 3. Neural Network Consideration
Neural Network preprocessing was kept separate, avoiding premature scaling and encoding at this stage to maintain flexibility.

---

## ⚖️ Handling Imbalanced Data
- Dataset is highly imbalanced
- Instead of over-sampling or under-sampling, **`class_weight="balanced"`** was used
- This preserves real-world distribution while improving recall and F1-score

---

## 🤖 Model Development

### Models Trained
- Logistic Regression
- Support Vector Machine
- KNN
- Naive Bayes
- Random Forest
- Gradient Boosting
- AdaBoost

### Hyperparameter Tuning
- Performed using `GridSearchCV`
- Optimized primarily for **F1-score**

---

## 🧩 Ensemble Learning

### Voting Classifier
A **soft voting classifier** was built using:
- Tuned Random Forest
- Tuned Gradient Boosting

This achieved the **best balance between precision and recall**.

### Stacking Classifier
- Tested RF + GB with Logistic Regression as meta-learner
- Resulted in high recall but lower precision
- Voting Classifier was selected as the final model

---

## 📊 Final Model Performance (Voting Classifier)

- Accuracy: ~94%
- Precision: ~83%
- Recall: ~36%
- F1-score: ~51%

Given the class imbalance, **F1-score** was prioritized over accuracy.

---

## 🚀 Deployment Architecture (Local / Demo Ready)


- **FastAPI** provides REST endpoints for prediction
- **Streamlit** acts as a user-friendly frontend
- Model is loaded once and reused for predictions

---

## 📦 Model File Note
The trained model (`.pkl`) is **not included** in this repository due to GitHub file size limitations.

This follows **industry best practices**, where models are typically stored in:
- Cloud Storage (e.g., GCS, S3)
- Model Registry systems

The repository contains **complete training, preprocessing, and deployment code** to reproduce the model.

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Docker (deployment-ready structure)
- GitHub

---

## 🔮 Future Enhancements
- Cloud deployment using Google Cloud Run
- Model versioning and monitoring
- SHAP-based model explainability
- Neural Network experimentation

---

## 👤 Author
**Santhosh Periasamy**  
Data Science / Machine Learning Engineer  

This project is part of my portfolio to demonstrate practical ML system design and deployment understanding.
