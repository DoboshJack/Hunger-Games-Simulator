#AUTHOR: Jack Dobosh

import random
CharList = [0, 1, 2, 3, 4]
Store = []
Nugget = []
DayNum = 1
Kill = ["steps on a mine by the cornucopia and is vaporized in seconds\n\n",

       "eats a poisonous Chom Chom and dies\n\n",

       "is swallowed whole by Ahmad Abdallah.\n\n",

       "gets Rick Rolled to death.\n\n",

       "just dies\n\n",

       "gets struck by lightning\n\n",

       "Drinks hecka soma and becomes indra (Dies)\n\n",

       "is discovered to be a federal criminal and sworn enemy of the "
       "Capital and has a giant boulder dropped on them.\n\n",

       "is killed by the notoriously vicious butterfly beaver wielding "
       "a butterfly knife.\n\n",

       "is tickled to death by a native tribe of rabid chickens.\n\n",

       "eats a grenade thinking it was a chom chom... an honorable death.\n\n",

       "is so convinced that they are 'pickle rick' that they actually "
       "transform into a pickle and are eaten by another competitor.\n\n",

       "encounters a wild berry that turns out to be almost as vile and "
       "poisonous than your average white person and dies instantly.\n\n",

       "sneaks over to the cornucopia and finds a used bandaid which they "
       "use for a light snack. Unfortunately this light snack gives them fatal "
       "diarrhea.\n\n",

       "finds the ancient Egyptian Shrine of Ra, which teleports them to a "
       "pocket dimension where every atom in their body is simultaneously "
       "split into 100 billion pieces.\n\n",

       "is tickled to death by the Venus Tickle Trap.\n\n",

       "is distracted by a Learn Python textbook and is stabbed from behind "
       "with a very sharp boolean by another competitor.\n\n",

       "encounters the Grinch who shrinks their heart to the point where "
       "it can no longer pump blood to their entire body. Yipee!!\n\n",

       "encounters Donald Trump and is beaten to death by his tiny baby hands.\n\n",

       "trips and falls onto a pointy rock. (And dies) Whoopsie!! :'(\n\n"]
Live = ["finds a butter knife in the cornucopia and manages to fend off"
       " the other contenders.\n\n",

       "hides in a magical bush for the night.\n\n",

       "jukes out the other competitors and cooks a wild rabbit for "
       "supper.\n\n",

       "builds a fire and 'accidentally' burns down the entire forest "
       "and somehow survives.\n\n",

       "eats a stale Chicken McNugget which gives them, temporary "
       "invincibility.\n\n",

       "takes control of the Cornucopia and devours various nitrogen "
       "rich berries.\n\n",

       "becomes an entrepreneur and starts a laundromat/dry-cleaning business\n\n",

       "gets laundry done at another competitor's laundromat\n\n",

       "hides in a tree for the night.\n\n",

       "skins a wild beaver and devours it's succulent flesh.\n\n",

       "finds a chicken tree and harvests its sweet chicken nectar.\n\n",

       "finds a wild Dwayne 'The Rock' Johnson and Dwayne becomes their "
       "eternal companion.\n\n",

       "survives a close call with a spilled cup of coffee.\n\n",

       "finds a cave and uses it as shelter for the night.\n\n",

       "falls deeply in love with a random no name competitor and uses "
       "it to mooch money out of viewers.\n\n",

       "loses left foot in a minor shoe manufacturing incident\n\n",

       "finds a nerf super-soaker thunderstorm\n\n",

       "digs a hole\n\n",

       "receives the gift of flowers and a good luck letter from their "
       "sponsor and immediately uses it for food.\n\n"]
print("\n =============================== \n\n WELCOME TO THE ONE, THE ONLY...\n\n 0  0  0  0  0  0  0000"
     "  0000  0000\n"
     " 0  0  0  0  00 0  0     0     0  0\n 0000  0  0  0 00  0 00  000   000 \n 0  0  0  0  0  0  0"
     "  0  0     0  0\n 0  0  0000  0  0  0000  0000  0   0\n\n\n 0000  0000  0   0  0000  0000\n 0 "
     "    0  0  00 00  0     0   \n 0 00  0000  0 0 0  000   0000\n 0  0  0  0  0   0  0        0\n "
     "0000  0  0  0   0  0000  0000\n\n \n 0000  00000  0   0  0   0  0     0000  00000  0000  0000  "
     " \n 0       0    00 00  0   0  0     0  0    0    0  0  0  0   \n 0000    0    0 0 0  0   0  0  "
     "   0000    0    0  0  000    \n    0    0    0   0  0   0  0     0  0    0    0  0  0  0   \n 00"
     "00  00000  0   0  00000  0000  0  0    0    0000  0   0 \n\n"
     )
Char1 = random.randint(0, 4)
Store.append(Char1)
CharList[Char1] = input("Who is your first challenger? (You will have 5 in total) \n")
while True:
   Char2 = random.randint(0, 4)
   if Char2 in Store:
       continue
   else:
       Store.append(Char2)
       CharList[Char2] = input("Who is your next challenger? \n")
       if len(Store) == 5:
           break
while True:
   a = 0
   if len(CharList) == 1:
       break
   else:
       print("\n \n              DAY", DayNum, "\n =============================== \n\n")
       Setting = random.randint(0, len(Kill) - 1)
       Chicken = (CharList[0], Kill[Setting])
       Nugget.append(Chicken)
       Kill.pop(Setting)
       CharList.pop(0)
       while True:
           if a == len(CharList):
               for i in range(len(Nugget)):
                   if len(Nugget) == 0:
                       break
                   else:
                       Position = random.randrange(0, len(Nugget))
                       print(" ".join(Nugget[Position]))
                       Nugget.pop(Position)
               Nugget = []
               DayNum += 1
               UserInput = input("Press enter to continue:\n")
               if UserInput == "":
                   break
               else:
                   continue
           else:
               Setting = random.randint(0, len(Live) - 1)
               Chicken = (CharList[a], Live[Setting])
               Nugget.append(Chicken)
               Live.pop(Setting)
               a += 1
print("\n =============================== \n\n",
     "Congratulations to", CharList[0],
     "! \nThe odds were in your favour!")
