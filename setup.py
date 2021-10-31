def welcome():
    print(
        """
********************************************************************************

 **********                   **       *******                              **  
/////**///                   /**      **/////**                            /**  
    /**      *****  **   ** ******   **     //**  **   **  *****   ****** ******
    /**     **///**//** ** ///**/   /**      /** /**  /** **///** **//// ///**/ 
    /**    /******* //***    /**    /**    **/** /**  /**/*******//*****   /**  
    /**    /**////   **/**   /**    //**  // **  /**  /**/**////  /////**  /**  
    /**    //****** ** //**  //**    //******* **//******//****** ******   //** 
    //      ////// //   //    //      /////// //  //////  ////// //////     // 

********************************************************************************
This is a DEMO version that represents an unfinished project.
********************************************************************************
"""
    )
    pause_for_input()


def instructions():
    print(
        """
        Text Quest DEMO is a short, and simple, demo of a text-based game 
        where you make choices at each location you visit. If you survive 
        all the way, you win. But be warned; you only have one life.
        
        Actions are taken with keyboard inputs. The game will display which 
        keys correspond to which action when making a choice is needed.
        
        You start the game with full health (100), and a basic weapon (short 
        sword) in your inventory. Weapons can degrade and break after using 
        them to attack, buy you can find more in your adventure. There are also
        healing items, and armor items that will reduce the damage you take.
        """
    )
    pause_for_input()


def story():
    print(
        """
        Your town is on the verge of ruin. Crops wither and rot. More and 
        more livestock are found dead every morning. An unknown disease 
        spreads among the populace, claiming lives daily. The townsfolk 
        desperately pray to the gods, unaware of the dark truth the village 
        elders have revealed to you. A powerful sorcerer, worshipper of the
        demon Obzahn, has demanded blood sacrifices for his master. Curses tear
        the lives of your people apart. If this price is not paid, everyone you
        know and love will perish.""")
    
    pause_for_input()

    print(
        """
        The villagers have made a decision. You will not be pawns in the evil 
        one's game. They will send you, their trusted sentinel, on a mission. 
        Your lives will end, unless you are successful in finding 
        and vanquishing your foe. Equipped with only a short sword, 
        you begin a journey full of grave dangers with the hope of saving your 
        people. """)
    pause_for_input()


def pause_for_input():
    print()
    player_input = input("Press Enter to continue: ")
    return


def display_commands():
    pass


def get_help():
    pass
