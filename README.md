# data-science-student-engagement

# Project Overview
This project analyzes student engagement using EEG and behavioral data. It involves data preprocessing, exploratory analysis, feature engineering, model training, and evaluation to predict engagement levels based on various physiological signals.

# Folder Structure
```
project-root/
├── data/
│   ├── student_engagement_dataset.csv
│   ├── processed_student_engagement.csv
│   └── engineered_student_engagement.csv
├── scripts/
│   ├── 01_load_and_preprocess.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_feature_engineering.py
│   ├── 04_train_model.py
│   └── 05_evaluate_model.py
├── outputs/
│   ├── feature_distributions.png
│   ├── correlation_heatmap.png
│   ├── engagement_model.pkl
│   ├── feature_importance.png
├── requirements.txt
└── README.md
```

# Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Load and Preprocess Data:
Run the following script to clean and preprocess the dataset:
```bash
python scripts/01_load_and_preprocess.py
```

### 3. Perform Exploratory Data Analysis:
Generate summary statistics and visualizations:
```bash
python scripts/02_exploratory_analysis.py
```

### 4. Feature Engineering:
Standardize numerical features and perform feature selection:
```bash
python scripts/03_feature_engineering.py
```

### 5. Train Model:
Train a RandomForest model on the processed dataset:
```bash
python scripts/04_train_model.py
```

### 6. Evaluate Model:
Assess the model's accuracy, generate classification reports, and visualize feature importance:
```bash
python scripts/05_evaluate_model.py
```

# Requirements
Ensure you have Python 3.x installed. Install dependencies using:
```bash
pip install -r requirements.txt
```

# Acknowledgments
- **Dataset Name:** Student Engagement Dataset  
- **Dataset Author:** Ziya  
- **Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/ziya07/student-engagement-dataset-using-eeg)  