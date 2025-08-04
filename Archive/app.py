import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# PAGE SETUP
# ----------------------------
st.set_page_config(page_title="S&P 500 Historical Returns", page_icon=":bar_chart:")

# ----------------------------
# HEADER
# ----------------------------
st.title(":bar_chart: S&P 500 Historical Returns")
st.markdown("""
This app shows a Bloomberg-style heatmap of S&P 500 monthly returns over time.  
A [**Between The Pipes**](https://betweenthepipes.substack.com) app by [Stephan Teodosescu](https://stephanteodosescu.com).
""")

# ------------------------
# Download S&P 500 Data
# ------------------------
sp500 = yf.download('SPY', start='2000-01-01', progress=False)

sp500

# ------------------------
# Calculate Monthly Returns
# ------------------------
monthly_prices = sp500['Close'].resample('M').ffill()
monthly_returns = monthly_prices.pct_change() * 100
monthly_returns = monthly_returns.to_frame(name='Monthly Return')

monthly_returns['Year'] = monthly_returns.index.year
monthly_returns['Month'] = monthly_returns.index.strftime('%b')

# ------------------------
# Pivot to Year-Month Format
# ------------------------
heatmap_data = monthly_returns.pivot_table(index='Year', columns='Month', values='Monthly Return')

# Reorder months
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
heatmap_data = heatmap_data.reindex(columns=month_order)

# ------------------------
# Plot Heatmap in Streamlit
# ------------------------
fig, ax = plt.subplots(figsize=(14, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='RdYlGn', center=0,
            linewidths=0.5, cbar_kws={'label': 'Monthly Return (%)'})
ax.set_title('S&P 500 Monthly % Change Heatmap', fontsize=16)
ax.set_ylabel('Year')
ax.set_xlabel('Month')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

st.pyplot(fig)