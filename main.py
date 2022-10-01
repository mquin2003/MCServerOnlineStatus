from mcstatus import JavaServer as ms
import time
ms.lookup

start_time = time.time()  # Gets start time to calculate total runtime later

serverIPs = open('serverips.txt',"r")
currentServers = open('onlineservers.txt','w')

count = 0
for server in serverIPs:
    count += 1
    try:
        servStat = ms.lookup(server, 0.5).status()
        currentServers.write(f"[{count}] - IP: {server}, Online, Players: {servStat.players.online}\n")
        print(f"[{count}] - IP: {server}, Online, Players: {servStat.players.online}\n")
    except:
        currentServers.write(f"[{count}] - IP: {server}, Offline\n")
        print(f"[{count}] - IP: {server}, Offline\n")

serverIPs.close()
currentServers.close()

end_time = (time.time() - start_time)
print("--- %s seconds ---" % (time.time() - start_time))
