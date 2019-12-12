from lib.model import Model
import lib.train as trainer
from torch.autograd import Variable
import torch

# Import your model
model = Model()

# Training data
data = trainer.parseTrainingData('./dataSet.json')

# Train your model
trainer.trainCPU(model=model, data=data, epochs=15000, targetLoss=0.001, learningRate=0.2)

# Save your model
trainer.saveModel(model, 'xor.net')