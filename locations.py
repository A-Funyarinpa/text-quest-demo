import location_texts as texts
import item

# level 1: abandoned_village
def abandoned_village_encounter():
    # encounter text
    texts.abandoned_village_encounter_text()
    # make choice
    print("\nWill you investigate the village? Or continue on your path?",
    "\n")
    print("\nEnter village: 'e' | Continue on: 'c'")
    choice = input("Hit the 'Enter' key to confirm your choice: ")
    while choice not in ["E".lower(), "C".lower()]:
           choice = input("Hit the 'Enter' key to confirm your choice: ")
    return choice


def abandoned_village_enter():
    # enter text
    texts.abandoned_village_enter_text()
    # make choice
    print("\nAttack: 'a' | Flee: 'f'")
    choice = input("\nHit the 'Enter' key to confirm your choice: ")
    while choice not in ["A".lower(), "F".lower()]:
           choice = input("Hit the 'Enter' key to confirm your choice: ")
    return choice

# level 2: chapel
def chapel_enter():
    # enter text
    texts.chapel_enter_text()
    # make puzzle choice
    print("\nAttempt puzzle: p  |  Not attempt puzzle: n  ")
    choice = input("\nHit the 'Enter' key to confirm your choice: ")
    while choice not in ["P".lower(), "N".lower()]:
        choice = input("Hit the 'Enter' key to confirm your choice: ")
    return choice

def create_stones():
    blue_stone = item.ColoredStone("Blue Stone", "Blue")
    green_stone = item.ColoredStone("Green Stone", "Green")
    yellow_stone = item.ColoredStone("Yellow Stone", "Yellow")
    white_stone = item.ColoredStone("White Stone", "White")
    red_stone = item.ColoredStone("Red Stone", "Red")
    black_stone = item.ColoredStone("Black Stone", "Black")
    clear_stone = item.ColoredStone("Clear Stone", "Clear")
    return{
        1: blue_stone,
        2: green_stone,
        3: yellow_stone,
        4: white_stone,
        5: red_stone,
        6: black_stone,
        7: clear_stone
    }

def chapel_puzzle():
    stones = create_stones()
    texts.chapel_puzzle_text()
    puzzle_finished = False
    print("'\nViolence Often Lacks Empathy, Trust'", "\n")
    puzzle_inputs = ["1", "2", "3", "4", "5", "6", "7", "Q".lower()]
    while puzzle_finished != True:
        display_stones(stones)
        puzzle_input = input('\nPress "Enter" to confirm choice: ')
        while puzzle_input not in puzzle_inputs:
            puzzle_input = input('Invalid choice. Try again. Press "Enter" to \
             confirm choice.')
        if puzzle_input == "Q".lower():
            puzzle_finished = True
            puzzle_finish(False)
        else:
            stones[int(puzzle_input)].interact()
            if puzzle_solved_check(stones) == True:
                puzzle_finished = True
                puzzle_finish(True)

def puzzle_solved_check(stones):
    if not stones[1].is_placed and not stones[5].is_placed:
        count = 0
        for val in stones.values():
            if val.is_placed == False:
                count += 1
        if count == 2:
            return True
        else:
            return False
    else:
        return False


def display_stones(stones):
    for counter in range(1, len(stones) + 1):
        if stones[counter].is_placed:
            print("Take " + stones[counter].color + ": " + str(counter),
            end
            = " | ")
        else:
            print("Place " + stones[counter].color + ": " + str(counter),
            end = " | ")
    print("Quit puzzle: q")


def puzzle_finish(is_solved):
    if is_solved:
        texts.puzzle_solved_text()
    else:
        texts.puzzle_quit_text()

def puzzle_quit():
    texts.puzzle_quit_text()

def chapel_end():
    texts.chapel_end_text()
    decision = input("Press 'Enter' to confirm choice: ")
    while decision not in ["A".lower(), "R".lower()]:
        decision = input("Invalid choice. Try again. Press 'Enter' to \
        confirm choice: ")
    return decision

def chapel_dinner():
    texts.dinner_accepted_text()
    decision = input("Press 'Enter' to confirm choice: ")
    while decision not in ["F".lower(), "G".lower(), "L".lower()]:
        decision = input("Invalid choice. Try again. Press 'Enter' to \
        confirm choice: ")
    return decision

def pre_ghoul_fight():
    texts.pre_ghoul_fight_text()

def post_ghoul_fight():
    texts.post_ghoul_fight_text()

def leader_fight():
    texts.leader_fight_text()

def demo_end():
    print("""
         Thank you for checking out this demo! This was a small programming
         practice exercise for a Codecademy course, but someday I plan on
         expanding and finishing this project after I learn more about
         programming.
         """)

def chapel_flee():
    texts.chapel_flee_text()
    demo_end()