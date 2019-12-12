import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # Layers
        self.fc1 = nn.Linear(2, 8, True)
        self.fc2 = nn.Linear(8, 6, True)
        self.fc3 = nn.Linear(6, 4, True)

    def forward(self, x):
        # Forward propagation
        x = torch.sigmoid(self.fc1(x)) # torch.sigmoid (stable), torch.relu (fast, but wonky), F.leaky_relu (fast, but less(?) wonky)
        x = self.fc2(x)
        x = self.fc3(x)
        return x