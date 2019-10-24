#__author: xlu.com
#date : 2018/12/28

if __name__ == "__main__":
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    c = zip(a,b)
    # for i in c:
    #     print(1)

    d = zip(c)
    for j in zip(*c):
        print(j)

    f = []
    for x,y in zip(a,b):
        f.append(x+y)
    print(f)
