import pandas as pd
from functions import calculate_real_change, calculate_fold_change, calculate_avg_fold_changes

def test_calculate_real_change():
    test_data = pd.DataFrame({
        'dCT': [2, 0, -3],
        'Lines': ['kolf', 'srsf5', 'supt6h_c2']
    })
    expected_real_change = pd.Series([0.25, 1.0, 8.0])
    result_data = calculate_real_change(test_data)
    assert result_data['Real_Change'].equals(expected_real_change), "Real Change calculation failed"

def test_calculate_fold_change():
    test_data = pd.DataFrame({
        'dCT': [2, 0, -3],
        'Lines': ['kolf', 'srsf5', 'supt6h_c2']
    })
    result_data = calculate_real_change(test_data)
    result_data, kolf_avg = calculate_fold_change(result_data)
    expected_fold_change = result_data['Real_Change'] / result_data['Real_Change'][0]
    assert result_data['Fold_Change'].equals(expected_fold_change), "Fold Change calculation failed"

def test_calculate_avg_fold_changes():
    test_data = pd.DataFrame({
        'dCT': [2, 0, -3, -2],
        'Lines': ['kolf', 'srsf5', 'supt6h_c2', 'supt6h_c5']
    })
    result_data = calculate_real_change(test_data)
    result_data, _ = calculate_fold_change(result_data)
    avg_fold_changes = calculate_avg_fold_changes(result_data, ['srsf5', 'supt6h_c2', 'supt6h_c5'])
    assert 'srsf5' in avg_fold_changes, "Average fold change calculation failed for srsf5"
    assert 'supt6h_c2' in avg_fold_changes, "Average fold change calculation failed for supt6h_c2"
    assert 'supt6h_c5' in avg_fold_changes, "Average fold change calculation failed for supt6h_c5"

if __name__ == "__main__":
    test_calculate_real_change()
    test_calculate_fold_change()
    test_calculate_avg_fold_changes()
    print("All tests passed!")
