#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(room):
            for key in rooms[room]:
                visited.add(room)
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        dfs(0)
        return len(rooms)==len(visited)
# @lc code=end

