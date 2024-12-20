
from dataclasses import dataclass


@dataclass
class FilePart:
    id: int

class Disc:
    def __init__(self, line: str):
        self._disc = []
        self._parse(line.strip())
        self._start_index = 0
    
    def _parse(self, line: str):
        fileid = 0
        for i, c in enumerate(line):
            if i % 2 == 0:
                # even -> a file
                for _ in range(int(c)):
                    self._disc.append(FilePart(id = fileid))
                fileid = fileid + 1
            else:
                for _ in range(int(c)):
                    self._disc.append(None)

    def _find_last_element_non_empty(self, min_index):
        x = len(self._disc) - 1
        while x > min_index:
            element = self._disc[x]
            if element is not None:
                self._disc[x] = None
                return element
            x -= 1
        return None

    def _reduce_disk(self):
        first_index_empty = self._disc.index(None, self._start_index)
        self._start_index = first_index_empty
        
        last_element_non_empty = self._find_last_element_non_empty(self._start_index)
        if last_element_non_empty is not None:
            self._disc[first_index_empty] = last_element_non_empty
            return True
        return False
    
    def reduce_disc(self):
        while (disc._reduce_disk()):
            pass
        self._disc = self._disc[:self._disc.index(None)]

    def calculate_checksum(self):
        s = 0
        for i, e in enumerate(self._disc):
            s += i * e.id
        return s

            
disc = Disc(open('data/09.txt').readline())
disc.reduce_disc()
print(disc.calculate_checksum())