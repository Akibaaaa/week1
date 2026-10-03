# quetion number 5

def balance_workload(servers):
    overloaded_servers =[]
    for server_id, cpu, memory in servers:
        if cpu>85 or memory > 90:
            overloaded_servers.append(server_id)
    return overloaded_servers
servers = []
number_of_servers = int(input("enter the numbers of servers:"))
for i in range (number_of_servers):
    server_id = input("enter the server id: ")
    cpu = float(input("Enter the cpu usage: "))
    memory = float(input("enter the memory usage: "))
    server = (server_id, cpu, memory)
    servers.append(server)
result = balance_workload(servers)
print(result)
            
