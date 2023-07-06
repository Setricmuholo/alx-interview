#!/usr/bin/python3

"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    a method that determines if all boxes can be opened
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
