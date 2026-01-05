import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/processed_student_engagement.csv")

# Normalize numerical features
scaler = StandardScaler()
num_features = ["Delta_PSD", "Theta_PSD", "Alpha_PSD", "Beta_PSD", 
                "Gamma_PSD", "Pupil_Dilation", "Blink_Rate", 
                "Fixation_Duration", "Saccade_Velocity"]
df[num_features] = scaler.fit_transform(df[num_features])

# Save transformed dataset
df.to_csv("data/engineered_student_engagement.csv", index=False)
