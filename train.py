import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import json;

EPOCHS_TO_TRAIN = 20000

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 6, True)
        self.fc2 = nn.Linear(6, 6, True)
        self.fc3 = nn.Linear(6, 3, True)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = self.fc2(x)
        x = self.fc3(x)
        return x

net = Net()

raw = open("./dataset.json").read()
data = json.loads(raw)

inputs = []
targets = []

for set in data:
    inputs.insert(0, torch.Tensor([float(set['pos']['x']) / 200, float(set['pos']['y']) / 200]))
    targets.insert(0, torch.Tensor([float(set['servo']['base']) / 700, float(set['servo']['shoulder']) / 700, float(set['servo']['elbow']) / 700]))
    pass

criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.4)

print("Training loop:")
for idx in range(0, EPOCHS_TO_TRAIN):
    for input, target in zip(inputs, targets):
        optimizer.zero_grad()   # zero the gradient buffers
        output = net(input)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()    # Does the update
    if idx % 50 == 0:
        print("Epoch {: >8} Loss: {}".format(idx, loss.data.numpy()))
    if loss.data.numpy() < 0.0001:
        break


torch.save(net, 'trained.net')