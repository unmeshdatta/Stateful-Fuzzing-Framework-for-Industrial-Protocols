"""Simple state machine representation using networkx."""
import networkx as nx
from typing import Hashable, Iterable


class StateMachine:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.start_state = None

    def add_state(self, state: Hashable, start: bool = False):
        self.graph.add_node(state)
        if start or self.start_state is None:
            self.start_state = state

    def add_transition(self, src: Hashable, dst: Hashable, action: str):
        self.graph.add_edge(src, dst, action=action)

    def next_states(self, state: Hashable) -> Iterable[Hashable]:
        return self.graph.successors(state)
