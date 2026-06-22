#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1.0:
                    return weight * result

            return -1.0

        ans = []

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set()))

        return ans
# @lc code=end

