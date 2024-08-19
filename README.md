# Survey Tool for Income Spending Analysis

## Setup Instructions

1. Install Python 3 and pip.
2. Install required packages:
   ```bash
   pip install flask pymongo pandas matplotlib
   ```
3. Start the Flask application:
   ```bash
   flask run
   ```
4. Access the web application via `http://localhost:5000` to submit data.
5. Run `data_processing.py` to export MongoDB data to CSV.
6. Load the CSV file in `data_analysis.ipynb` for visualization.
7. Export charts for use in presentations.
