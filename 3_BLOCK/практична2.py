import torch
import torch.nn as nn
import torch.optim as optim
X = torch.tensor([[0.,0.],
[0.,1.],
[1.,0.],
[1.,1.]])
y = torch.tensor([[0.],[0.],[0.],[1.]])
model = nn.Sequential(nn.Linear(2, 1),nn.Sigmoid())

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1000):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
with torch.no_grad():
    preds = model(X)
    print("Передбачення:\n", preds.round())


