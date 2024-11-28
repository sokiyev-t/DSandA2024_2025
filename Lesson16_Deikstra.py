graph = {}
graph["начало"] = {}
graph["начало"]["a"] = 6
graph["начало"]["b"] = 2

graph["a"] = {}
graph["a"]["конец"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["конец"] = 5

graph["конец"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["конец"] = infinity

parents = {}
parents["a"] = "начало"
parents["b"] = "начало"
parents["конец"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:  # Если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать всех соседей (neighbors) текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost  # обновить стоимость для этого узла
            parents[n] = node  # Этот узел становится новым родителем для соседа
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)

# print(node)
print(parents)
# print(costs)

start=parents["конец"]
print("конец")
while(parents.get(start)):
    print(start)
    start=parents[start]
print(start)

print("Минимальный маршрут: ", costs["конец"])
