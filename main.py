import sys, getopt
from sportsipy.nfl.teams import Team
from sportsipy.nfl.teams import Teams

# Find team code based on substring match to the key within the dictionary
def teamcodes(inp):
    fullnames = {'Arizona Cardinals': 'CRD', 'Atlanta Falcons': 'ATL', 'Baltimore Ravens': 'RAV', 
            'Buffalo Bills': 'BUF', 'Carolina Panthers': 'CAR', 'Chicago Bears': 'CHI', 'Cincinnati Bengals': 'CIN',
            'Cleveland Browns': 'CLE', 'Dallas Cowboys': 'DAL', 'Denver Broncos': 'DEN', 'Detroit Lions': 'DET',
            'Green Bay Packers': 'GNB', 'Houston Texans': 'HTX', 'Indianapolis Colts': 'CLT', 
            'Jacksonville Jaguars': 'JAX', 'Kansas City Chiefs': 'KAN', 'Las Vegas Raiders': 'RAI',
            'Los Angeles Charges': 'SDG', 'Los Angeles Rams': 'RAM', 'Miami Dolphins': 'MIA', 
            'Minnesota Vikings': 'MIN', 'New England Patriots': 'NWE', 'New Orleans Saints': 'NOR',
            'New York Giants': 'NYG', 'New York Jets': 'NYJ', 'Philadelphia Eagles': 'PHI', 
            'Pittsburgh Steelers': 'PIT', 'San Francisco 49ers': 'SFO', 'Seattle Seahawks': 'SEA', 
            'Tampa Bay Buccaneers': 'TAM', 'Tennessee Titans': 'OTI', 'Washington Football Team': 'WAS'}
    res = [val for key, val in fullnames.items() if inp in key]
    #print(res[0])
    return res[0]

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ht:a:", ["team=","all="])
    except getopt.GetoptError:
        print('main.py -t \'<team name>\' -a <all teams>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -t \'<team name>\' -a <all teams>')
            sys.exit()
        elif opt in ("-t", "--team"):
            team = Team(teamcodes(str(arg)))
        elif opt in ("-a", "--all"):
            team == allteams

if __name__ == "__main__":
    main(sys.argv[1:])
