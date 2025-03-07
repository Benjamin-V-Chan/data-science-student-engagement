import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/processed_student_engagement.csv")

# Summary statistics
print(df.describe())

# Visualize distributions
df.hist(figsize=(10, 8), bins=30)
plt.tight_layout()
plt.savefig("../outputs/feature_distributions.png")

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.savefig("../outputs/correlation_heatmap.png")
plt.show()
