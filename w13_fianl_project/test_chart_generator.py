import pytest
import random
import string
import os
import csv
from unittest.mock import patch
import matplotlib.pyplot as plt



# Import the functions to be tested
from chart_generator import (
    get_chart_type,
    get_title,
    get_labels_and_values,
    create_bar_chart,
    create_pie_chart,
    create_line_graph,
    save_to_csv,
    main
)

# Helper function to generate random string
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Helper function to generate random float
def random_float(min=0, max=100):
    return random.uniform(min, max)

@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter([
        '1',  # chart type
        'Test Chart',  # title
        '3',  # number of labels
        'Label1', '10',
        'Label2', '20',
        'Label3', '30',
        'no'  # don't generate another chart
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

@pytest.fixture
def random_chart_data():
    num_labels = random.randint(2, 5)
    labels = [random_string() for _ in range(num_labels)]
    values = [random_float() for _ in range(num_labels)]
    return labels, values

def test_get_chart_type(mock_input):
    assert get_chart_type() == '1'

def test_get_title(mock_input):
    get_chart_type()  # Consume the chart type input
    assert get_title() == 'Test Chart'

def test_get_labels_and_values(mock_input):
    get_chart_type()  # Consume the chart type input
    get_title()  # Consume the title input
    labels, values = get_labels_and_values()
    assert labels == ['Label1', 'Label2', 'Label3']
    assert values == [10.0, 20.0, 30.0]

@pytest.mark.parametrize("chart_func", [create_bar_chart, create_pie_chart, create_line_graph])
def test_create_chart(chart_func, random_chart_data, tmp_path):
    labels, values = random_chart_data
    title = random_string()
    filename = tmp_path / f"{title}.png"
    
    with patch.object(plt, 'show'), patch.object(plt, 'savefig'):  # Mock plt.show and plt.savefig
        chart_func(title, labels, values, str(filename))
    
    # We're not actually saving the file in the test, so we don't check if it exists
    # Instead, we're just ensuring the function runs without errors

def test_save_to_csv(random_chart_data, tmp_path):
    labels, values = random_chart_data
    title = random_string()
    filename = tmp_path / "test_chart_data_log.csv"
    
    with patch('chart_generator.datetime') as mock_datetime, \
         patch('chart_generator.open', create=True) as mock_open, \
         patch('csv.writer') as mock_csv_writer:
        mock_datetime.datetime.now.return_value.strftime.return_value = '2024-07-12 10:00:00'
        save_to_csv(title, labels, values)
        
    mock_open.assert_called_once()
    mock_csv_writer.return_value.writerow.assert_called()

@pytest.mark.parametrize("chart_type", ['1', '2', '3'])
def test_main(chart_type, random_chart_data, tmp_path, monkeypatch):
    labels, values = random_chart_data
    title = random_string()
    
    inputs = iter([
        chart_type,
        title,
        str(len(labels)),
        *[item for pair in zip(labels, map(str, values)) for item in pair],
        'no'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with patch('chart_generator.plt.show'), \
         patch('chart_generator.plt.savefig'), \
         patch('chart_generator.save_to_csv'), \
         patch('os.path.exists', return_value=True), \
         patch('os.makedirs'):
        main()

if __name__ == "__main__":
    pytest.main(["-v", __file__])


    # To run test please use the command: 
    #  pytest test_chart_generator.py