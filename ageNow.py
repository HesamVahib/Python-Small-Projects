import datetime
x = datetime.datetime.today()
x = ((str(x).split())[0]).split('-')

inp = input().split('/')
if int(inp[1]) > 12 or int(inp[2]) > 31:
    print('WRONG')

else:
    diff = int(x[0]) - int(inp[0]) - ((int(x[1]), int(x[2])) <= (int(inp[1]), int(inp[2])))
    print(diff)