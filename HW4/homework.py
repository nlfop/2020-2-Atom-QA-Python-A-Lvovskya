import csv
import json

try:
   textFile = open("C://Users//ulvov//Downloads//access.log", "r")
except IOError:
    print("error opening the file")
    exit(2)

with textFile:
    with open("data.json", mode="w+", encoding='utf-8') as w_file:
        lines = [line.split() for line in textFile]
        for i in range(len(lines)):
            pass
        json.dump({"number of lines": i}, w_file)
        counter_GET = 0
        for i in range(len(lines)):
            if lines[i][5][1] == 'G':
                counter_GET += 1
        json.dump({"GET": counter_GET}, w_file)
        counter_POST = 0
        for i in range(len(lines)):
            if lines[i][5][1] == 'P':
                counter_POST += 1
        json.dump({"POST": counter_POST}, w_file)
        counter_HEAD = 0
        for i in range(len(lines)):
            if lines[i][5][1] == 'H':
                counter_HEAD += 1
        json.dump({"HEAD": counter_HEAD}, w_file)

        MAX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for a in range(10):
            for i in range(len(lines)):
                leng = 0
                for k in range(len(lines[i])):
                    leng += len(lines[i][k])
                if leng > MAX[a]:
                    if a != 0:
                        if leng < MAX[a-1]:
                            MAX[a] = leng
                    else:
                        MAX[a] = leng

        for i in range(len(lines)):
            leng = 0
            for k in range(len(lines[i])):
                leng += len(lines[i][k])
            for a in range(10):
                if leng == MAX[a]:
                        json.dump({"number": MAX[a],
                                   "code": lines[i][8],
                                   "requests": lines[i][9],
                                   "url": lines[i][10]},
                                  w_file)

        MAX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for a in range(10):
            for i in range(len(lines)):
                if (int(lines[i][8]) >= 400) & (int(lines[i][8]) < 410):
                    leng = int(lines[i][9])
                    if leng > MAX[a]:
                        if a != 0:
                            if leng < MAX[a - 1]:
                                MAX[a] = leng
                        else:
                            MAX[a] = leng

        for i in range(len(lines)):
            if (int(lines[i][8]) >= 400) & (int(lines[i][8]) < 410):
                leng = int(lines[i][9])
                for a in range(10):
                    if leng == MAX[a]:
                        json.dump({"number": MAX[a],
                                   "ip": lines[i][0],
                                   "code": lines[i][8],
                                   "url": lines[i][10]},
                                  w_file)

        MAX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for a in range(10):
            for i in range(len(lines)):
                if (int(lines[i][8]) >= 500) & (int(lines[i][8]) < 600):
                    leng = 0
                    for k in range(len(lines[i])):
                        leng += len(lines[i][k])
                    if leng > MAX[a]:
                        if a != 0:
                            if leng < MAX[a-1]:
                                MAX[a] = leng
                        else:
                            MAX[a] = leng

        for i in range(len(lines)):
            leng = 0
            if (int(lines[i][8]) >= 500) & (int(lines[i][8]) < 600):
                for k in range(len(lines[i])):
                    leng += len(lines[i][k])
                for a in range(10):
                    if leng == MAX[a]:
                        json.dump({"lenght": MAX[a],
                                   "ip": lines[i][0],
                                   "code": lines[i][8],
                                   "url": lines[i][10]},
                                  w_file)


