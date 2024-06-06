import os
import threading
import numpy as np
import pandas as pd

def main():
    print("Parliment Election 2024\n")
    sr_no=0
    key=4209
    
    auth=int(input("Enter the key for sart the election: "))
    if auth==key:
        no_voters=int(input("Enter the number of voters: "))
        
        election_data=pd.DataFrame(columns=["sr no","name","voter id","vote"])
        
        for i in range(no_voters):
            print("Parliment election 2024\n")
            sr_no+=1
            name=input("Voter name: ").title()
            voter_id=input("Voter id: ")
            print("For Voting Press No of your Party\n")
            print("BJP:1\nNCP:2\nSHIVSENA:3\n")
            
            vote_option=int(input("Now Vote your party:"))
            if vote_option==1:
                vote="BJP"
            elif vote_option==2:
                vote="NCP"
            elif vote_option==3:
                vote="SHIVSENA"
                
            voter_data=[sr_no,name,voter_id,vote]
            election_data.loc[len(election_data)] = voter_data
            
            if os.name == 'nt':
                os.system("cls")
        auth=int(input("Enter the key for election result: "))
        
        if auth==key:
            print("Getting Results Ready..........\n")
            def result_display():
                print("parliment Election Result 2024\n")
                bjp=(election_data["vote"]=="BJP").sum()
                ncp=(election_data["vote"]=="NCP").sum()
                shivsena=(election_data["vote"]=="SHIVSENA").sum()
                result=max([bjp,ncp,shivsena])
                if result==bjp:
                    print(f"BJP is winner in this election by {bjp} vote")
                elif result==ncp:
                    print(f"NCP is winner in this election by {ncp} vote")
                elif result==shivsena:
                    print(f"Shivsena is winner in this election by {shivsena} vote")
                election_data.to_excel("election_result.xlsx",index=False)   
                
            timer=threading.Timer(4.0,result_display)
            timer.start()
    
    else:
        print("error: invalid auth")
        
if __name__ == '__main__':
    main()