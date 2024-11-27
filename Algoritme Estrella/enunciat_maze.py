#!/bin/bash

import pyamaze as maze
from queue import PriorityQueue
import time

ROWS = 20
COLS = 20


def distance(cell1, cell2):
    distance = abs(cell1[0]-cell2[0])+abs(cell1[1]-cell2[1])
    return distance



def aStar(m):

    end = (ROWS,COLS)
    start = (1,1)
    paradas={}

    distancia_recorrida={dir:float("inf") for dir in m.grid}
    distancia_recorrida[start]=0

    pq = PriorityQueue()
    pq.put((distance(start,end),start))
    
    while not pq.empty():
        current = pq.get()[1]
        print(f'POSI ACTUAL:{current}')
        if current == end:
            break

        for dir in "NSEW":
            if m.maze_map[current][dir] == 1:

                if dir == "E":
                    new_position = (current[0] , current[1]+1)

                if dir == "S":
                    new_position = (current[0]+1, current[1])

                if dir == "N":
                    new_position = (current[0]-1, current[1])

                if dir == "W":
                    new_position = (current[0], current[1]-1)

                # print(f'NUEVA POSICION: {new_position}')
                aux_recorrido = distancia_recorrida[current]+1
                # print(f'AUXILIAR: {aux_recorrido}')
                # print(f'RECORRIDA: {distancia_recorrida}')

                if distancia_recorrida[new_position] > aux_recorrido:
                    distancia_recorrida[new_position] = aux_recorrido
                    paradas[new_position] = current
                    pq.put((distancia_recorrida[new_position]+distance(new_position, end),new_position))
                



    return paradas


m=maze.maze(ROWS,COLS)
m.CreateMaze()
#pre_Astar = time.time()
path = aStar(m)
post_Astar = time.time()
#print(post_Astar - pre_Astar)
a=maze.agent(m,footprints=True)
m.tracePath({a:path},delay=300)
m.run()
#print(m.maze_map)


#total = distance(m.maze_map[(1,1)],m.maze_map[(ROWS,COLS)])

#m.run()

###################################
