# Package load
from bs4 import BeautifulSoup
import requests

# Scrape major professional sports teams
url = 'https://www.stadium-maps.com/facts/sports-franchises.html'

# Fetch the page
response = requests.get(url, headers={'User-Agent': 'XY'})
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the teams
table = soup.select('#franchisetable')

# Extract the rows from the table
rows = table[0].find_all('tr')
teams = []
for row in rows[1:]:  
    cols = row.find_all('td')
    team = {
        'City': cols[0].text.strip(),
        'MLB': cols[1].text.strip(),
        'NFL': cols[2].text.strip(),
        'NBA': cols[3].text.strip(),
        'NHL': cols[4].text.strip()
    }
    teams.append(team)

# Save the data to a file
with open('data/city_teams.csv', 'w') as f:
    for team in teams:
        f.write(f"{team['City']}, {team['MLB']}, {team['NFL']}, {team['NBA']}, {team['NHL']}\n")

# Create list of MLB teams
mlb_teams = [team['MLB'] for team in teams if team['MLB']]