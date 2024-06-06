import os
import threading
import pandas as pd
import numpy as np

def main():
    print("Parliment Election 2024\n")
    sr_no=0
    key=4209
    auth=int(input("Enter Key for start the election: "))
    if auth==key:
        no_voters=int(input("\nEnter The Numbers Of Voters: "))
    
        election_data=pd.DataFrame(columns=["sr no","Name","Contact","Voter id","Vote"])
        
        for i in range(no_voters):
            print("\nParliment Election 2024")
        
            sr_no+=1
            name=input("\nEnter Voter Name: ").title()
            contact=int(input("Enter Voter Contact: "))
            voter_id=int(input("Enter Voter id: "))
            
            print("For Voting Press No of your Party\n")
            print("BJP:1\nNCP:2\nSHIVSENA:3\n")
            vote_options=int(input("Now Vote Your Party: "))
            if vote_options ==1:
                vote="BJP"
            elif vote_options ==2:
                vote="NCP"
            elif vote_options ==3:
                vote="SHIVSENA"
                
            voter_data=[sr_no,name,contact,voter_id,vote]    
            election_data.loc[len(election_data)] = voter_data
            
            if os.name == 'nt':
                os.system("cls")
    
        auth=int(input("Enter Key for Result of election:  "))
        if auth==key:    
            print("Geting results Ready.....\n")
            def result_display():
                print("Parliment Election 2024\n")
                bjp=(election_data["Vote"]=="BJP").sum()
                ncp=(election_data["Vote"]=="NCP").sum()
                shivsena=(election_data["Vote"]=="SHIVSENA").sum()  
                result=max([bjp,ncp,shivsena])
                if result==bjp:
                    print(f"BJP is winner in this election by {bjp} vote")
                elif result==ncp:
                    print(f"NCP is winner in this election by {ncp} vote")
                elif result==shivsena:
                    print(f"Shivsena is winner in this election by {shivsena} vote")
                election_data.to_excel("election_result.xlsx", index=False)
                
            timer=threading.Timer(4.0,result_display)
            timer.start()
    else:
        print("Error: Authentication Failed.")
        
    
if __name__ == "__main__":
    main()
    
