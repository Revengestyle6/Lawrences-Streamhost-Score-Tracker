from pathlib import Path

# Get folder where the script resides
BASE_DIR = Path(__file__).parent

output_dir = BASE_DIR / 'output'
output_dir.mkdir(exist_ok=True)

score_h_file = output_dir / 'Score (H).txt'
score_a_file = output_dir / 'Score (A).txt'
racecount_file = output_dir / 'racecount.txt'

# stores the points for each spot
mkwWarDict = {"1": 15, "2": 12, "3": 10, "4": 8, "5": 6, "6": 4, "7": 3, "8": 2, "9": 1}

def results(r, pen=0, enemypen=0):
    teamscorerace, enemyscorerace = -int(pen or "0"), -int(enemypen or "0")
    teamscore, enemyscore = int(score_h_file.read_text() or "0"), int(score_a_file.read_text() or "0")
    teamspots, enemyspots = [], []
    for j in range(1, 10):
        if r.count(str(j)) == 1:
            teamscorerace += mkwWarDict[str(j)]
            teamspots.append(j)
        else:
            enemyscorerace += mkwWarDict[str(j)]
            enemyspots.append(j)
    return (str(teamscorerace),str(enemyscorerace),teamspots,enemyspots,pen,enemypen,str(teamscore+teamscorerace),str(enemyscorerace+enemyscore))


def racecount(text):
    racecount_file.write_text(f'Race {str(text)}')
    return(text+1)



def reset():
    score_h_file.write_text("000")
    score_a_file.write_text("000")
    racecount_file.write_text("Race 1")


def status():
    homescore = score_h_file.read_text()
    awayscore = score_a_file.read_text()
    racetext = racecount_file.read_text()
    return homescore, awayscore, racetext