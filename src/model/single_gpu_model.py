import torch
from torch import nn

class TifUNET(nn.Module):
    def __init__(self, pixel_height, pixel_width, num_channels):
        super().__init__(pixel_height, pixel_width, num_channels)

    def forward(self, input):
        pass