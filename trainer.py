import copy
from random import randint as randint

def trainer(network,dataset):
    dataset_num = 0
    for (x,y) in dataset:
        dataset_num += 1
        z = 0
        while z < 100:
            #temp_network = copy.deepcopy(network)
            network.Nodes[0].calculate_signal(0,x)
            network.fire_network()
            print(network.network_output(),"dataset:({0},{1})".format(x,y))
            divergence = network.network_output() - y
            if network.network_output() == y :
                break
            if network.network_output() > y :
                network.reset_newtork()
                network.weights = [x - randint(0,10)/(z+dataset_num) for x in network.weights]
                for x in range(1,len(network.Nodes)):
                    network.Nodes[x].weights = [x - randint(0,10)/(z+dataset_num) for x in network.Nodes[x].weights]
                    network.Nodes[x].threshold += randint(0,1000)/(z+dataset_num)
            if network.network_output() < y :
                network.reset_newtork()
                network.weights = [x + randint(0,10)/(z+dataset_num) for x in network.weights]
                for x in range(1,len(network.Nodes)):
                    network.Nodes[x].weights = [x + randint(0,10)/(z+dataset_num) for x in network.Nodes[x].weights]
                    network.Nodes[x].threshold -= randint(0,1000)/(z+dataset_num)
            new_divergence = network.network_output() - y
            if abs(new_divergence) > abs(divergence):
                network = temp_network
            z += 1
                
                
