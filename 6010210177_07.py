if __name__ == '__main__' :
    c = 10
    for i in range (1,22,2):
        for j in range(1):
            print ("  ")*c + ("# ")*i + ("  ")*c
            c = c - 1
