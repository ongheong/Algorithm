class Solution:
    def dfs(self, graph, start, path):
        path = path + [start] #현재 탐색하는 경로 배열에 요소(노드 혹은 경로) 추가
        if start == len(graph)-1: #종료 노드에 도달하면 현재 경로 반환 
            return [path] #ex) [[0, 1, 3]]
        paths = []
        for node in graph[start]:
            if node not in path: #경로 중복하지 않도록 체크함
                new_path = self.dfs(graph, node, path) #새로운 경로 탐색
                for p in new_path:
                    paths.append(p) #탐색 후 답안 배열에 추가
        return paths #모든 경로 탐색하면 최종 답안 리턴

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(graph, 0, [])