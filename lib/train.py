import torch
import torch.nn as nn
import torch.optim as optim
import json
import warnings

def trainCPU(*, model, data, epochs=5000, learningRate=0.1, stopOnStuck=False, targetLoss=0):
    inputs = data[0]
    targets = data[1]

    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learningRate)

    avg_loss = 1
    sum_loss = 0
    counter = 0

    print("Max epoch: {: >14}".format(epochs))
    print("Learning rate: {: >10}".format(learningRate))
    if targetLoss != 0:
        print("Target loss: {: >12}".format(targetLoss))
    print()

    print("\033[s")

    for idx in range(0, epochs):
        if counter != 0:
            avg_loss = sum_loss / counter
            sum_loss = 0
            counter = 0
        for input, target in zip(inputs, targets):
            optimizer.zero_grad()
            output = model(input)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            last_loss = loss.cpu().data.numpy()
            counter = counter + 1
            sum_loss = sum_loss + last_loss

        if stopOnStuck and idx % 10 == 0:
            if last == avg_loss:
                print("Loss: {}".format(avg_loss))
                break
            last = avg_loss

        if targetLoss > 0 and avg_loss < targetLoss:
            print("Loss: {}".format(avg_loss))
            break

        if idx % 100 == 0:
            print("\033[uEpoch: {: >15}    Loss: {}".format(idx, avg_loss))
            print("{: >20} %".format(round(idx / epochs * 10000)/100))
            printBar(0, epochs, idx)

        if idx == epochs - 1:
            print("Loss: {}".format(avg_loss))

def trainGPU(*, model, data, epochs=5000, learningRate=0.1, stopOnStuck=False, targetLoss=0):
    model.cuda()
    inputs = data[0]
    targets = data[1]

    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learningRate)

    avg_loss = 1
    sum_loss = 0
    counter = 0

    print("Max epoch: {: >14}".format(epochs))
    print("Learning rate: {: >10}".format(learningRate))
    if targetLoss != 0:
        print("Target loss: {: >12}".format(targetLoss))
    print()

    print("\033[s")

    for idx in range(0, epochs):
        if counter != 0:
            avg_loss = sum_loss / counter
            sum_loss = 0
            counter = 0
        for input, target in zip(inputs, targets):
            optimizer.zero_grad()
            output = model(input.cuda()).cuda()
            loss = criterion(output, target.cuda())
            loss.backward()
            optimizer.step()
            last_loss = loss.cpu().data.numpy()
            counter = counter + 1
            sum_loss = sum_loss + last_loss

        if stopOnStuck and idx % 10 == 0:
            if last == avg_loss:
                print("Loss: {}".format(avg_loss))
                break
            last = avg_loss

        if targetLoss > 0 and avg_loss < targetLoss:
            print("Loss: {}".format(avg_loss))
            break

        if idx % 10 == 0:
            print("\033[uEpoch: {: >15}    Loss: {}".format(idx, avg_loss))
            print("{: >20} %".format(round(idx / epochs * 10000)/100))
            printBar(0, epochs, idx)

        if idx == epochs - 1:
            print("Loss: {}".format(avg_loss))

def printBar(minimum, maximum, progress):
    left = "["
    right = "]"
    percent = (progress - minimum) / (maximum - minimum)
    bar = '#' * int(round(20 * percent))
    space = ' ' * int(round(20 * (1 - percent)))
    print(left + bar + space + right)

def saveModel(model, path):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=UserWarning)
        torch.save(model, path)
        print("Model saved")

def loadModel(path):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=UserWarning)
        return torch.load(path)

def run(model, data, wholeNum=False):
    tensor = torch.Tensor(data).cpu()
    output = model(tensor)
    if not wholeNum:
        print("output: {}".format(output.cpu().data.numpy()))
    else:
        rounded = []
        for out in output.cpu().data.numpy():
            tmp = round(float(out))
            rounded.insert(len(rounded), tmp)
        print("output: {}".format(rounded))

def parseTrainingData(path):
    raw = open(path, 'r').read()
    data = json.loads(raw)
    inputs = []
    targets = []
    for d in data:
        inputs.insert(0, torch.Tensor(d['input']))
        targets.insert(0, torch.Tensor(d['output']))
    return [inputs, targets]
