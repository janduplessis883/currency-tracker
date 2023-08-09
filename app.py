import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import streamlit as st

data = pd.read_csv('currency_rates.csv', parse_dates=['Timestamp'])

st.title("Currency Tracker")
st.markdown("Select currencies to compare:")
