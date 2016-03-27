# Kevin-Bacon-game
Simple game that uses Djkstra's algorithim to find the shortest path.
How to use the program:
  1.) Enter a txt file that holds movies and the actors in those movies (See "films-small.txt" file for the format of the txt file)
  2.) Enter an actor name that is in the txt file that you have provided
  3.) The progrma will then output the shortest link from that actor to Kevin Bacon.

Implementation of the program:
  
This program uses an unweighted shortest path test to determine a link between a specified actor and kevin bacon. The program utilizes
the hash tables (or dictionaries) that are built in python to create a graph structure of all the movies and actors in the txt file that is
provided by the user.Then, another dictionary is created and every item in that dictionary has two keys "parent and "distance"; this
is needed to calculate the distance between all the actors from kevin bacon which means that we start with kevin bacon as the "parent" and
go down the list of actors and calculate their distances away from Then, the program asks the user to input an actor name to find the closest link between that actor and Kevin Bacon.
Afterwards, the program uses Djkastra's algorithim to find the closest link to from the actor to Kevin Bacon (See the file "bacon.py" to
see how that was coded). Then, after finding the closest link, output it starting with the actor and ending it with kevin bacon, for ex:
    big mamba was in The killers with james woods
    james woods was ain Assaulted with brad pitt
    brad pitt was in Fake movies with Kevin Bacon
