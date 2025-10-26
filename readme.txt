# NBA Player Stats Explorer

## Project Overview
This interactive web application allows users to explore NBA player statistics from 1950 to 2024. The app scrapes data from Basketball-Reference.com and presents it in an interactive dashboard built with Streamlit.

## Features
- **Year Selection**: Choose any NBA season from 1950 to 2024
- **Team Filtering**: Filter players by team
- **Position Filtering**: Filter players by position (C, PF, SF, PG, SG)
- **Data Download**: Export filtered data as CSV file
- **Data Visualization**: Generate correlation heatmaps for numeric statistics

## Technical Details
- **Framework**: Streamlit
- **Data Source**: Basketball-Reference.com
- **Libraries Used**:
  - streamlit: Web application framework
  - pandas: Data manipulation and analysis
  - matplotlib & seaborn: Data visualization
  - numpy: Numerical operations
  - base64: Data encoding for file downloads

## Setup Instructions
1. **Clone the repository**

2. **Create and activate a virtual environment**:
   ```
   python -m venv bkt_env
   .\bkt_env\Scripts\activate  # Windows
   ```

3. **Install required packages**:
   ```
   pip install streamlit pandas matplotlib seaborn numpy lxml
   ```
   Note: lxml is required for pandas HTML parsing

4. **Run the application**:
   ```
   streamlit run main.py
   ```

## Usage Guide
1. Select a year from the sidebar dropdown
2. Filter by team and position using the multiselect options
3. View the filtered player statistics in the main panel
4. Download the data as CSV using the download link
5. Generate a correlation heatmap by clicking the "Generate Intercorrelation Heatmap" button

## Data Description
The application displays various player statistics including:
- Points per game (PTS)
- Rebounds per game (TRB)
- Assists per game (AST)
- Field goal percentage (FG%)
- And many more standard basketball metrics

## Troubleshooting
- If data fails to load, check your internet connection
- Ensure all dependencies are installed, especially lxml for HTML parsing
- If the application crashes, try selecting a different year or refreshing the page

## Future Enhancements
- Add player comparison features
- Implement advanced statistics visualization
- Include historical team performance data
- Add player search functionality