class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = dict()

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        
        print(self.graph_dict)
    
    def is_path_exist(self, start, end, path=list()):
        if start in path:
            return False

        print("Start: {}, End: {}".format(start, end))

        path = path + [start]

        if start == end:
            return True
        
        if start not in self.graph_dict:
            return False

        for dest in self.graph_dict[start]:
            is_reachable = self.is_path_exist(dest, end, path)

            if is_reachable:
                return True

        return False        
    

    def all_path(self, start, end, path=[]):
        
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

        all_paths = list()

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.all_path(node, end, path)

                for _path in new_paths:
                    all_paths.append(_path)

        return all_paths

        
if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("Paris", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    # print("Result: {}".format(route_graph.is_path_exist("Mumbai", "Toronto")))
    print("All Path : {}".format(route_graph.all_path("Mumbai", "New York")))

