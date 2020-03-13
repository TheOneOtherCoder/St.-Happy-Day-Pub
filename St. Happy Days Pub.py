def start():
    AGE_LIMIT = 18
    StHappyDaySpecialBrew = float(40)
    ClassicGuiness = float(25)
    OldFashionedBrew = float(10)
    QuickShotGlass = float(5)
    FriendStat = 0
    HP = 100
    AlchoholLVL = 0
    age = int(raw_input("Welcome to the St. Happy Days Pub, how old are ya? >> "))
    if age < AGE_LIMIT:
        print ("Sorry kid, but " + str(age) + " is below the age limit. Come back when ya older and start counting, cause you got " + str(18 - age) + " years left.")
    else:
        print ("Welp, " + str(age) + " is old enough. Come on in and have a good time.")
        print ("You enter the pub and walk up to the bar, you look at the menue to see what you can get.")
        print ("1 = St. Happy Day Special Brew")
        print ("2 = Classic Guiness")
        print ("3 = Old Fashioned Brew")
        print ("4 = The Quick Shot Glass")
        Beverage = (raw_input("Hello there, what would you like to have today sir? >> "))
        if Beverage in (str("1")):
            print ("The St. Happy Day Special Brew, a man in great taste I see. That will be $" + "%.2f" %(StHappyDaySpecialBrew))
            AlchoholLVL = (AlchoholLVL + 50)
            print ("Your AlchoholLVL raised by 50. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
        elif Beverage in (str("2")):
            print ("A classic guiness, an amazing standard drink. That will be $" + "%.2f" %(ClassicGuiness))
            AlchoholLVL = (AlchoholLVL + 30)
            print ("Your AlchoholLVL raised by 30. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
        elif Beverage in (str("3")):
            print ("The Old Fashioned Brew, quite the simple looking beverage, but it sure packs a kick. That will be $" + "%.2f" %(OldFashionedBrew))
            AlchoholLVL = (AlchoholLVL + 70)
            print ("Your AlchoholLVL raised by 70. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
        elif Beverage in (str("4")):
            print ("Ah, the quick shot, a perfect choice for people new to drinking. That will be $" + "%.2f" %(QuickShotGlass))
            AlchoholLVL = (AlchoholLVL + 10)
            print ("Your AlchoholLVL raised by 10. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
        print ("You pull out you wallet and give the bartender the money. You take the drink from the bartender and look around the pub.")
        print ("You see some areas you could check out")
        print ("1 = Pool Tables")
        print ("2 = Group of Men")
        print ("3 = Bowling Alley")
        print ("4 = Juke Box")
        AreaFirst = raw_input("Which area would you like to check out first? >> ")
        if AreaFirst in (str("1")):
            print ("There are some men playing a game. They appear to not know what they're doing. You would make fun of them to yourself, but you also don't know how to play pool.")
        elif AreaFirst in (str("2")):
            print ("They have leather jackets and matching tattoos, I wouldn't mess with them.")
        elif AreaFirst in (str("3")):
            print ("You have no idea why a bar would have a bowling alley, but drunk bowling could be fun to watch.")
        elif AreaFirst in (str("4")):
            print ("You wonder over to the juke box. It's broken, but the sticker on it says it's a 'Harper's Juke Box'.")
        print ("You head back to the bar and figure out what you want to check out now")
        
        AreaSecond = raw_input("Which area would you like to check out now >> ")
        if AreaSecond in (str("1")):
            print ("There are some men playing a game. They appear to not know what they're doing. You would make fun of them to yourself, but you also don't know how to play pool.")
        elif AreaSecond in (str("2")):
            print ("They have leather jackets and matching tattoos, I wouldn't mess with them.")
        elif AreaSecond in (str("3")):
            print ("You have no idea why a bar would have a bowling alley, but drunk bowling could be fun to watch.")
        elif AreaSecond in (str("4")):
            print ("You wonder over to the juke box. It's broken, but the sticker on it says it's a 'Harper's Juke Box'.")
        print ("You head back to the bar and figure out what you want to check out now")
        
        AreaThird = raw_input("What's the third thing you would like to look at? >> ")
        if AreaThird in (str("1")):
            print ("There are some men playing a game. They appear to not know what they're doing. You would make fun of them to yourself, but you also don't know how to play pool.")
        elif AreaThird in (str("2")):
            print ("They have leather jackets and matching tattoos, I wouldn't mess with them.")
        elif AreaThird in (str("3")):
            print ("You have no idea why a bar would have a bowling alley, but drunk bowling could be fun to watch.")
        elif AreaThird in (str("4")):
            print ("You wonder over to the juke box. It's broken, but the sticker on it says it's a 'Harper's Juke Box'.")
        print ("You head back to the bar and figure out what you want to check out now")
        
        AreaFourth = raw_input("What's the final thing you would like to look at? >> ")
        if AreaFourth in (str("1")):
            print ("There are some men playing a game. They appear to not know what they're doing. You would make fun of them to yourself, but you also don't know how to play pool.")
        elif AreaFourth in (str("2")):
            print ("They have leather jackets and matching tattoos, I wouldn't mess with them.")
        elif AreaFourth in (str("3")):
            print ("You have no idea why a bar would have a bowling alley, but drunk bowling could be fun to watch.")
        elif AreaFourth in (str("4")):
            print ("You wonder over to the juke box. It's broken, but the sticker on it says it's a 'Harper's Juke Box'.")
        print ("You head back to the bar and figure out what to do after looking at what you wanted to.")
        
        LeaveBar = raw_input("Would you like to leave the bar right now? (1 = yes 2 = no) >> ")
        if LeaveBar in (str("1")):
            print ("You leave the bar and will come back another day. ENDING 1 of 7: EARLY DEPARTING")
        else:
            print ("After some thinking, you decide that the St. Happy Day Pub is good enough to stay for a little bit longer.")
            print
            print ("You notice one of your friends at a table. You think about going to greet him")
            FriendChoice = raw_input("Do you greet your friend? (1 = yes 2 = no) >> ")
            if FriendChoice in (str("2")):
                print ("You decide to not greet your friend.")
            if FriendChoice in (str("1")):
                print ("You decided to greet your friend. You had a nice chat and seemed to have raised his spirits. Your Friend stat has increased by 1.")
            FriendStat = (FriendStat + 1)
            print
            print ("You went to the bowling alley to see if anyone way playing a game. You spotted a group of people playing, (Well, as close as playing possible while being drunk), and you question whether or not to join them")
            BowlingGame = raw_input("Would you like to play a game with the drunk group? (1 = yes 2 = no) >> ")
            if BowlingGame in (str("1")) and FriendStat > 0:
                print ("You played a game with the drunken group. You laughed a lot because almost every time they went to roll they almost fell over. You even got your friend to join you. Both of you had a lot of fun")
            elif BowlingGame in (str("1")):
                print ("You played a game with the drunken group. You laughed a lot because almost every time they went to roll they almost fell over.")
            if BowlingGame in (str("2")):
                print ("You decided to not join them in fear that they might throw the bowling ball at you by mistake.")
                print
            print ("After a bit you get bored. You want to do something before you are overtaken by boredom.")
            print ("You look over towards the bar and find a group of men and think about fighting them.")
            Fightthem = raw_input("Would you like to attempt to fight the group of men? (1 = yes 2 = no) >> ")
            if Fightthem in (str("1")):
                print "You attempted to fight the men and ended up getting clobbered (AKA: you lost the fight, real bad). Your HP dropped down by 100."
                HP = (HP - 100)
                print ("Your HP is now " + str(HP))
                if HP <= 0:
                    print ("You ran out of health. You were sent to the hospital. ENDING 2 of 7: Beaten Down")
            if Fightthem in (str("2")):
                print "You made the right choice and decided to not fight the group of men. Instead, you decided to play some solo pool."
            elif Fightthem in (str("2")) and FriendStat > 0:
                print "You made the right choice and decided to not fight the group of men. Instead, you decided to play some pool with your friend."
            print
            print ("After playing a game of pool you found out it just took that game to clear the boredom out of your mind.")
            print ("You head to the bar. Thirsty, you go to a drink. Be careful though, your AlchoholLVL limits your choices.")
            print ("As you head to the bar counter, the bartender says the same thing as before.")
            print ("1 = St. Happy Day Special Brew")
            print ("2 = Classic Guiness")
            print ("3 = Old Fashioned Brew")
            print ("4 = The Quick Shot Glass")
            Beverage = (raw_input("Hello there, what would you like to have today sir? >> "))
            if Beverage in (str("1")):
                print ("The St. Happy Day Special Brew, a man in great taste I see. That will be $" + "%.2f" %(StHappyDaySpecialBrew))
                AlchoholLVL = (AlchoholLVL + 50)
                print ("Your AlchoholLVL raised by 50. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                if AlchoholLVL >= 100:
                        print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
            if Beverage in (str("2")):
                print ("A classic guiness, an amazing standard drink. That will be $" + "%.2f" %(ClassicGuiness))
                AlchoholLVL = (AlchoholLVL + 30)
                print ("Your AlchoholLVL raised by 30. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                if AlchoholLVL >= 100:
                        print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
            if Beverage in (str("3")):
                print ("The Old Fashioned Brew, quite the simple looking beverage, but it sure packs a kick. That will be $" + "%.2f" %(OldFashionedBrew))
                AlchoholLVL = (AlchoholLVL + 70)
                print ("Your AlchoholLVL raised by 70. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                if AlchoholLVL >= 100:
                        print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
            if Beverage in (str("4")):
                print ("Ah, the quick shot, a perfect choice for newcomers. That will be $" + "%.2f" %(QuickShotGlass))
                AlchoholLVL = (AlchoholLVL + 10)
                print ("Your AlchoholLVL raised by 10. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                if AlchoholLVL >= 100:
                        print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
            if AlchoholLVL < 100:
                print
                print ("After a nice drink, you check your watch and see that it's 9:57 PM. You want to stay at the bar a little longer but going home now would be a good idea.")
                print ("1 = yes  2 = no")
                leavenow = raw_input("Do you want to leave the bar now? >> ")
                if leavenow in (str("1")):
                    print ("You decided to head home. Now the big question, how do you get home?")
                    print ("You know that you can get your car in the morning and you can get an Uber ride, but you could also just drive your own car.")
                    print ("Be careful, AlchoholLVL can affect your choices")
                    print ("Your AlchoholLVL is " + str(AlchoholLVL))
                    howtogo = raw_input("How do you want to go home? 1 = drive your own car 2 = Uber >> ")
                    if howtogo in (str("1")) and AlchoholLVL >80:
                        print ("You drove your own car but crashed your car on the way home. You were sent to the hospital. ENDING 4 of 7: Crash Ending")
                    elif howtogo in (str("1")):
                        print ("You drove your own car and made it safely home. ENDING 5 of 7: Safe Way Back")
                    if howtogo in (str("2")):
                        print ("You took an Uber home. Luckily they were not creepy or the type who tries to socialize when no one wants to. ENDING 5 of 7: Safe Way Back")
                if leavenow in (str("2")):
                    print "You decided that you can stay longer. You are thirsty, so you head to the bar again to get another drink."
                if AlchoholLVL > 80:
                    print ("As you head over to the bar, the bartender says that you have had too much to drink")
                    print ("The bartender was kind enough to pay for an Uber to send you back home. ENDING 5 of 7: Safe Way Back")
                else:
                    print ("I think you already know how this will work. Just do not go over 100. Got it, good")
                    print ("1 = St. Happy Day Special Brew")
                    print ("2 = Classic Guiness")
                    print ("3 = Old Fashioned Brew")
                    print ("4 = The Quick Shot Glass")
                    Beverage2 = (raw_input("Hello there, what would you like to have today sir? >> "))
                    if Beverage2 in (str("1")):
                        print ("The St. Happy Day Special Brew, a man in great taste I see. That will be $" + "%.2f" %(StHappyDaySpecialBrew))
                        AlchoholLVL = (AlchoholLVL + 50)
                        print ("Your AlchoholLVL raised by 50. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                        if AlchoholLVL >= 100:
                            print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
                    if Beverage2 in (str("2")):
                        print ("A classic guiness, an amazing standard drink. That will be $" + "%.2f" %(ClassicGuiness))
                        AlchoholLVL = (AlchoholLVL + 30)
                        print ("Your AlchoholLVL raised by 30. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                        if AlchoholLVL >= 100:
                            print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
                    if Beverage2 in (str("3")):
                        print ("The Old Fashioned Brew, quite the simple looking beverage, but it sure packs a kick. That will be $" + "%.2f" %(OldFashionedBrew))
                        AlchoholLVL = (AlchoholLVL + 70)
                        print ("Your AlchoholLVL raised by 70. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                        if AlchoholLVL >= 100:
                                print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
                    if Beverage2 in (str("4")):
                        print ("Ah, the quick shot, a perfect choice for newcomers. That will be $" + "%.2f" %(QuickShotGlass))
                        AlchoholLVL = (AlchoholLVL + 10)
                        print ("Your AlchoholLVL raised by 10. Reach 100 and times won't be good. AlchoholLVL = " + str(AlchoholLVL))
                        if AlchoholLVL >= 100:
                                print ("Oh no, your AlchoholLVL became to high. You were taken to the hospital to be treated. ENDING 3 of 7: A Bit Too Much To Drink")
                    if AlchoholLVL < 100:
                        print
                        print ("You are most likely drunk at this point and I am running out of ideas of how to continue this game.")
                        print ("So, I will ask you this one question for the final 2 endings")
                        print ("Do you want to leave now 1 = yes 2 = no")
                        leaveattheend = raw_input("Do you want to leave? >> ")
                        if leaveattheend in (str("1")):
                            print ("Finally, you have come to your senses. You headed home via Uber and everything ended well. ENDING 6 of 7: GO HOME YOU'RE DRUNK")
                        if leaveattheend in (str("2")):
                            print ("Ok then fine. *Sigh*. You decided to stay even though you are about dead from alchohol posioning and you may get knocked out because you decided to fight the group of men. ENDING 7 of 7: You Stupid Drunken Idiot")
                            endscreen = raw_input("Continue? 1 = yes 2 = no >> ")
                            if endscreen in (str("1")):
                                print ("There is nothing left")
                                endscreen1 = raw_input("Continue? >> ")
                                if endscreen1 in (str("1")):
                                    print ("There is nothing left")
                                    endscreen2 = raw_input("Continue? >> ")
                                    if endscreen2 in (str("1")):
                                        print ("There is nothing left")
                                        endscreen3 = raw_input("Continue? >> ")
                                        if endscreen3 in (str("1")):
                                            print ("You really wanna see how far you can push me, don't you. I told you already, nothing is left. The game is over and you got your final ending. Stop trying to continue")
                                            endscreen4 = raw_input("Continue? >> ")
                                            if endscreen4 in (str("1")):
                                                print ("What did I just say? You went through the same screen for the 5th time now. You can see nothing is here. Give up now")
                                                endscreen5 = raw_input("Continue? >> ")
                                                if endscreen5 in (str("1")):
                                                    print ("You know what. I'm tired of you trying to push a completed game past it's limit. I spent so much time to make this and now you want even more. Do you KNOW how many variables I had to make for this game to work? TOO MANY. So please, stop")
                                                    endscreen6 = raw_input("Continue? 2 = no >> ")
                                                    if endscreen6 in (str("1")):
                                                        print ("Fine, if you're going to be this determined to get something new from this program, then I'll give you a secret ending (OUT OF PITY). Enjoy your useless ending. ENDING 8 of 7: A PITY SECRET")
                                                    else:
                                                        print ("Thanks for finally listening")
                                                else:
                                                    print ("Thanks for understanding, goodbye")
                                            else:
                                                print ("Thanks for not pushing my buttons any further")
                                        else:
                                            print ("Thanks for playing, goodbye")
                                    else:
                                        print ("Thanks for playing, goodbye")
                                else:
                                    print ("Thanks for playing, goodbye")
                            else:
                                print ("Thanks for playing, goodbye")