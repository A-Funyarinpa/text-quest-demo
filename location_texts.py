import setup


# level 1
def abandoned_village_encounter_text():
    print("""
         Your path has you passing by the nearest village to yours. It is one 
         you are familiar with. The two villages always celebrate the new year 
         together with a joyous feast.
         """)

    setup.pause_for_input()

    print("""
         As you get closer to the houses, a slight nausea sets in. Your heart 
         feels like it is being gripped. There is no sound to be heard, but 
         there is no feeling of peace. Something is not right. You are 
         struggling with the choice of investigating further, or moving on.
         """)

    setup.pause_for_input()


def abandoned_village_enter_text():
    print("""
          You call out to the villagers in vain. You approach one of the
          nearby houses. Its door its partially open. As you get closer 
          you begin to hear chewing sounds. You enter the house, expecting 
          to find someone to talk to. What you find drains the strength from
          your legs.""")

    setup.pause_for_input()

    print("""
          Something that vaguely resembles a person is devouring a copse.
          You recognize the victim. It is Killian, a young botanist who was
          friendly to all.""")

    setup.pause_for_input()

    print("""
         The creature turns its attention to you. Holding back the urge
         to vomit, you must make a choice. Will you fight? Or will you
         flee? """)


# level 2
def chapel_enter_text():
    print("""
         At the end of the path before lands become unknown lies a large, 
         isolated chapel. It is a custom in your village to ask Saint Yorel 
         and Lady Grecia, the patron saints of safe travels and  good fortunes
         respectively, for a blessing before departing. More than ever you 
         could use some divine protection.""")

    setup.pause_for_input()

    print("""
         You enter to find a cleric lost in thought, staring at one of the 
         nearby candles. She is startled by your greeting. She turns to you 
         and speaks "Child, what brings you here? I have heard whispers of 
         horrors and death today. The roads are unsafe.""")

    setup.pause_for_input()

    print("""
         You tell the cleric about the situation your village is in, and 
         the mission you have undertaken. She stares at the floor and sighs 
         before uttering what sounds like a prayer under her breath. She 
         enters a nearby room, and when she returns she hands you a dagger. 
         "This dagger was used by Saint Mikael when his village was attacked by 
         marauders. He lost his life when the battle was over, but thanks to 
         his valor, none of the other villagers were harmed. As long as this 
         dagger is used in self-defense or protection, it will never break. If 
         your mission is successful, this relic must be returned, understood?" 
         You nod and thank the cleric for the loan.
         """)

    setup.pause_for_input()

    print("""
         Your eye is drawn to a small altar with a row of colored gems below
         beneath an inscription. You ask the cleric what the altar represents,
         but she only offers a smile and a head nod to its direction. You 
         approach it and take a better look. You turn to the cleric and ask if
         this is some sort of puzzle. She nods. "Saint Lucia favors the 
         clever."
        
         Do you want to attempt the puzzle?""")


def chapel_puzzle_text():
    puzzle_solved = False
    print("""
         The inscription reads:
             "Violence Is Often Lacking Empathy, Trust"
        
         A row of 7 colored stones lies beneath the inscription, each one a 
         different color: blue, green, yellow, white, red, black, and clear. 
         They can be removed from their slot, or placed back into it.
        
         Which stone would you like to take/replace?""")


def puzzle_solved_text():
    print("""
         "Finally! Sister Yuri set that up two months ago and no one had
         solved it. Good job. Now claim your reward." """)

    setup.pause_for_input()

    print("""
         The metal plate where the inscription was etched has fallen off
         Behind it is a lies a pendant. You look to cleric Ignacia. She nods 
         and you grab your prize.""")

    setup.pause_for_input()

    print('''"
         "That pendant is said to increase the luck of the wearer if they are 
         courageous. I pray it aids you on your journey," says Ignacia.''')

    setup.pause_for_input()


def puzzle_quit_text():
    print('''
         "Too bad. I hoped you'd be the one to solve it," says Ignatia.''')


def chapel_end_text():
    print("""
         The chapel door opens and in enters a man in religious garbs holding
         bags of supplies. He introduces himself as Olrick. The three of you 
         spend some time talking about your quest. """)

    setup.pause_for_input()

    print("""
         Brother Olrick then offers you a meal and shelter for the night.
         
         Will you accept?
         a = accept   |    r = refuse """)


