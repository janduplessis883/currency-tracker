import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import streamlit as st

data = pd.read_csv('currency_rates.csv', parse_dates=['Timestamp'])

st.title("Currency Tracker")
st.markdown("Select currencies to compare:")






# Filter data for the last 2 hours
two_hours_ago = datetime.now() - timedelta(hours=2)
last_two_hours_data = data[data['Timestamp'] >= two_hours_ago]

fig, axs = plt.subplots(2, 2, figsize=(16, 10)) # Adjust the figure size as necessary

# Plot all data
sns.lineplot(data=data, x='Timestamp', y='GBP', ax=axs[0, 0], color='#d00000', label='GBP')
sns.lineplot(data=data, x='Timestamp', y='USD', ax=axs[0, 1], color='#023e8a', label='USD')

# Plot last 2 hours data
sns.lineplot(data=last_two_hours_data, x='Timestamp', y='GBP', ax=axs[1, 0], linewidth=3, color='#e85d04', label='GBP')
sns.lineplot(data=last_two_hours_data, x='Timestamp', y='USD', ax=axs[1, 1], linewidth=3, color='#0096c7', label='USD')

# Titles for all data
axs[0, 0].set_title('All GBP Exchange Rate (Base EUR)')
axs[0, 1].set_title('All USD Exchange Rate (Base EUR)')

# Titles for last 2 hours data
axs[1, 0].set_title('Last 2 hours GBP Exchange Rate (Base EUR)')
axs[1, 1].set_title('Last 2 hours USD Exchange Rate (Base EUR)')

# Rotate x-tick labels and show grid for all subplots
for ax in axs.flat:
    ax.xaxis.set_tick_params(rotation=45)
    ax.grid(axis='y', linestyle='-', linewidth=0.5, alpha=0.5)
    ax.legend()

plt.tight_layout()
st.pyplot(fig)
