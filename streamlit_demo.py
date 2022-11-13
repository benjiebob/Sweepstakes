# Launch with streamlit run streamlit_demo.py

import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_teams_players():
    teams_players = pd.read_csv("teams_ranking.csv")
    return teams_players

teams_players  = load_teams_players()
teams_players = teams_players.iloc[:, 1:]

st.title("World Cup Qatar 2022 - The Sweepstake")

players = sorted(list(set(teams_players['Player'].to_numpy().tolist())))
selected_player = st.selectbox("Players", options = ["ALL"] + players)

upper_half = teams_players[:16]
lower_half = teams_players[16:]

if selected_player != "ALL":
    upper_half = upper_half[upper_half["Player"] == selected_player]
    lower_half = lower_half[lower_half["Player"] == selected_player]

st.write("Upper Half")
st.dataframe(upper_half)

st.write("Lower Half")
st.dataframe(lower_half)
