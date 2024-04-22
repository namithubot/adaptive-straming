import subprocess
import matplotlib.pyplot as plt
from run import get_psnr
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d

# Define YUV file path and dimensions
yuv_file = "path/to/your/yuv_file.yuv"
dimensions = [
    (1280, 548),
    (320, 138),
    (640, 274),  # Replace with your desired dimensions
]

# Define bitrates for encoding
bitrates = {
	1280: [ 512, 1024, 2048, 3072 ],
	640: [96, 128, 256, 384, 512, 1024, 2048 ],
	320: [64, 96, 128, 256, 512, 1024],
}

# Function to encode with ffmpeg and calculate PSNR (replace with your PSNR calculation method)
def encode_and_get_psnr(bitrate, dim):
    # Replace this with your preferred PSNR calculation method (e.g., using VMAF score)
    psnr = calculate_psnr(yuv_file, f"output_{dim[0]}x{dim[1]}_{bitrate}.yuv")
    return psnr

# Encode videos and store PSNR values
psnr_values = {}
for dim in dimensions:
    psnr_list = []
    for bitrate in bitrates[dim[0]]:
        # Encode video with ffmpeg command
        command = [
			"cmds.bat",
			f"{dim[0]}",
			f"{dim[1]}",
			f"{bitrate}",
        ]
        #subprocess.run(command)

        # Calculate PSNR (replace with your method using encode_and_get_psnr)
        psnr = get_psnr(bitrate, dim[0], dim[1])
        psnr_list.append(psnr)
    psnr_values[dim[0]] = psnr_list

#Plotting PSNR vs Bitrate
print(psnr_values)
plt.figure(figsize=(8, 6))
all_points = []
for i, dim in enumerate(dimensions):
    points = np.column_stack((bitrates[dim[0]], psnr_values[dim[0]]))
    all_points.extend(points)
    plt.plot(bitrates[dim[0]], psnr_values[dim[0]], label=f"{dim[0]}x{dim[1]}")

# Convert all_points to a 2D array
all_points = np.array(all_points).reshape(-1, 2)
print(all_points)

# Add convex hull
hull = ConvexHull(all_points)
vertices = hull.vertices

plt.plot(all_points[vertices, 0], all_points[vertices, 1], '--o', color='black', linewidth=1, alpha=0.5, label="Convex Hull")

plt.xlabel("Bitrate (kbps)")
plt.ylabel("PSNR (dB)")
plt.title("PSNR vs Bitrate for Different Resolutions")
plt.legend()
plt.grid(True)
plt.show()

print("Encoding and PSNR calculation completed. Graphs displayed.")