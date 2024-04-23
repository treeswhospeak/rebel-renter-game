import time

lore = []
party = []


def add_lore(x):
    lore.append(x)
    total_wisdom = sum(lore)
    print("Lore gathered. New Wisdom Score: ", str(total_wisdom))


def add_party(x):
    party.append(x)
    total_charisma = sum(party)
    print("Bond forged. New Charisma Score: ", str(total_charisma))


while True:
    print()
    print("- - - - - REBEL RENTERS - - - - -")
    print()

    while True:
        menu = input("1 - Start\n2 - Exit\n")
        if menu == "2":
            print("Goodbye!")
            time.sleep(2)
            exit()
        elif menu == "1":
            break
        else:
            print("Input not recognized, try again!")

    print()
    print(
        """Your current ability scores are:\nCharisma: 0\nWisdom: 0""")
    print()
    print("""Throughout the game, you will gain Charisma as you forge Bonds with characters, and Wisdom as you collect Lore. 
Your accumulated scores will determine your success at the end of the game. Good luck! 
Hit Enter to begin."""), input()
    print("""You wake up on the morning this story begins to see a notice has been slipped under your door. It reads:
        ___________________________________________________________________________________________________________________
        30 DAY NOTICE OF RENT INCREASE
        
        Dear Tenant, 
        
        I am writing to inform you that the rent of all units will be raised effective from the beginning of the upcoming 
        month. The decision to adjust the rent has been made after careful consideration of various factors, including 
        maintenance costs, property taxes, and market trends.  
        
        The monthly rent for your unit will be increased from $950.00 to $1,200.00. This adjustment is in line with the 
        current rental rates in the area and is necessary to ensure the continued upkeep and improvement of the property.  
        
        If you have any questions or concerns regarding this rent increase, please reach out. 
        Office hours are 8am to noon, every Monday & Thursday.  
        
        Thank you for your attention to this matter.  
        Sincerely,
        Donna Graham, Manager
        Pacific Heights Properties
        ___________________________________________________________________________________________________________________""")
    input()
    print("""This isn't the first time you've received a notice like this. In the last 2 years, the rent for your 
one-bedroom apartment has been increasing steadily from its once reasonable cost of $600 a month. With this news, it's 
finally raised to double the original cost, forcing you to find a new place to live by the end of the month.""")
    print()
    print("On that note, you should probably get to work!"), input()
    print("You start walking toward the bus stop and see your neighbor, Mr. Tell, sitting on his porch.")

    while True:
        talk_tell = input("Say good morning? Y/N ").upper()
        if talk_tell == "Y":
            print('You: "Hey, Mr. Tell, how are you today?"'), input()
            print("""Mr. Tell: "Aw man, I'm super bummed, they're trying to get me to give up my house." """), input()
            print("""You: "What, who's 'they?'" """), input()
            print("""Mr. Tell: "My landlord, man! He wants to sell out to that big developer that's been buying up the 
neighborhood and building those shitty condos." """), input()
            print(
                """You: "Oh yeah, my apartment's new owners are raising the rent again, not sure what I'm gonna do." """), input()
            print("""Mr. Tell: "You should try Earthing, man..." """), input()
            print("""Mr. Tell goes on to explain his favorite stress management strategy, which mostly involves laying on 
the ground a lot. When he pauses for breath, you tell him you have to get to work and run for the bus.""")
            print()
            add_lore(3)
            add_party(3)
            input()
            break
        elif talk_tell == "N":
            print("You give him a friendly nod and continue on your way to work.")
            input()
            break
        else:
            print("Input not recognized. Try again! ")

    print("""As you step onto the bus, you exchange a greeting with the driver before taking a seat near the front.
Across from you sits Elisa, a middle-aged Hispanic woman you often share this route with. When she sees you, she
smiles and leans forward to start a conversation."""), input()
    print("""Elisa: "Hi! How's your morning so far?" """), input()

    while True:
        talk_bus = input("Tell her about the rent notice? Y/N ").upper()
        if talk_bus == "Y":
            print("""You: "Well, I'm okay. I got a notice that my rent is going up again and I think I'm gonna finally 
have to move." """), input()
            print("""Elisa: "Oh no, that's too bad. I live a couple streets over and everyone's worried that our rent is 
going to go up, too. I don't know what we'd do, we can barely make ends meet as it is." """), input()
            print("""There's a young woman you haven't met before sitting near the two of you. She takes notice of your 
conversation and joins in."""), input()
            print("""Stranger: "I just moved in and we got a notice this morning, too. My roommates told me it's been 
happening for a while, right?" """), input()
            print("""You: "Yeah, there's definitely a trend." """), input()
            print("""Stranger: "I'm going to have to work more hours if I want to stay here, which will give me less time 
for school." """), input()
            print("""You: "That sucks. It's so frustrating not having any control over the situation." """), input()
            print("""Elisa: "Well, has anyone tried organizing a rent strike?" """)
            print()
            add_lore(10)
            add_party(6), input()
            print("""Rent Strike: A form of protest in which tenants collectively refuse to pay rent to their landlord in 
order to demand changes or concessions."""), input()
            break
        elif talk_bus == "N":
            print("""Elisa tells you a story about something funny her child did before you get off the bus, and the rent 
increase doesn't come up.""")
            break
        else:
            print("Input not recognized. Try again!")

    print("""Later, at work, Ms. Merrill, a regular customer here at Mitchel's, comes to your station with her latest haul
of knitting supplies and a big smile.""")
    print()

    while True:
        print("""Ms. Merrill: "Hi, honey, how you holdin' up today?" """)
        talk_merrill = input("Share your news with her? Y/N ").upper()
        if talk_merrill == "N":
            print("""You: "Oh, I'm fine! Nice colors today, what are you making?" """), input()
            print("""You help Ms. Merrill with her purchase as she tells you all about the project she's working on for her
grandchild.""")
            break
        elif talk_merrill == "Y":
            print("""You: "Oh, I had kind of a rough morning, but seeing you always brightens my day!" """), input()
            print("""Ms. Merrill: "Oh no, what happened this morning?" """), input()
            print(
                """You: "I found out my rent is getting hiked again and it might be my final straw at that place." """)
            input()
            print("She huffs angrily.")
            input()
            print("""Ms. Merrill: "Oh, they just never stop. Well you know me and the ladies in my knitting circle, we got
fed up with being taken advantage of by our landlords, so we all got together and wrote a flurry of letters to the 
editor about it, and that sure scared them, so now we always get our maintenance requests answered right away." """)
            input()
            print("""You: "I wonder if that would work for my neighborhood." """), input()
            print("""Ms. Merrill: "Well you just let me know if you need any help because we've got nothing but time! Why do
you think I'm always in here buying yarn?" """), input()
            add_lore(10)
            add_party(10), input()
            break
        else:
            print("Input not recognized. Try again!")

    while True:
        after_hours = input(
            "After work, you can either spend some time at the bar, or go grocery shopping. B/G ").upper()
        if after_hours == "G":
            print("""On the way home from work you stop at the grocery store, and as you shop you think about how food 
prices have been creeping upwards just like the rent."""), input()
            print("----- in the checkout line -----")
            print("""Cashier: "Hey, did you find what you were looking for?" """), input()

            while True:
                talk_cash = input("Vent to the cashier? Y/N ").upper()
                if talk_cash == "N":
                    print(
                        "You finish buying your groceries, give a nod to the cashier, and head home feeling discouraged.")
                    input()
                    break
                elif talk_cash == "Y":
                    print("""You: "Yeah, I did, but prices sure are going up, huh?" """), input()
                    print("""Cashier: "Yeah, I know, it's unfortunate, but it's operational costs. Our lease just got 
renewed and the rent is higher than ever." """), input()
                    print("""You: "Oh, you too? I'm hearing that's happening all over the neighborhood." """), input()
                    print("""Cashier: "Well, yeah, it's that Pacific Development or whatever, they've been buying everything
up in the area, so they can do whatever they want." """), input()
                    print("""You: "Do you mean Pacific Heights Properties? I didn't realize they owned commercial buildings.
They own my apartment building and our rent just went up, too." """), input()
                    print("""Cashier: "That's the one. It's like they're building a monopoly. Thought that shit was illegal
but I guess not." """), input()
                    add_lore(10)
                    add_party(6)
                    print()
                    print("""As you're leaving the store, you realize that if the neighborhood has a common enemy, maybe the
idea of a rent strike isn't too far-fetched. Armed with a new awareness and sense of community, you go home and
begin to put together a plan."""), input()
                    break
                else:
                    print("Input not recognized. Try again!")

        elif after_hours == "B":
            print("""You decide to get a drink at the local bar after work to blow off some steam. When you get there, it's
fairly empty, so you take a seat at the bar and order a drink."""), input()
            print("""In his usual fashion, the bartender starts making small talk while he pours.""")
            print("""Bartender: "Hey there, how's your day been?" """), input()

            while True:
                talk_bar = input("Talk about your day? Y/N ").upper()
                if talk_bar == "N":
                    print("""Shrugging off the question, you take your drink to a booth and try to unwind from the day, but 
your worries are still forefront in your mind as you head home." """)
                    break
                if talk_bar == "Y":
                    print("""You: "Honestly, it didn't start out great. I got a notice this morning that my rent's being 
raised again. But it's been kind of interesting talking to people about it today. It seems like a lot of us are dealing
with the same thing." """), input()
                    print("""Bartender: "Tell me about it, I hear that all the time. You live in one of those Pacific 
Heights places?" """), input()
                    print("""You: "Yeah, how'd you knokw?" """), input()
                    print("""Bartender: "They own everything around here, man, they keep trying to get me to sell this place
so they want to turn it into some hipster coffee shop or something. There's no way, I'd burn the place to the ground
before I sold out to them." """), input()
                    print("""You: "Ha, well I can't burn my apartment building down, but I was thinking about organizing a 
rent strike." """), input()
                    add_lore(10)
                    add_party(6)
                    print()
                    break

        else:
            print("Input not recognized. Try again!")

        final_score = sum(lore + party)
        if final_score < 32:
            print("""You're back home at the end of the day, not knowing how to move forward, and you get online to start
apartment hunting.""")
            print()

        elif 32 <= final_score <= 58:
            print("""The next day, you show up to Mr. Tell's house with a stack of flyers.""")
            print()

        print("Total points collected: " + str(final_score) + "/58")
        print()
        print("Thanks for playing!")
        time.sleep(5)
        exit()
