import sims4.commands


# The first line loads the sims4.commands module from EA's game scripts. This step is required to use the
# sims4.commands.Command in the next line. The next line defines the cheat code command. The first item passed to the
# cheat code is the name of the cheat code that will be typed into the in-game cheat console. The second part
# specifies that this cheat code will be used in Live mode in the game. After the sims4.commands.Command decorator (a
# python term), is a function that will run when the cheat code is called from the game. The first line of the cheat
# code function acquires a reference to the cheat UI's output window. The last line simply writes some text to the
# output window. In the game, you should see whatever you write in the script instead of "This is my first script mod".

@sims4.commands.Command('myfirstscript', command_type=sims4.commands.CommandType.Live)
def myfirstscript(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Hello World!")
