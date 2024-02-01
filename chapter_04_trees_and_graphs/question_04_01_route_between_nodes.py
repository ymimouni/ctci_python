"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
Hints: #127
"""

from enum import Enum, auto
from typing import final
from collections import deque


class AutoName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self


class State(AutoName):
    Unvisited = auto()
    Visited = auto()
    Visiting = auto()


class Node:
    def __init__(self, vertex: str, adjacents_length: int) -> None:
        self.vertex = vertex
        self.adjacents = [None] * adjacents_length
        self.adjacents_count = 0
        self.state = None

    def add_adjacent(self, x: 'Node'):
        if self.adjacents_count < len(self.adjacents):
            self.adjacents[self.adjacents_count] = x
            self.adjacents_count += 1
        else:
            print("No more adjacents can be added.")

    def get_adjacents(self):
        return self.adjacents

    def get_vertex(self):
        return self.vertex


class Graph:
    MAX_VERTICES: final = 6

    def __init__(self):
        self.vertices = [None] * Graph.MAX_VERTICES
        self.count = 0

    def add_node(self, x: Node):
        if self.count < len(self.vertices):
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("Graph full.")

    def get_nodes(self):
        return self.vertices


def search(g: Graph, start: Node, end: Node) -> bool:
    q = deque()
    for n in g.get_nodes():
        n.state = State.Unvisited
    start.state = State.Visiting
    q.appendleft(start)
    while q:
        u = q.pop()
        if u:
            for v in u.get_adjacents():
                if v.state == State.Unvisited:
                    if v is end:
                        return True
                    else:
                        v.state = State.Visiting
                        q.appendleft(v)
            u.state = State.Visited
    return False


def create_new_graph() -> Graph:
    a_graph = Graph()
    temp = [None] * 6

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[2])
    temp[0].add_adjacent(temp[3])
    temp[3].add_adjacent(temp[4])
    temp[4].add_adjacent(temp[5])

    for i in range(6):
        a_graph.add_node(temp[i])
    return a_graph


if __name__ == "__main__":
    g = create_new_graph()
    print(search(g, g.get_nodes()[0], g.get_nodes()[5]))
    print(search(g, g.get_nodes()[3], g.get_nodes()[5]))
    print(search(g, g.get_nodes()[1], g.get_nodes()[5]))