def dinner_accepted_text():
    print("""
         "You eat bread and fish and pass the next hours talking. Unfortunately
         the night does not remain peaceful. The chapel doors slam open, and in
         walk a group of creatures. There are three ghouls, but leading them 
         is a foe that looks much fiercer, wielding a mace. The leader 
         points towards your group and the ghouls immediately rush towards 
         you.""")

    setup.pause_for_input()

    print("""
         There is no time for planning. You must decide. Will you flee? Or 
         Will you engage the ghouls? Or will you fight the leader?
          
         Flee: f |  Attack ghouls: g  |  Attack leader: l""")


def chapel_flee_text():
    print("""
         You run as fast as you can and evade the ghouls. Their leader 
         swings its mace towards you as you reach the doorway. You leap 
         outside with all your strength and manage to evade it. You 
         sprint forwards, ignoring the screams of those you had befriended.""")


def pre_ghoul_fight_text():
    print("""
         Ignatia and Olrick arm themselves with blades hidden under their 
         robes. "I'll distract the big one and buy you some time," shouts 
         Olrick as he runs to their leader. You engage the ghouls with 
         Ignacia's aid while Olrick gets the leader's attention.
         """)


def post_ghoul_fight_text():
    print("""
         Just as you defeat the ghouls, Olrick cries out in pain as the leader 
         lands a crushing blow to his right side. You and Ignatia sprint 
         towards the leader and attempt to attack from opposing angles. The 
         creature's large size combined with the short range of your weapons
         prevent you from finding a good opening. All you can do is circle 
         around it and keep away.""")

    setup.pause_for_input()

    print("""
         Sensing that this stalemate will persist, the injured Olrick launches
         a surprised attack, digging his blade into your foe's chest. "Now!,"
         yells Olrick. The creature wraps one of his massive hands around 
         Olrick's neck while he swings his mace wildly. You tell Ignatia to 
         approach it from behind as soon as there's a chance, before you rush
         towards Olrick.""")

    setup.pause_for_input()

    print("""
         Olrick uses the blade to inflict as much damage as he can, even as his
         neck is being crushed. You successfully jump over one of the enemy's
         swings, and with well-placed slash of your sword, you cut its left 
         wrist off. As your foe begins its attempt to crush you with its 
         mace, Ignacia jumps on the creatures back, and using all the strength
         she could summon, she drives her blade through its neck. Ignacia is 
         flung to the floor. Your foe staggers, but it still has strength. 
         Before it can mount another attack, you focus all your rage into a 
         strike that targets its weakened neck, beheading it.""")

    print("""
         You kneel near Olrick's body to check on him, but his eyes are 
         lifeless. Once caught in the creature's grip, there was no chance of 
         survival. His windpipe had been crushed. Ignacia hobbles towards you.
         You look at her and hang your head. She falls to her knees next to you
         and sobs.""")


def leader_fight_text():
    print("""
         You signal to Olrick and Ignacia to focus on the ghouls while you 
         head to face their imposing leader. His size and reach are beyond
         anything you've trained for. You survey your surroundings carefully
         as you move, staying away from its powerful swings. """)

    setup.pause_for_input()

    print("""
         Ignacia and Olrich defeat the ghouls and join your battle. All three
         of you form a triangle surrounding your large foe. With patience, 
         you start coordinating openings. In sync, you dodge the villain's 
         attacks and take turns approaching from blind spots to inflict small
         amounts of damage.""")

    setup.pause_for_input()

    print("""
         The creature's swings become wilder, and it lands a crushing blow on
         Olrick's right side. He falls to the ground, yelling in agony. 
         "Olrick!," shouts Ignacia as she begins to run towards him. You see 
         your enemy prepare to crush them both with one swing. You seize the
         opportunity and channel all your focus and strength on a well-placed
         strike that severs your foe's mace-wielding arm. You yell at Ignatia
         to approach from behind when the chance arrives. The enemy is severely
         weakened, but it is not harmless. It's remaining arm is still very
         large, and very strong.""")

    setup.pause_for_input()

    print("""
         You engage your foe carefully. The creature loses its patience and 
         takes a wild swing which you successfully evade. "Now!," you scream. 
         Ignatia jumps on the towering and summoning all of her strength, she 
         drives her blade through its neck. The creature staggers, but it 
         recovers and manages to fling Ignacia to the floor. The enemy starts
         reaching for its mace, but Olrick fights though the pain of his 
         injuries and lunges towards towards the creature's hand, stabbing it 
         with his blade. The opportunity has arrived to finish this. You rush
         towards your foe and channel your rage into a strike targeting its 
         weakened neck. Your foe's head falls on the church's floor, and soon
         after its body as well.""")


