import pandas as pd
import matplotlib.pyplot as plt

# Define file paths for uploaded files in Colab
pre_assessment_path = '/content/PRE ASSESSMENT - 21ST CENTURY SKILLS - results-survey593625.csv'
post_assessment_path = '/content/post_exp_survery.csv'

# Function to read and clean CSV files
def read_and_clean_csv(file_path):
    try:
        # Try reading the CSV file
        data = pd.read_csv(file_path, delimiter=';', encoding='utf-8', on_bad_lines='skip')
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
8
# Load and clean the pre and post assessment data
pre_data = read_and_clean_csv(pre_assessment_path)
post_data = read_and_clean_csv(post_assessment_path)

# Check and print column names after loading the data
if pre_data is not None:
    print("Pre-Assessment Columns:", pre_data.columns.tolist())
if post_data is not None:
    print("Post-Assessment Columns:", post_data.columns.tolist())

# If data is loaded successfully, proceed with visualization
if pre_data is not None and post_data is not None:
    # Clean up column names for both datasets
    clean_columns = {col: col.split('[')[1].split('].')[0] if '[' in col and '].' in col else col for col in pre_data.columns}
    pre_data.rename(columns=clean_columns, inplace=True)

    clean_columns = {col: col.split('[')[1].split('].')[0] if '[' in col and '].' in col else col for col in post_data.columns}
    post_data.rename(columns=clean_columns, inplace=True)

    # Define relevant columns for comparison based on cleaned column names
    skills_columns = ['001', '002', '003', '004', '005']  # Adjusted based on actual cleaned column names

    # Ensure the columns exist in both datasets
    try:
        pre_data = pre_data[skills_columns]
        post_data = post_data[skills_columns]
    except KeyError as e:
        print(f"KeyError: {e}. Please check the column names and try again.")

    # Generate individual histograms for pre and post responses for each skill
    skill_names = ['Critical Thinking', 'Collaboration', 'Communication', 'Creativity']
    file_names = ['Critical_Thinking_Histogram.png', 'Collaboration_Histogram.png', 'Communication_Histogram.png', 'Creativity_Histogram.png']

    for idx, (col, skill_name, file_name) in enumerate(zip(skills_columns, skill_names, file_names)):
        plt.figure(figsize=(10, 5))
        plt.hist(pre_data[col].dropna(), bins='auto', alpha=0.7, rwidth=0.85, color='blue', label='Pre')
        plt.hist(post_data[col].dropna(), bins='auto', alpha=0.7, rwidth=0.85, color='green', label='Post')
        plt.title(f'{skill_name} Pre and Post Assessment')
        plt.xlabel('Response')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig(f'/content/{file_name}')
        plt.show()

    # Display paths for downloading
    for file_name in file_names:
        print(f"{file_name} saved to: /content/{file_name}")
else:
    print("Failed to load data. Please check the CSV files and try again.")
