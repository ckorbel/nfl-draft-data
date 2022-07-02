from bs4 import BeautifulSoup
import csv
import requests

open_file = open("draft-data.csv", 'w', encoding='utf8')
writer = csv.writer(open_file)

#writer header rows
writer.writerow(['name', 'position', 'original team', 'draft year', 'draft round', 'draft pick', 'max year', 'first team all pro', 'pro-bowls', 'years as primary starter', 'weighted career approximate value', 'value for draft team'])

player_list = []


# note the player_info dict is totally useless and unessecary but to lazy to change it
def get_page_data(url, year):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    players_rows = doc.find_all("tr")
    for player in players_rows: 
        player_info = {}
        csv_row = []
        player_name = player.find("td", attrs={ "data-stat": "player"})
        if not player_name:
            continue
        else:
            player_info["name"] = player_name.text
            csv_row.append(player_info["name"])

        position = player.find("td", attrs={ "data-stat": "pos"})
        player_info["position"] = position.text
        csv_row.append(player_info["position"])

        team = player.find("td", attrs={ "data-stat": "team"})
        player_info["original-team"] = team.text
        csv_row.append(player_info["original-team"])

        csv_row.append(year)

        draft_round = player.find("th", attrs={ "data-stat": "draft_round"})
        player_info["draft-round"] = draft_round.text
        csv_row.append(player_info["draft-round"])

        draft_pick = player.find("td", attrs={ "data-stat": "draft_pick"})
        player_info["draft-pick"] = int(draft_pick.text)
        csv_row.append(repr(player_info["draft-pick"]))

        max_year = player.find("td", attrs={ "data-stat": "year_max" })
        player_info["max-year"] = max_year.text
        csv_row.append(repr(player_info["max-year"]))

        first_team_all_pro = player.find("td", attrs={ "data-stat": "all_pros_first_team"})
        player_info["first-team-all-pro"] = int(first_team_all_pro.text)
        csv_row.append(repr(player_info["first-team-all-pro"]))

        pro_bowls = player.find("td", attrs={ "data-stat": "pro_bowls"})
        player_info["pro-bowls"] = int(pro_bowls.text)
        csv_row.append(repr(player_info["pro-bowls"]))

        years_as_primary_starter = player.find("td", attrs={ "data-stat": "years_as_primary_starter" })
        player_info["years-as-primary-starter"] = int(years_as_primary_starter.text)
        csv_row.append(repr(player_info["years-as-primary-starter"]))

        approximate_value = player.find("td", attrs={ "data-stat": "career_av" })
        try:
            approximate_value = int(approximate_value.text)
        except ValueError:
            approximate_value = 0
        player_info["weighted-career-approximate-value"] = approximate_value
        csv_row.append(repr(player_info["weighted-career-approximate-value"]))

        value_for_draft_team = player.find("td", attrs={ "data-stat": "draft_av"})
        try:
            value_for_draft_team = int(value_for_draft_team.text)
        except ValueError:
            value_for_draft_team = 0
        player_info["value-for-draft-team"] = value_for_draft_team
        csv_row.append(repr(player_info["value-for-draft-team"]))
        player_list.append(player_info)
        writer.writerow(csv_row)


for year in range(1985, 2022):
    print(year)
    url = f'https://www.pro-football-reference.com/years/{year}/draft.htm'
    get_page_data(url, year)


open_file.close()
# print(player_list)

    # print(player_name)

# print(players_rows)  

    # player_name = play.find()
    # print(player)
# prices = doc.find_all("li", { 'class': "draftTable__headline draftTable__headline--player" })
# for player in prices:
#     print(player.text)
# # print(prices)

# with open("index2.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")
# print(tag)