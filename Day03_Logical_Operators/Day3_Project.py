print('''                                                     __________
             _,---.                          _..--'/          \
          ,-'      )                    _,-,'     /            \
         (          )               _,-'  /      /              \
          `-.__, -'             _,-/     /     _/ ,------------. \
     ,--._,---.             _,-'  /     /_,--'' | |    Hier    | |
   _(_,-'      )        _,-'/    /_, - '|       | |   koennte  | |
 ,'  (        )      ,'/   /_, -'|      ||_  -  | |    IRRE    | |
(     `--._,-'    _,' /_,-'|     ||_  - |       | |   Werbung  | |
 `--.__,-'     _,'/,-'|  - ||_ - |      ||_  -  | |   stehen!  | |
            _,'/,'|  - ___ |     ||_  - |       | `------------' |
        _ ,' |_' -|- _(   ) |_   |      ||_  -  |                |
       ( ): ((`) -| (. `-/ )   - ||_  - |       |                |
      ` | '(-.,') '( _\`/-') _ - |      | _   - |                |
        `   (_.) -(_._ \|,-_)    ||_  - |       |                |
 .        `. || ` | (_\||_)  _ - |      ||_  -  |                |
             `.    ` . ||  |   - ||_  - |       |                |
                `.     ||-.|  :  |  _   ||_   - |     __________ |
                   `.  ||    ` -.|   |  |   _   |    | _Doener_ |`'--.._
                      `.           ` - .|  | |  |    || ()._o  ||   __ |
\           `            `.   `           ` -' .|____|`'---.|>_||  |. ||
                            `.                         `' -- .._|__|__||
                      ,----.---------- .                            .-_.
   _                 |.`.,' `.           `.                         || |
    \                \ _|`. / `.            `.                      \|_o
     \                | \  `.   \.-----_-----.\     `
      \               `.|.`| `./ \\  c__)___/ \\             .
       \        `         `.   `. \\____\___)__\\
                            `. _ `.\`____________\
                              | \  |_|   ____   |_|
          _                   `.|\ |#|__[jrei]__|_|`.
           \                      `================'  `.

''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure")

direction_input = input("At the crossroad you choose Left or Right ? : ")

direction_input = str.lower(direction_input)

if direction_input != "left":
    print("Fall into a hole. Game Over.")
else:
    action_input = input("Now there is a lake in your path. What you do, Swim or Wait ? : ")
    
    action_input = str.lower(action_input)
    
    if action_input != "wait":
        print("Attacked by trout. Game over !")
    else:
        door_input = input("Encountering a set of doors, which door colour you choose to open ? : ")
        
        door_input  = str.lower(door_input)
        
        if door_input == "red":
            print("Burnt by fire. Game Over !")
        elif door_input == "yellow":
            print("You Win !")
        elif door_input == "blue":
            print("Eaten by beasts. Game Over !")
        else:
            print("Game Over")