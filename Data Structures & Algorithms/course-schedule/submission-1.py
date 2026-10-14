class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        We can visualise prereqs as oriented vertices of a graph.
        e.g. [[0,1], [1,0]] means 0 -> 1 -> 0
        which means:
        1. we need to detect if there is a cycle. If there is a cycle, it means one course is required
        for another which is required for it.
        2. if there is no cycle, we must check if we can travel through numCourses nodes at least.
        """

        # setting up an adjacency list:
        # prerequisites = [[0,1], [0,2],[1,2]] graph = {0: [1, 2], 1: [2]}
        graph = {}
        for vertex in prerequisites:
            if vertex[0] not in graph:
                graph[vertex[0]] = graph.get(vertex[0], [])
                graph[vertex[0]].append(vertex[1])
            else:
                graph[vertex[0]].append(vertex[1])
        
        path = set()
        visited = set()

        def dfs(node): # is there a cycle ?
            if node in path: return True       
            if node in visited: return False 
            path.add(node)
            for nei in graph.get(node, []):
                if dfs(nei): return True
            
            path.remove(node)
            visited.add(node)
            return False
        
        for course in range(numCourses):
            if dfs(course): return False
        return True

                

