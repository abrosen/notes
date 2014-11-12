def getNetwork(filename):
    """Given a network matrix of the specified below format, store it"""
    lines =  open(filename)
    nodes = []
    edges = {}
    node = 0 
    for line in lines:
        nodes.append(node)
        line =line.strip()
        line = line.split(',')
        #print line
        for i in range(node,len(line)):
            if line[i] != '-':
                edges[(node,i)] = int(line[i])
        node +=1
    return nodes, edges


nodes, edges = getNetwork("p107_network.txt")
