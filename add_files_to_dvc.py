import os

folder_list = ["Training_Batch_Files", "Prediction_Batch_Files"]
for folder in folder_list:
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder, filename)
            os.system(f"dvc add {file_path}")