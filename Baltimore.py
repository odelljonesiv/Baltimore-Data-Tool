
import json
import sys
import urllib3
import pandas as pd
http = urllib3.PoolManager()
listNeighborhoods = ["Abell", "Barclay", "Charles Village", "East Baltimore Midway", "Greenmount West", "Harwood", "Old Goucher", "Remington",
"Waverly"]
print(".....connecting to: https://data.baltimorecity.gov/......\n\n")
for element in listNeighborhoods:
    print("Checking Neighborhood: ", element, ".....")
print("\n\n")
r = http.request('GET', 'https://data.baltimorecity.gov/resource/xviu-ezkt.json')
# print(r.status)
data = json.loads(r.data.decode('utf-8'))
# print(data)
highCounter =0;

def main():
    print("HIGH PRIORITY CALLS:\n\n")
    for item in data:
        if item["neighborhood"] in listNeighborhoods:
            if item["priority"] == "High":
                print("Neighborhood: ", item["neighborhood"],
                      "| Date and Time: ", item["calldatetime"],
                      "| Record ID: ", item["recordid"])
                print("INCIDENT: ", item["description"],"\n")


    print("\n\nMEDIUM PRIORITY CALLS:\n\n")
    for item in data:
        if item["neighborhood"] in listNeighborhoods:
            if item["priority"] == "Medium":
                print("Neighborhood: ", item["neighborhood"],
                      "| Date and Time: ", item["calldatetime"],
                      "| Record ID: ", item["recordid"])
                print("INCIDENT: ", item["description"],"\n")

    print("\n\nNON - EMERGENCY PRIORITY CALLS:\n\n")

    for item in data:
        if item["neighborhood"] in listNeighborhoods:
            if item["priority"] == "Non-Emergency" :
                print("Neighborhood: ", item["neighborhood"],
                      "| Date and Time: ", item["calldatetime"],
                      "| Record ID: ", item["recordid"])
                print("INCIDENT: ", item["description"],"\n\n")
                exit = input("Press any key followed by enter to exit.")
                sys.exit("exiting...")
if __name__ == '__main__':
    main()