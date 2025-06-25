network = {
    "HR_PC": ["FIN_PC", "ADMIN_PC"],  # insecure
    "FIN_PC": [],
    "ADMIN_PC": ["DATABASE_SERVER"],
    "DATABASE_SERVER": []
}



def traverse_network(start, target, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True
    visited.add(start)


    for neighbor in network.get(start, []):
        if neighbor not in visited and traverse_network(neighbor, target, visited):
            return True
    return False


print("Can attacker reach DATABASE_SERVER from HR_PC?", traverse_network("HR_PC", "DATABASE_SERVER"))