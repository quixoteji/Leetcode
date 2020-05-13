import numpy as np

# x = [batch_size, h, w, input_channels]

def conv2d(x, output_channels, 
            kernel_size, stride = 1, 
            padding = 0) : 
    batch_size, height, width, input_channels = x.shape
    kernel = np.random.rand(kernel_size, kernel_size, input_channels, output_channels)

    if padding > 0 : 
        pad_x = np.zeros((batch_size, height + 2 * padding, width + 2 * padding, input_channels))
        pad_x[:,padding:-padding,padding:-padding,:] = x
    else :
        pad_x = x
    
    output_height = (height + 2 * padding - kernel_size) // stride + 1
    output_width = (width + 2 * padding - kernel_size) // stride + 1
    output = np.zeros((batch_size, output_height, output_width, output_channels))

    for i in range(output_height) :
        for j in range(output_width) :
            
            roi_x = pad_x[:, i * stride : i * stride + kernel_size, j * stride : j * stride + kernel_size, :]
            
            conv = np.tile(np.expand_dims(roi_x, -1), (1,1,1,1,output_channels)) * kernel
            
            output[:,i,j,:] = np.sum(conv, axis=(1,2,3))
            
    return output

if __name__ == "__main__":
    images = np.random.rand(2, 10, 10, 3)
    print(images.shape)
    print(conv2d(images, 2, 3, 1, 2).shape)