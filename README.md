# jwar
beginner python game 


use ** > python move.py** to start it. 

presently, the tiny thing can:

    > "generate"  - prompts user for map dimension and generates a list^3 with random place descriptions
    
    > "save"      - saves the map to urMap.jw
    
    > "open"      - attempts to open urMap.jw and load the data
    
    > "n/s/e/w"   - the cardinal direction, as in MUDS or whatever. doesn't support full words, does parse uppercase.
    
    > "l"         - check out your surroundings. may be one of 5 different sentences!
    
    > "map"       - prints the list^4
    
    > "q"         - exits the game


this is meant to be an exercize in map-generation systems. 

personal goals for this:

    * exploiting the z-axis

    * random-walk river carving
    
    * voroni assignment of terrain
    
    * procedural mountain generation
