from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        result = 0
        if(len(tasks) == 1):
            return -1
        tasks.sort()
        last = tasks[0]
        count = 0
        for task in tasks:
            if(task == last):
                count += 1
            else:
                if(count == 1):
                    return -1
                result += (count // 3) + (0 if (count % 3) == 0 else 1)
                count = 1
                last = task
        result += (count % 3) + (0 if (count // 3) == 0 else 1)
        return result

s = Solution()

print(s.minimumRounds([2,2,3,3,2,4,4,4,4,4]))