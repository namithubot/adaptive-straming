import cv2
import numpy as np

# Define file paths (modify as needed)
ref_path = "dancing.1280x548.yuv"

# Video properties (adjust if necessary)
n_frames = 120
hres = 1280
vres = 548
npels = hres * vres * 1.5  # Account for YUV420p format


def get_psnr(bitrate, comp_hres, comp_vres):
    comp_path = f'out.{bitrate}.{comp_hres}x{comp_vres}.yuv'
    # Initialize PSNR array for storing frame-wise values
    psnr = np.zeros(n_frames)
    comp_nprels = comp_hres * comp_vres * 1.5

    # Open video files for reading
    ref_in = open(ref_path, "rb")
    comp_in = open(comp_path, "rb")

    for frame in range(n_frames):
        # Read frame data from both files
        ref_data = np.fromfile(ref_in, dtype=np.uint8, count=int(npels))
        comp_data = np.fromfile(comp_in, dtype=np.uint8, count=int(comp_nprels))

        # Reshape Y component efficiently using slicing and view conversion
        ref_y = ref_data[:hres * vres].reshape((vres, hres)).T.astype(np.float64)  # Reshape + transpose + cast
        comp_y = comp_data[:comp_hres * comp_vres].reshape((comp_vres, comp_hres)).T.astype(np.float64)
        comp_y = cv2.resize(comp_y, (vres, hres), interpolation = cv2.INTER_LINEAR)

        # Calculate PSNR (mean squared error approach)
        psnr[frame] = cv2.PSNR(ref_y, comp_y)
        # mse = np.mean(np.square(ref_y - comp_y))
        # if mse == 0:  # Avoid division by zero
        #     psnr[frame] = float('inf')  # Set PSNR to infinity
        # else:
        #     psnr[frame] = 10 * np.log10((255 * 255) / mse)

    # Close video files
    ref_in.close()
    comp_in.close()

    # Print or process PSNR values (optional)
    print("PSNR values:", np.average(psnr))
    return np.average(psnr)

#print(get_psnr('out.256.640x274.yuv', 650, 274))