from typing import Any


class Node:


    def __init__(self, data: Any, next_node=None) -> None:

        self.__data = data
        self.__next_node = next_node

    def __str__(self) -> str:
        return f'Node(data={self.__data}, next_node={self.__next_node})'

    def __repr__(self) -> str:
        return repr(f'Node(data={self.__data}, next_node={self.__next_node})')

    @property
    def data(self) -> Any:

        return self.__data

    @data.setter
    def data(self, data: Any) -> None:

        self.__data = data

    @property
    def next_node(self) -> 'Node':

        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: 'Node') -> None:

        self.__next_node = next_node