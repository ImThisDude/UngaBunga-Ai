from math import log as log
from random import randint as randint

class network:
    def __init__(self):
        self.Nodes = []
        self._n = 0
        self.weights = []
    def fire_signal(self,node,signal_stregnth):
        index = self.Nodes.index(node)
        hierarchy = log(index,2) if index > 1 else 0
        hierarchy = 1 if index == 1 else hierarchy
        hierarchy = hierarchy if int(hierarchy) == hierarchy else int(hierarchy) + 1
        signal_index = index - 2**(hierarchy) + 1
        hierarchy = int(hierarchy)
        if hierarchy >= self._n :
            return
        signal_index = int(signal_index)
        for x in range(2**(hierarchy+1)-1,2**(hierarchy +2)-1):
            self.Nodes[x].calculate_signal(signal_index = signal_index,signal_stregnth =signal_stregnth)
    def create_network(self,n):
        self._n = n
        self.weights = [randint(0,10) for x in range(2**n)]
        node = Node([1],0,self)
        self.Nodes.append(node)
        print(n)
        for x in range(1,n+1):
            for y in range(2**x):
                weights = [randint(0,10) for x in range(2**(x-1))]
                threshold = randint(0,1000)
                node = Node(weights = weights,threshold = threshold,network = self)
                self.Nodes.append(node)
    def network_output(self):
        total = 0
        for x in range(2**(self._n),2**(self._n+1)):
            total += self.Nodes[x-1].output()*self.weights[x-2**(self._n)]*self.Nodes[x-1].sum
        return total
    def reset_newtork(self):
        for x in self.Nodes:
            x.reset_sum()
    def fire_network(self):
        for x in self.Nodes:
            x.fire()
    def print_network(self):
        for x in self.Nodes:
            print(x.weights,x.threshold,x.sum)





class Node(network):
    def __init__(self,weights,threshold,network):
        self._weights = weights
        self._threshold = threshold
        self._sum = 0
        self.network = network
    def fire(self):
        if self._sum >= self._threshold:
            network.fire_signal(self.network,node = self,signal_stregnth =self._sum)
    def calculate_signal(self,signal_index,signal_stregnth):
        self._sum += self._weights[signal_index]*signal_stregnth
    def output(self):
        if self._sum >= self._threshold:
            return self._sum
        return 0 
    def reset_sum(self):
        self._sum = 0
    @property
    def sum(self):
        return self._sum
    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self,weights):
        _weights = weights
    
    @property
    def threshold(self):
        return self._threshold
    @threshold.setter
    def threshold(self,threshold):
        _threshold = threshold

    
def start(n):
    test_network = network()
    test_network.create_network(n)
    return test_network
    