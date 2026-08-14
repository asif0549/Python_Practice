class Player:
    def __init__(self,n,c,m):
        self.name=n
        self.country=c
        self.matches=m
        
    def displayPlayerInfo(self):
        print("Player Details:")
        print("="*20)
        print(f"Player Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Matches Played: {self.matches}")
        
class Batsman(Player):
    def __init__(self,n,c,m,ba,tr):
        super().__init__(n,c,m)
        self.battingavg=ba
        self.totalruns=tr
    
    def displayPlayerInfo(self):
        super().displayPlayerInfo()
        print(f"Batting Average: {self.battingavg}")
        print(f"Total Runs: {self.totalruns}")
    
class Bowler(Player):
    def __init__(self, n, c, m, boa, tw):
        super().__init__(n, c, m)
        self.bowlingavg = boa
        self.totalwickets = tw

    def displayPlayerInfo(self):
        super().displayPlayerInfo()
        print(f"Bowling Average: {self.bowlingavg}")
        print(f"Total Wickets: {self.totalwickets}")


class AllRounder(Player):
    def __init__(self, n, c, m, ba, boa):
        super().__init__(n, c, m)
        self.battingavg = ba
        self.bowlingavg = boa

    def displayPlayerInfo(self):
        super().displayPlayerInfo()
        print(f"Batting Average: {self.battingavg}")
        print(f"Bowling Average: {self.bowlingavg}")
        
class Main:
    def main():
        pltype=input("Enter Player Type (Batsman, Bowler, or AllRounder): ").strip()
        if pltype not in ["Batsman", "Bowler", "AllRounder"]:
            print("Invalid Input Please enter only Player Type (Batsman, Bowler, or AllRounder).")
        else:
            name=input("Enter Player Name: ")
            country=input("Enter Country: ")
            matches=int(input("Enter Number of Matches Played: "))


            if pltype =='Batsman':
                battingavg = float(input("Enter Batting Average: "))
                totalruns = int(input("Enter Total Runs: "))
                player = Batsman(name, country, matches, battingavg, totalruns)
                print("="*20)

            elif pltype=='Bowler':
                bowavg=float(input("Enter Bowling Average: "))
                TotalWic=int(input("Enter Total Wickets: "))
                player=Bowler(name,country,matches,bowavg,TotalWic)
                print("="*20)

            else:
                battingavg=float(input("Enter Batting Average: "))
                bowlingavg=float(input("Enter Bowling Average: "))
                player=AllRounder(name,country,matches,battingavg,bowlingavg)
                print("="*20)
            player.displayPlayerInfo()
Main.main()
