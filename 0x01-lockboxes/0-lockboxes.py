#!/usr/bin/python3
"""
unlocking locked box using keys from different box
"""


def canUnlockAll(boxes):
    if type(boxes) != list:
        return False

    opened_boxes = [0]
    for i in opened_boxes:
        for key in boxes[i]:
            if not key in opened_boxes and key < len(boxes):
                opened_boxes.append(key)
                print(opened_boxes)

    return len(boxes) == len(opened_boxes)
