class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(loc, nodes, path, visited):
            if loc in visited:
                return path, True

            if loc not in nodes:
                return path, False

            visited[loc] = True

            end_paths = sorted(nodes[loc])

            if len(end_paths) == 0:
                return path

            non_return_to_origin_path = None

            for end in end_paths:
                tmppath = []
                tmppath.append(end)
                tmppath, return_to_origin = dfs(end, nodes, tmppath, visited)

                if return_to_origin is False:
                    non_return_to_origin_path = tmppath
                else:
                    path += tmppath

            if non_return_to_origin_path is not None:
                path += non_return_to_origin_path

            return path, True


        nodes = {}
        for ticket in tickets:
            if ticket[0] not in nodes:
                nodes[ticket[0]] = [ticket[1]]
            else:
                nodes[ticket[0]].append(ticket[1])

        start = "JFK"

        path, v = dfs(start, nodes, [start], {})
        return path

soln = Solution()

# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

print(soln.findItinerary(tickets))