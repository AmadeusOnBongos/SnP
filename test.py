import torch
print(torch.version.cuda)
print(torch.cuda.is_available())        # Should be True
# print(torch.cuda.get_device_name(0))    # Should print your GPU
# print(torch.version.cuda)               # Should say '12.1'
