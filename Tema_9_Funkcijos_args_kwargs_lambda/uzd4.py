# Ar galite surasti bigramas?

from typing import List


def can_find(bigrams: List[str], words: List[str]) -> bool:
    for bigram in bigrams:
        found = False

        for word in words:
            if bigram in word:
                found = True
                break
        if not found:
            return False
    
    return True




print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))