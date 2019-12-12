from lib.model import Model
import lib.train as trainer

model = Model().cpu()

model = trainer.loadModel('xor.net')
model.eval()
model.cpu()

print("model loaded")

trainer.run(model, [0, 0]) # 0 0 0 0
trainer.run(model, [0.9, -0.5]) # 1 0 0 1
trainer.run(model, [0, 0], wholeNum=True) # 0 0 0 0
trainer.run(model, [0.9, -0.5], wholeNum=True) # 1 0 0 1

trainer.run(model, [0, 1]) # 0 0 1 0
trainer.run(model, [0.2, 0.8]) # 1 0 1 0 
trainer.run(model, [0, 1], wholeNum=True) # 0 0 1 0
trainer.run(model, [0.2, 0.8], wholeNum=True) # 1 0 1 0 