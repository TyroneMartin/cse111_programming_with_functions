import matplotlib.pyplot as plt
from unittest.mock import patch
import csv
import datetime
import os

def get_chart_type():
    print("Select chart type:")
    print("1. Bar Chart")
    print("2. Pie Chart")
    print("3. Line Graph")
    while True:
        choice = input("Enter the number corresponding to the chart type: ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_title():
    return input("Enter the title of the chart: ")

def get_labels_and_values():
    while True:
        try:
            num_labels = int(input("Enter the number of labels: "))
            if num_labels <= 0:
                print("Please enter a positive integer for the number of labels.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    labels = []
    values = []
    for i in range(num_labels):
        label = input(f"Enter label {i+1}: ")
        while True:
            try:
                value = float(input(f"Enter value for {label}: "))
                values.append(value)
                labels.append(label)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
    return labels, values

def create_bar_chart(title, labels, values, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.savefig(filename)
    plt.show()

def create_pie_chart(title, labels, values, filename):
    plt.figure(figsize=(10, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.savefig(filename)
    # plt.show()
    plt.close()

def create_line_graph(title, labels, values, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(labels, values, marker='o')
    plt.title(title)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.savefig(filename)
    plt.show()

def save_to_csv(title, labels, values):
    filename = "chart_data_log.csv"
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["-"*40])  # separator line
            writer.writerow([f"Report generated on: {timestamp}"])
            writer.writerow(["Title", title])
            writer.writerow(["Label", "Value"])
            for label, value in zip(labels, values):
                writer.writerow([label, value])
            writer.writerow(["-"*40])  # separator line
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

def main():
    # Create directory for saving images if it doesn't exist
    if not os.path.exists("charts_generated"):
        os.makedirs("charts_generated")
    
    while True:
        try:
            chart_type = get_chart_type()
            title = get_title()
            labels, values = get_labels_and_values()

            image_filename = os.path.join("charts_generated", f"{title.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            
            if chart_type == '1':
                create_bar_chart(title, labels, values, image_filename)
            elif chart_type == '2':
                create_pie_chart(title, labels, values, image_filename)
            elif chart_type == '3':
                create_line_graph(title, labels, values, image_filename)
            
            save_to_csv(title, labels, values)
            print(f"Chart image saved to {image_filename}")
            
            cont = input("Do you want to generate another chart? (yes/no): ").strip().lower()
            if cont != 'yes':
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
