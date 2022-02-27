import speedtest
s = speedtest.Speedtest()
print("Running SpeedTest.....")
print("Download: ",s.download()/pow(10,6)," Mbps")
print("Upload: ",s.upload()/pow(10,6)," Mbps")

best_server = s.get_best_server()
print('\nBest server:')
for key,value in best_server.items():
    print(key,' : ',value)

closest_server = s.get_closest_servers()
print('\nClosest server:')
for key,value in closest_server[1].items():
    print(key,' : ',value)
