import requests
from bs4 import BeautifulSoup

def print_Games(Games   ):
    #used to print the results to the screen
    #index values  0 & 1 team and score vis
    #index values  2 & 3 team and score home
    #index value 4 status of game
    for Game in Games:
        print (Game[4])
        print (Game[0] + " " + Game[1])
        print (Game[2] + " " + Game[3])
        print ("---------------------------------")
def get_games(teams,scores,status):
#combine all the teams and scores and status into games
    Games = []
    for x in range(len(teams)):
        Game = []
        if x%2 == 0:
            Game.append(teams[x])
            Game.append(scores[x])
            Game.append(teams[x+1])
            Game.append(scores[x+1])
            Games.append(Game)
    for x in range(len(Games)):
        Games[x].append(status[x])
    return Games
def main(url):
   #get the page and collect the teams and scores and status of game
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    g_data = soup.find_all('div',{'class':'game-card-container'})
    Playing_Teams = []
    Score_Teams = []
    Teams_Status = []
    for Game in g_data:
        
        #print ('--------------------')
        Game_Teams = Game.find_all('div',{"class":"team-text-container"})

        for Team in Game_Teams:
            Team_Names = Team.find_all('span')
            Playing_Teams.append(Team_Names[0].text + " " +Team_Names[1].text)



        Game_Scores=Game.find_all('div',{'class':'team-score-container'})
        for score in Game_Scores:
            Score_Teams.append(score.text)
        ## need to get class "final" as well
        Game_Status =Game.find_all('div',{"class":"game-time-start"})
        if Game_Status == []:
            Game_Status =Game.find_all('div',{"class":"final"})
        if Game_Status ==[]:
            Game_Status = Game.find_all('div',{"class":"col-xs-3 scores-game-status"})


        for Status in Game_Status:

            Teams_Status.append(Status.text)
    New_Scores = []
    for x in Score_Teams:
        y = x.strip('\n')
        y = y.strip(' ')
        if len(y) == 0:
            y = "0"
        New_Scores.append(y)
    #print (len(Teams_Status))
    Games = get_games(Playing_Teams,New_Scores,Teams_Status)
    return Games
    #print_Games(Games)
    #for x in range(len(Playing_Teams)):
        #print (Playing_Teams[x] + " " + New_Scores[x])
if __name__=="__main__":
    url ="http://www.sportsnet.ca/baseball/mlb/scores/"
    url2= "http://www.sportsnet.ca/baseball/mlb/scores/?datepicker-date=2015-08-11"
    Games = main(url)
    print_Games(Games)
