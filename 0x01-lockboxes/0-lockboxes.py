#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes."""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened."""
    boxesUnlocked = [0]
    for x, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in boxesUnlocked and key != x:
                boxesUnlocked.append(key)
    if len(boxesUnlocked) == len(boxes):
        return True
    else:
        return False

    return len(boxes)
