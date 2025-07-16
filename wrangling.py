# Package load
import pandas as pd

# Data load
full = pd.read_csv('data/city_teams.csv', header=None,
                   names=['City', 'MLB', 'NFL', 'NBA', 'NHL'])

# Remove rows with any missing values
full = full.replace(r'^\s*$', pd.NA, regex=True)
full = full.dropna(how='any')

# Fix cities with multiple teams
# Chicago - sorry White Sox fans
full.loc[full['City'] == 'Chicago', 'MLB'] = 'Chicago Cubs'

# New York and Los Angeles
def fix_multiple