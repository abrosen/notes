CAPACITY = 10

array = [0]*(3*CAPACITY)
top = [-1,-1,-1]


def push(stack,value):
    if top[stack] >= CAPACITY -1:
        raise Exception
    else:
        top[stack]+=1
        array[stack*100 +top[stack]] = value

def pop(stack):
    if top[stack] < 0:
        raise Exception
    else:
        val =  array[stack*100 +top[stack]]
        array[stack*100 +top[stack]] = 0
        top[stack]-=1
        return val


def peek(stack):
    if top[stack] < 0:
        raise Exception
    else:
        return array[stack*100 +top[stack]]