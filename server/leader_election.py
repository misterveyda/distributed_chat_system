def elect_leader(nodes):
    return min(nodes, key=lambda n: n["port"])
