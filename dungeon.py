from info import PlayerInfo as info
from Game import Game as game

print("DUNGEON GAME! Make your choices, well")
class Flow:

    def main(self):
        """
        Main Method will drive all operations.
        :return:
        Fun ;)
        """
        _age= info.getInfo(self)
        _flag = game.check_age(_age)
        if _flag == False:exit()
        game.wantsToPlay(0)

"""
Here object created and and called main method
"""
ObjFlow = Flow()
ObjFlow.main()
