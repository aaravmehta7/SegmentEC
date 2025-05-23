import torch
from torch import nn

class TifUNET(nn.Module):
    def __init__(self, pixel_height, pixel_width, num_channels, batch_size):
        super().__init__()
        self.pixel_height = pixel_height
        self.pixel_width = pixel_width
        self.num_channels = num_channels
        self.batch_size = batch_size

    def forward(self, input):
        pass

class Decoder(nn.Module):
    pass

class Encoder(nn.Module):
    pass