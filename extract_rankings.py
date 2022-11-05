import pandas as pd
import json

# https://www.kaggle.com/datasets/cashncarry/fifaworldranking?resource=download
ranking_data = pd.read_csv("data/fifa_ranking-2022-10-06.csv")
ranking_data = ranking_data[ranking_data["rank_date"] == "2022-10-06"]

# https://www.fifa.com/fifaplus/en/articles/qatar-2022-all-qualified-teams-groups-dates-match-schedule-tickets-more
with open("data/worldcup22_teams.json") as f:
    teams = json.load(f)

teams_df = pd.DataFrame([ 
    (team, group[-1]) for group, team_list in teams.items() for team in team_list
], columns=["Team", "Group"])

teams_ranking_df = teams_df.merge(ranking_data, left_on="Team", right_on="country_full")
teams_ranking_df = teams_ranking_df.sort_values("rank").reset_index()

teams_ranking_df.to_csv("worldcup22_teams_ranking.csv")


print ("Written team/ranking data")