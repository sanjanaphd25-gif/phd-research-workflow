import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
input_path = os.path.join("data", "cleaned_data.csv")
output_dir = "results"

def visualize_data():
    # Ensure results directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read cleaned data
    df = pd.read_csv(input_path)

    print("Data Preview:")
    print(df.head())

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) < 1:
        print("No numeric columns found for plotting.")
        return

    # ---- Plot 1: Histogram of first numeric column ----
    plt.figure()
    df[numeric_cols[0]].hist()
    plt.title(f"Histogram of {numeric_cols[0]}")
    plt.xlabel(numeric_cols[0])
    plt.ylabel("Frequency")

    hist_path = os.path.join(output_dir, "temperature_humidity_plot.png")
    plt.savefig(hist_path)
    plt.close()

    # ---- Plot 2: Scatter plot (first two numeric columns if available) ----
    if len(numeric_cols) >= 2:
        plt.figure()
        plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
        plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
        plt.xlabel(numeric_cols[0])
        plt.ylabel(numeric_cols[1])

        scatter_path = os.path.join(output_dir, "score_plot.png")
        plt.savefig(scatter_path)
        plt.close()
    else:
        print("Not enough numeric columns for scatter plot.")

    print(f"Plots saved in '{output_dir}' folder.")

if __name__ == "__main__":
    visualize_data()