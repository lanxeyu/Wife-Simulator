import os

def clear_screen():
    if os.name == 'posix': # for Unix/Linux/MacOS/BSD
        os.system('clear')
    elif os.name == 'nt': # for Windows
        os.system('cls')




print("""
 ________________________________________
|                                        |
|     WELCOME TO WIFE SIMULATOR V1.0!    |
|________________________________________|
""")

input("         Press 'ENTER' to Start")

clear_screen()

# Initiate variables
maxwifescore = 5
wifescore = 3
lolscore = 5
ending_ok = False

# Define function for displaying wife's hearts status
def wifehearts() :
    print("\n          WIFE ═══ " + ("♥ " * wifescore) + ("♡ " * (maxwifescore - wifescore)) + "═══")

# Define function for displaying the appropriate ending
def ending() :
    if wifescore > 0 :
        wifeending = "Your marriage is safe! For now. "
    elif wifescore <= 0 :
        wifeending = "You have been DIVORCED. "
    
    if lolscore > 3 :
        lolending = "You've also ranked up to Silver! Neat!"
    else :
        lolending = "You're also still stuck in Bronze lmao."
    
    print(wifeending + lolending)

# START Game
wifehearts()
ans = input("""
It's a nice Saturday afternoon. League of Legends is your favorite game that you've been playing for 13 years.
You decided to try and rank up today and so you fire up the game.
You just started playing a ranked match, then your wife calls. What do you do?

a  -  Ignore the phone and keep playing.
b  -  Answer the phone.\n\n> """)
clear_screen()

# START Path a
if ans == "a" :
    wifescore -= 1
    lolscore += 1
    wifehearts()
    ans = input("""
The phone kept ringing for 2 minutes. Your team won the early game easily and have put the enemy team in an extreme power gap.

a  -  Great! Time to push for the enemy base and close out this game!
b  -  Since you're ahead, there's some leeway to call back your wife.\n\n> """)
    clear_screen()

    # START Path aa
    if ans == "a" :
        wifescore -= 1
        lolscore += 1
        wifehearts()
        ans = input("""
You won overwhelmingly and you feel like you can keep going. You check your phone, your wife left message:
'TAKE MEAT OUT.'

a  -  You're on a roll! There's still alot of time before your wife gets home. Get more wins!
b  -  Take the meat out of the freezer.\n\n> """)
        clear_screen()

        # START Path aaa
        if ans == "a" :
            wifescore -= 1
            lolscore += 1
            wifehearts()
            print("""
You kept winning multiple ranked games in a row and lose track of time. Suddenly, there was a loud banging on the door.
Your wife gets home to find that the meat is still in the freezer and you played games all day.\n""")
            ending()
            ending_ok = True
        # END Path aaa

        # START Path aab
        elif ans == "b" :
            wifescore += 1
            wifehearts()
            print("""
Meat successfully extracted. You can now play again without much worry.
Your wife gets home and eyes you with doubt.\n""")
            ending()
            ending_ok = True
        # END Path aab

    # START Path ab
    elif ans == "b" :
        lolscore -= 1
        wifehearts()
        ans = input("""
Your wife tells you to take the meat out of the freezer. 
As you're talking, you didn't notice that multiple enemies were missing from the map.
You get ganked by 3 enemy heroes and die.

a  -  Rage mode! Take out your frustration on your wife and slam down the phone. Keep playing.
b  -  Say OK to your wife, ask her how she is, and take the time to talk to her while you continue to lose game focus.\n\n> """)
        clear_screen()

        # START Path aba
        if ans == "a" :
            wifescore -= 2
            lolscore -= 1
            wifehearts()
            print("\nYour wife gets home to find that the meat is still in the freezer and you played games all day.\n")
            ending()
            ending_ok = True
        # END Path aba

        # START Path abb
        elif ans == "b" :
            wifescore += 1
            lolscore -= 2
            wifehearts()
            print("\nYou take out the meat and continue playing more ranked games. Dinner will be cooked tonight.\n")
            ending()
            ending_ok = True
        # End Path abb


# START Path b    
elif ans == "b" :
    lolscore -= 1
    wifehearts()
    ans = input("""
Your wife tells you to take the meat out of the freezer because that's to be cooked for your dinner.
As this happens, you see your team getting into an early 4v5 teamfight without you. They all die. 
Your teammates have now begun calling you words that can only be found in the Urban Dictionary.

a  -  Rage mode! Yell at your wife for disturbing you then slam the phone down. Blame your teammates for engaging in a fight while outnumbered.
b  -  Say OK to your wife, ask her how she is, and take the time to talk to her while you continue to lose precious early game focus.\n\n> """)
    clear_screen()

    # START Path ba
    if ans == "a" :
        wifescore -= 2
        lolscore -= 2
        wifehearts()
        ans = input("""
You continue to play and eventually lose the ranked match. You feel frustrated.

a  -  Play another game! You have to win!
b  -  Take a break. Call your wife to apologize then take the meat out.\n\n> """)
        clear_screen()
        
        # START Path baa
        if ans == "a" :
            wifescore -= 1
            lolscore -= 2
            wifehearts()
            print("""
All the next matches you played were losses, causing you to descend into further madness.
Your wife gets home to find that the meat is still in the freezer and you played games all day.\n""")
            ending()
            ending_ok = True
        # END Path baa
        
        # START Path bab
        elif ans == "b" :
            wifescore += 1
            lolscore += 1
            wifehearts()
            print("\nYour wife forgives you. Meat is thawing. You now feel refreshed and get back into the game with a clear head.\n")
            ending()
            ending_ok = True
        # END Path bab
    
    # START Path bb
    elif ans == "b" :
        wifescore += 1
        lolscore -= 1
        wifehearts()
        print("\nYou lose the game but take the meat out of the freezer anyway. Your wife will come home to thawed meat.\n")
        ending()
        ending_ok = True
    # End Path bb   

if ending_ok == False :
    print("\nYour PC exploded and your house burned down. The end.")


