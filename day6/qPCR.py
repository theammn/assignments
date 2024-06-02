#!pip install pandas openpyxl
#!pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'qPCR.xlsx'  # Ensure this file is in the same directory as your notebook
data = pd.read_excel(file_path)  # Skip the first row to align the headers properly
data.head()

# Calculating Delta Ct and ddCT
data['Delta_Ct'] = data['Target'] - data['Reference']
data['Real_Change'] = 2 ** -data['Delta_Ct']

# Filtering for KOLF samples to calculate the average Real Change
kolf_data = data[data['Lines'] == 'kolf']
kolf_avg = kolf_data['Real_Change'].mean()
data['Fold_Change'] = data['Real_Change'] / kolf_avg
print(f"KOLF Average Real Change: {kolf_avg}")

# Calculate the average fold change for target lines
srsf5_lines = data[data['Lines'].str.contains('srsf5')]
srsf5_avg_fold_change = srsf5_lines['Fold_Change'].mean()
supt6hc2_lines = data[data['Lines'].str.contains('supt6h_c2')]
supt6hc2_avg_fold_change = supt6hc2_lines['Fold_Change'].mean()
supt6hc5_lines = data[data['Lines'].str.contains('supt6h_c5')]
supt6hc5_avg_fold_change = supt6hc5_lines['Fold_Change'].mean()
print(f"Average Fold Change for SUPT6Hc5 lines: {supt6hc5_avg_fold_change}")
print(f"Average Fold Change for SUPT6Hc2 lines: {supt6hc2_avg_fold_change}")
print(f"Average Fold Change for SRSF5 lines: {srsf5_avg_fold_change}")

#Plot the results
kolf_FC = 1
# Data for plotting
categories = ['KOLF', 'SRSF5', 'SUPT6Hc2', 'SUPT6Hc5']
values = [kolf_FC, srsf5_avg_fold_change, supt6hc2_avg_fold_change, supt6hc5_avg_fold_change]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'red', 'green', 'orange'])
plt.xlabel('Lines')
plt.ylabel('Average Fold Change')
plt.title('Comparison of Average Fold Change Across Different Lines')
plt.show()
