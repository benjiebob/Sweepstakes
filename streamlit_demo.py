# Launch with: streamlit run streamlit_demo.py

import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_teams_players():
    teams_players = pd.read_csv("teams_ranking.csv")
    return teams_players

teams_players  = load_teams_players()
teams_players = teams_players.iloc[:, 1:][["Player", "Team", "FIFA World Cup Ranking", "Group", "FIFA World Ranking"]]


st.title("World Cup Qatar 2022 - The Sweepstake")

players = sorted(list(set(teams_players['Player'].to_numpy().tolist())))
selected_player = st.selectbox("Players", options = ["ALL"] + players)

if selected_player == "ALL":
    st.write("Upper Half")
    st.table(teams_players[:16])

    st.write("Lower Half")
    st.table(teams_players[16:])
else:
    teams = teams_players[teams_players["Player"] == selected_player]

    st.write(f"Your World Cup Qatar teams are: ")
    st.table(teams)
    


