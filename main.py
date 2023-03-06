import Neural_network
import trainer
from random import randint as randint


network = Neural_network.start(7)
dataset = []

for z in range(100):
    x = randint(0,10000)
    dataset.append((x,2*x))
trainer.trainer(network,dataset)

network.reset_newtork()
network.Nodes[0].calculate_signal(0,2)
network.fire_network()
print(network.network_output())