import player
import item


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
Welcome to Text Quest
********************************************************************************
"""
    )


def instructions():
    pass


def display_commands():
    pass


def get_help():
    pass


def start_game():
    pass


the_player = player.Player()
short_sword = item.Weapon("Sword")
the_player.add_item_to_inventory(short_sword)
