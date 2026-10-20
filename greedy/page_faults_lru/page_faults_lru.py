from collections import OrderedDict

class Solution:
    def pageFaults(self, pages, C):
        memory = OrderedDict()
        faults = 0

        for page in pages:
            if page in memory:
                memory.move_to_end(page)
            else:
                faults += 1

                if len(memory) == C:
                    memory.popitem(last=False)

                memory[page] = True

        return faults
