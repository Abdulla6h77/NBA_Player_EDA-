import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Title and description
st.title('🏀 NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit, matplotlib, seaborn, numpy
* **Data source:** [Basketball-Reference.com](https://www.basketball-reference.com/)
""")

# Sidebar - Year selection
st.sidebar.header('🔍 User Input Features')
selected_year = st.sidebar.selectbox('Select Year', list(reversed(range(1950, 2025))))

# Web scraping of NBA player stats
@st.cache_data  # ✅ Replace deprecated @st.cache
def load_data(year):
    # ✅ Fixed URL: removed extra spaces
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    
    # Extract tables
    try:
        html = pd.read_html(url, header=0)  # First table
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()
    
    df = html[0]
    
    # Remove repeated headers (where Age == 'Age')
    df = df[df['Age'] != 'Age']
    
    # Drop ranking column and handle NaN
    df = df.drop(['Rk'], axis=1)
    df = df.fillna(0)
    
    # ✅ Clean column names: remove extra spaces
    df.columns = df.columns.str.strip()
    
    return df

playerstats = load_data(selected_year)
st.write("Columns:", playerstats.columns.tolist()) #debuging line

# If no data, stop here
if playerstats.empty:
    st.warning("No data loaded. Check the URL or your internet connection.")
    st.stop()

# ✅ Debug: Show columns (optional, can be removed later)
# st.write("Columns in dataset:", playerstats.columns.tolist())

# Sidebar - Team selection
# ✅ Use .astype(str) in case 'Tm' has mixed types
sorted_unique_team = sorted(playerstats['Team'].astype(str).unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[
    (playerstats['Team'].isin(selected_team)) &
    (playerstats['Pos'].isin(selected_pos))
]

# Display filtered data
st.header('📊 Display Player Stats of Selected Team(s)')
st.write(f'Data Dimension: {df_selected_team.shape[0]} rows and {df_selected_team.shape[1]} columns')
st.dataframe(df_selected_team)

# Download CSV function
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">📥 Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('📈 Generate Intercorrelation Heatmap'):
    st.header('📉 Intercorrelation Matrix Heatmap')
    
    # Select only numeric columns
    numeric_df = df_selected_team.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        st.warning("No numeric columns available for correlation.")
    else:
        corr = numeric_df.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', center=0, ax=ax, fmt='.2f')
        st.pyplot(fig)