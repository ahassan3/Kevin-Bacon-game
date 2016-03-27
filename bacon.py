
# Aimen Hassan
# 11/3/2015
# CS-361
#instructor: David Reed

import sys

def main(argv):
    # command line argument
    if len(argv) > 1:
        file_object = argv[1]
    else:
        file_object = input("Enter Filename: ")
    # read file
    filename = open(file_object, 'r')
    # intialize dictionary for graph structure
    graph = {}
    # create an empty list to hold actors
    actors = []
    # to increment with
    incr = 0
    # iterate over the file
    for i in filename:
        # set the movie to first lie
        if incr == 0:
            movie = i
        # increment
        incr += 1
        # to append items in graph if blank space was found
        if i == '\n':
            # iterate over the actors
            for j in actors:
                # if the actor isn't in the dictionary
                if j not in graph:
                    graph[j] = {}
                # iterate over all the actors again
                for l in actors:
                    # append the actors as edges to every adjacent actor
                    if l != j:
                        graph[j][l] = movie[:-1]
            # reintialize the incr
            incr = 0
            # reintialize the actor list
            actors = []
        # to append the actors in the file to the list
        if (i != movie) and (i != '\n'):
            # if the the last letter is a \n
            if i[-1] == '\n':
                actors.append(i[:-1])
            # otherwise just add it in normally
            else:
                actors.append(i)
    # loop to append all remaining actors in the graph
    for j in actors:
        if j not in graph:
            graph[j] = {}
        for l in actors:
            if l != j:
                graph[j][l] = movie[:-1]
    # start the queue list with kevin bacon
    queue = ['Kevin Bacon']
    # create new dictionary
    small_dic = {}
    # append actors from graph into the new dictionary
    for i in graph:
        # create a nested dictionary
        small_dic[i] = {}
        # create a key named Parent and set it to none
        small_dic[i]['Parent'] = None
        # create key named distance and set it to zero
        small_dic[i]['Distance'] = 0
    # while queue not empty
    while len(queue) > 0:
        # take out the item from queue
        v = queue[0]
        # iterate over adjacent items for every vertex
        for i in graph[v]:
            # if item has no parent
            if small_dic[i]['Parent'] == None:
                # set v to the parent of item
                small_dic[i]['Parent'] = v
                # increase the distance of by 1 and add that to the item
                small_dic[i]['Distance'] = small_dic[v]['Distance'] + 1
                # append the item in queue
                queue.append(i)
        # remove item from queue
        queue.remove(v)
    # ask the name of actor
    source = input('enter actor: ')
    # while the user is inputing actor names
    while source != '':
        # if the actor name is Kevin Bacon
        if source == 'Kevin Bacon':
            # print this
            print('You are already there silly')
        # while the source isn't Kevin Bacon
        while source != 'Kevin Bacon':
            # parent is equal to the source' parent
            parent = small_dic[source]['Parent']
            # print the statement given the actor adjacent to kevin Bacon
            print(source, ' was in ' ,graph[source][parent],' with ',parent)
            # set the source to parent
            source = parent
        # new input is to be set
        source = input('enter actor: ')
    # close file
    filename.close()
if __name__ == '__main__':
    main(sys.argv)