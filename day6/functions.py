import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load qPCR data from an Excel file."""
    data = pd.read_excel(file_path)
    return data

def calculate_real_change(data):
    """Calculate Real Change."""
    data['Real_Change'] = 2 ** -data['dCT']
    return data

def calculate_fold_change(data):
    """Calculate Fold Change with respect to KOLF samples."""
    kolf_data = data[data['Lines'] == 'kolf']
    kolf_avg = kolf_data['Real_Change'].mean()
    data['Fold_Change'] = data['Real_Change'] / kolf_avg
    return data, kolf_avg

def calculate_avg_fold_changes(data, lines):
    """Calculate average fold change for specific lines."""
    avg_fold_changes = {}
    for line in lines:
        line_data = data[data['Lines'].str.contains(line)]
        avg_fold_changes[line] = line_data['Fold_Change'].mean()
    return avg_fold_changes

def plot_fold_changes(categories, values):
    """Plot the fold change values for different lines."""
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'red', 'green', 'orange'])
    plt.xlabel('Lines')
    plt.ylabel('Average Fold Change')
    plt.title('Comparison of Average Fold Change Across Different Lines')
    plt.show()

if __name__ == "__main__":
    file_path = 'qPCR.xlsx'
    data = load_data(file_path)
    data = calculate_real_change(data)
    data, kolf_avg = calculate_fold_change(data)
    avg_fold_changes = calculate_avg_fold_changes(data, ['srsf5', 'supt6h_c2', 'supt6h_c5'])
    
    print(f"KOLF Average Real Change: {kolf_avg}")
    for line, avg in avg_fold_changes.items():
        print(f"Average Fold Change for {line.upper()} lines: {avg}")
    
    # Data for plotting
    categories = ['KOLF'] + list(avg_fold_changes.keys())
    values = [1] + list(avg_fold_changes.values())
    
    # Plotting
    plot_fold_changes(categories, values)
