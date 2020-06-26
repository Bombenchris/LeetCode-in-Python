
# rains = [1,2,0,0,1,2]
# lake:key,  column: days

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(list)
        ret = [-1] * len(rains) # output
        to_empty = []           # index, min-heap to keep track of urgent day,
        full = set([])          # hashset, unique lake key
        for day, lake in enumerate(rains):
            dic[lake].append(day)
            # dic = 1:[0,4] 2:[1,5] 0:[2,3]

        for i in range(len(rains)):
            lake = rains[i]
            if lake:  # non zero lake
                if lake in full:
                    return []
                full.add(lake)
                dic[lake].pop(0)
                if dic[lake]:
                    heapq.heappush(to_empty, dic[lake][0])  # take the second days
            else:   # zero: sunny days
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]  # empty the most urgent lake
                    full.remove(ret[i])
                else:
                    ret[i] = 1
        return ret