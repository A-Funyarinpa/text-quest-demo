import setup           
import player
import item
import locations


def game_over():
    pass

           
# first level: village
def level_1():
    if locations.abandoned_village_encounter() == "E".lower():
        # player decides to enter village or not
        choice = locations.abandoned_village_enter()
        if choice.lower() == "a":
            the_player.attack("Ghoul", 1)
            if not the_player.is_dead: 
                level_2()
            else:
                game_over()
        else:
            level_2()
    else:
        level_2()


def level_2():
    # puzzle choice
    choice = locations.chapel_enter()
    if choice == "p":
        locations.chapel_puzzle()
    else:
        locations.puzzle_quit()
    # dinner choice
    choice = locations.chapel_end()
    if choice == "A".lower():
        fight_decision = locations.chapel_dinner()
        if fight_decision == "F".lower():
            locations.chapel_flee()
        elif fight_decision == "G".lower():
            locations.pre_ghoul_fight()
            the_player.attack("Ghouls", 3)
            locations.post_ghoul_fight()
            locations.demo_end()
        else:
            locations.leader_fight()
            locations.demo_end()
    else:
        locations.demo_end()


def game_setup():
    setup.welcome()
    setup.instructions()
    setup.story()
    start_game()


def start_game():
    level_1()


the_player = player.Player()
short_sword = item.Weapon("Sword")
the_player.add_item_to_inventory(short_sword)

game_setup()



