"""
Build Order.
"""

from enum import Enum, auto
from typing import List, Deque, Optional
from collections import deque


# Edge removal.
# class Project:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
#         self.map = {}
#         self.dependencies = 0
#
#     def increment_dependencies(self):
#         self.dependencies += 1
#
#     def decrement_dependencies(self):
#         self.dependencies -= 1
#
#     def add_neighbor(self, node):
#         if node.name not in self.map:
#             self.children.append(node)
#             self.map[node.name] = node
#             node.increment_dependencies()
#
#
# class Graph:
#     def __init__(self):
#         self.nodes = []
#         self.map = {}
#
#     def get_or_create_node(self, name: str) -> Project:
#         if name not in self.map:
#             node = Project(name)
#             self.nodes.append(node)
#             self.map[name] = node
#         return self.map.get(name)
#
#     def add_edge(self, start_name, end_name):
#         start = self.get_or_create_node(start_name)
#         end = self.get_or_create_node(end_name)
#         start.add_neighbor(end)
#
#
# def find_build_order(projects: List[str], dependencies: List[List[str]]) -> List[Project]:
#     graph = build_graph(projects, dependencies)
#     return order_projects(graph.nodes)
#
#
# def build_graph(projects: List[str], dependencies: List[List[str]]) -> Graph:
#     graph = Graph()
#     for project in projects:
#         graph.get_or_create_node(project)
#
#     for dependency in dependencies:
#         first = dependency[0]
#         second = dependency[1]
#         graph.add_edge(first, second)
#
#     return graph
#
#
# def order_projects(projects: List[Project]) -> Optional[List[Project]]:
#     order = []
#
#     # Add roots to the build order first.
#     end_of_list = add_non_dependent(order, projects, 0)
#
#     to_be_processed = 0
#     while to_be_processed < len(order):
#         current = order[to_be_processed]
#
#         # We have a circular dependency since there are no remaining projects with zero dependencies.
#         if not current:
#             return None
#
#         # Remove myself as a dependency.
#         children = current.children
#         for child in children:
#             child.decrement_dependencies()
#
#         # Add children that have no dependencies on them.
#         end_of_list = add_non_dependent(order, projects, end_of_list)
#
#         to_be_processed += 1
#
#     return order
#
#
# def add_non_dependent(order: List[Project], projects: List[Project], offset: int) -> int:
#     for project in projects:
#         if not project.dependencies:
#             order[offset] = project
#             offset += 1
#
#     return offset


# DFS.
class AutoName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self


class State(AutoName):
    COMPLETE = auto()
    PARTIAL = auto()
    BLANK = auto()


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.state = State.BLANK

    def add_neighbor(self, node):
        if node.name not in self.map:
            self.children.append(node)
            self.map[node.name] = node


class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def get_or_create_node(self, name: str) -> Project:
        if name not in self.map:
            node = Project(name)
            self.nodes.append(node)
            self.map[name] = node
        return self.map.get(name)

    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)


def find_build_order(projects: List[str], dependencies: List[List[str]]) -> List[Project]:
    graph = build_graph(projects, dependencies)
    return order_projects(graph.nodes)


def build_graph(projects: List[str], dependencies: List[List[str]]) -> Graph:
    graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)

    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph


def order_projects(projects: List[Project]) -> Optional[Deque]:
    stack = deque()

    for project in projects:
        if project.state == State.BLANK:
            if not do_dfs(project, stack):
                return None

    return stack


def do_dfs(project, stack) -> bool:
    if project.state == State.PARTIAL:
        return False

    if project.state == State.BLANK:
        project.state = State.PARTIAL
        children = project.children
        for child in children:
            if not do_dfs(child, stack):
                return False

    project.state = State.COMPLETE
    stack.append(project)
    return True
