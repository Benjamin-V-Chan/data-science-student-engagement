import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/engineered_student_engagement.csv")
X = df.drop(columns=["Engagement_Label"])
y = df["Engagement_Label"]

# Load model
model = joblib.load("outputs/engagement_model.pkl")

# Predictions
y_pred = model.predict(X)

# Evaluate performance
print("Accuracy:", accuracy_score(y, y_pred))
print(classification_report(y, y_pred))

# Feature importance
importances = model.feature_importances_
feature_names = X.columns
plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance")
plt.savefig("outputs/feature_importance.png")
plt.show()
