class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # create graph with stop-route relationship
        # key: stop, value: set of routes that pass through that stop
        graph = defaultdict(set)  
        for route_id, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route_id)  
        
		# perform breadth-first search starting at the source stop
		# queue maintains the stop we're at and the number of route
        # changes we've made so far
        queue = deque([(source, 0)])
		# keep track of seen stops and routes to not duplicate effort
        seen_stops = set([source])
        seen_routes = set()
        
        while queue:
			# check whether we've now reached the destination 
            # and if so, return number of route changes
            stop, num_changes = queue.popleft()
            if stop == target:
                return num_changes
            # for each new route that passes through the current stop
            for route_id in graph[stop]:
                if route_id not in seen_routes:
                    seen_routes.add(route_id)
                    # enqueue all previously unseen stops that 
                    # are part of the route 
                    for stop in routes[route_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop, num_changes + 1))
        
        return -1
                
