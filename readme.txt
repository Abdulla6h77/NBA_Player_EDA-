🏀 NBA Player Stats Explorer

An interactive Streamlit web app that lets users explore NBA player statistics from 1950 to 2024.
The app scrapes data directly from Basketball-Reference.com
 and visualizes it in an easy-to-use dashboard for quick filtering, analysis, and insights.

🚀 Features

📅 Year Selection: Browse NBA stats for any season between 1950 and 2024
🏟️ Team Filtering: Narrow down players by team
🧍 Position Filtering: Filter by position (C, PF, SF, PG, SG)
💾 Data Download: Export filtered player stats as a CSV file
📊 Data Visualization: Generate intercorrelation heatmaps for numeric statistics

⚙️ Technical Details
Component	Description
Framework	Streamlit
Data Source	Basketball-Reference.com

Libraries Used	streamlit, pandas, numpy, matplotlib, seaborn, base64, lxml
🧩 Setup Instructions
1. Clone the repository
git clone https://github.com/<your-username>/nba-player-stats-explorer.git
cd nba-player-stats-explorer

2. Create and activate a virtual environment
python -m venv bkt_env
# Activate (Windows)
bkt_env\Scripts\activate
# Activate (macOS/Linux)
source bkt_env/bin/activate

3. Install dependencies
pip install streamlit pandas matplotlib seaborn numpy lxml


Note: The lxml library is required for HTML parsing by pandas.

4. Run the application
streamlit run main.py

🧭 Usage Guide

Select a year from the sidebar dropdown
Filter data by team and position
View the filtered player statistics in the main panel
Click Download CSV to export data
Generate an intercorrelation heatmap for deeper analysis

📈 Data Description
The application displays standard NBA player statistics, including:

Metric	Description
PTS	Points per game
TRB	Rebounds per game
AST	Assists per game
FG%	Field goal percentage
3P%, STL, BLK, FT%	Additional basketball performance metrics
🧰 Troubleshooting

⚠️ Data not loading: Check your internet connection
⚙️ Missing dependencies: Ensure all required libraries (especially lxml) are installed
🔁 App crashes or freezes: Try refreshing the page or selecting a different year
🧹 Cache issues: Run streamlit cache clear if data seems outdated
🌟 Future Enhancements
🆚 Player comparison and side-by-side stats
📊 Advanced visualization (e.g., radar charts, trend lines)
🏆 Team performance and historical trends
🔍 Player search and autocomplete functionality
