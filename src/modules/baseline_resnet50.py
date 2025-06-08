import os
import torch
from torchvision import datasets, transforms, models
from torchvision.models import ResNet50_Weights
import torch.nn as nn
from torch.utils.data import DataLoader
import time

class BaselineResNet50:
    def __init__(self, size: int, data_path: str, batch_size: int = 4, device: str = "cpu"):
        transform = transforms.Compose([
            transforms.Resize((size, size)), 
            transforms.ToTensor(),
        ])

        train_dir = os.path.join(data_path, "train")
        val_dir = os.path.join(data_path, "val")

        train_dataset = datasets.ImageFolder(root=train_dir, transform=transform)
        val_dataset = datasets.ImageFolder(root=val_dir, transform=transform)

        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size)

        num_classes = len(train_dataset.classes)
        

        self.model = models.resnet50(weights=None)
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

        self.device = device
        self.model = self.model.to(self.device)

        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=3, gamma=0.1)

        print(f"Using {self.device}")
        print(f"Found {num_classes} classes: {train_dataset.classes}")


    def train(self, num_epochs=5):
        start_time = time.time()
        acc = 0.0

        for epoch in range(num_epochs):
            self.model.train()
            running_loss = 0.0
            correct = 0
            total = 0
            
            for inputs, labels in self.train_loader:
                inputs, labels = inputs.to(self.device), labels.to(self.device)

                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

                running_loss += loss.item()
                _, predicted = outputs.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()

            acc = 100.0 * correct / total
            self.scheduler.step()
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss:.4f}, Accuracy: {acc:.2f}%, Time: {(time.time()-start_time):.2f}s")

        self.training_time = time.time() - start_time
        print(f"\nTraining ended. Time: {self.training_time:.2f} seconds")
        torch.save(self.model.state_dict(), f"data/models/model_acc_{acc:.3f}.pth")

    def evaluate(self):
        correct = 0
        total = 0

        self.model.eval()
        with torch.no_grad():
            for inputs, labels in self.val_loader:
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                outputs = self.model(inputs)
                _, predicted = outputs.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()

        accuracy = 100. * correct / total
        print(f"Dokładność na zbiorze walidacyjnym: {accuracy:.2f}%")
        return accuracy
