import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
file_path = "../data/student_engagement_dataset.csv"
df = pd.read_csv(file_path)

# Encode categorical variables
label_encoders = {}
for col in ["Learning_Content_Type", "Difficulty_Level"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Save processed dataset
df.to_csv("../data/processed_student_engagement.csv", index=False)
