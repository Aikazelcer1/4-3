from typing import Any

from datastruct.node import Node


class Stack:
    

    def __init__(self) -> None:

        self.__top = None

    def __str__(self) -> str:
        result = ''
        current_node = self.__top
        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        else:
            result += 'None'
        return result

    @property
    def top(self) -> Node:

        return self.__top

    @top.setter
    def top(self, top: Node) -> None:

        self.__top = top

    def push(self, value: Any) -> None:

        new_node = Node(data=value)
        new_node.next_node = self.top
        self.__top = new_node

    def pop(self) -> Any:

        if self.__top is None:
            return
        value = self.__top.data
        self.__top = self.__top.next_node
        return value
