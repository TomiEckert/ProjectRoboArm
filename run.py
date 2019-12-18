import torch
import torch.nn as nn
import torch.nn.functional as F

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
net = torch.load('trained.net')

output = net(torch.Tensor([127 / 200, 78 / 200]))

print(output)
print('========')
print("base: {}".format(output.data.numpy()[0] * 700))
print("shoulder: {}".format(output.data.numpy()[1] * 700))
print("elbow: {}".format(output.data.numpy()[2] * 700))