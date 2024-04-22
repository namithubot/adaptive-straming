:: To play the video
::ffplay -video_size %1x%2 -pixel_format yuv420p dancing_org.%1x%2.yuv
 
:: Encoding the video
ffmpeg -video_size %1x%2 -pixel_format yuv420p -i dancing.%1x%2.yuv -vcodec libx264 -b:v %3k -pixel_format yuv420p -flags psnr out.%3.%1x%2.mp4
 
:: Take Raw Video and Encoded Video -> Convert to Raw Video
ffmpeg -i out.%3.%1x%2.mp4 -format raw_video -pixel_format yuv420p out.%3.%1x%2.yuv