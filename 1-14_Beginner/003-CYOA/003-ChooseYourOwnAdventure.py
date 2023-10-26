print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to island of Kilawaia.")
print("Your mission is to find the golden idol and get off this island!\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice = input(
    "As you move up the beach, you see two paths leading into the woods. To the left is a dark path leading deep into the forest. To the right, you see a path leading to a cave in the side of the island's mountain.\nWhich direction do you go? Left or Right? "
).tolower()
if choice == "left":
    choice = input(
        "You walk through the forest path, watching over your shoulder and jumping at every noise. After walking for hours you come across a wide river that cuts the island in two. The river seems to be relatively calm at the moment, though there may be a bridge further up. \nDo you take advantage of the calmer waters and swim for it, or do you continue walking in hopes of a better crossing? Swim or Walk?"
    ).lower()
    if choice == "walk":
        choice = input(
            "You know swimming in an unknown river can be dangerous, so you decide to head further up in hopes of finding a bridge or boat. After following the river for a while you see a bridgehouse leading across the river! Walking inside you see three doors. \nWhich door do you choose? Red, Blue, or Yellow?"
        ).lower()
        if choice == "yellow":
            print(
                "You cautiosly open the yellow door. It's dark inside, but you proceed anyway. Fumbling around in the dark you find a lantern, turning it on reveals a door clearly leading to the bridge. Excited you head to the door to make your escape. As you reach for the door you notice something shiny covered by some old cloth and a mountain of dust. Carefully lifting the sheet you reveal the treasure you came here for: the Idol of Manakili. Snatching the idol you sprint for freedom. Jumping into the plane you turn the engine on and make your escape.\n\nCONGRATULATIONS\nYOU WIN"
            )
        elif choice == "blue":
            print(
                "You cautiosly open the blue door. It's dark inside, but you proceed anyway. The floorboards creak under your weight as you spot a lantern in the corner. Making your way towards the lantern the floorboards groan loudly. You stop moving, hoping your weight isn't too much. Cautiosly, you light the lantern and spot a curious sparkle under a dust covered sheet. You reach for the shimmering prize while the floorboards protest the shifting weight. You lean too far and the aged wood finally gives way. You are swept away by the quickly moving waters of the river, the Idol of Ooanooa slipping from your fingers as you vanish into the abyss.\n\nGAME OVER"
            )
        else:
            print(
                "You cautiosly open the red door. It's dark inside, but you proceed anyway. In the corner of the room you spot a lantern among a pile of refuse. You snag the latern and give it a light. With the room fully illuminated you spot your prize. In the middle of the room lying among dust covered cloth and refuse you see the Idol of Kilawaka. You reach forward, excited to finally be through this experience. Your foot catches on a loose floorboard and you fall forward into the pile, the lantern smashing into the pile of dry old cloth. It instantly ignites and begins engulfing the room. Still holding the idol you slam into the red door trying to make an escape. It's stuck. In your last moments you grip the idol you gave your life for.\n\nGAME OVER"
            )
    else:
        print(
            "You're a strong swimmer, the rivers moving slow enough, and it's only a dozen or so feet across, right? On the other side you even see a village that probably has your prize inside. You wade deep into the water and begin swimming. After a while you realize you're only now reaching the middle of the river, and the current is getting much stronger. You press on, swimming as hard as you can, with the far shore never seeming to get closer. As your arms tire and your lungs burn you slowly sink into the depths of the river. Your time on Kilawaia is over.\n\nGAME OVER"
        )
else:
    print(
        "The cave is dark and wet. You make your way into the cave with what little light you've got. You find what looks to be a set of rocks you could use to make your way further in. As you step down you lose your footing, slipping to your demise into the dark deep cave.\n\nGAME OVER"
    )
