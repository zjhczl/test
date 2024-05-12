# 无人机远程监控
from gi.repository import Gst, GLib
import sys
import time
from threading import Thread
import gi
gi.require_version("Gst", "1.0")
Gst.init(sys.argv)

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()

# 调取摄像头
# windows：ksvideosrc
# mac：autovideosrc
# linux：v4l2src
pipeline = Gst.parse_launch(
    "rtmpsrc location=rtmp://gis.breton.top:1935/live/123456 ! flvdemux ! h264parse ! avdec_h264 ! autovideosink sync=false async=false")


# pipeline = Gst.parse_launch(
# "rtmpsrc location=rtmp://192.168.1.50:1935/live/1695630109819 ! flvdemux ! h264parse ! nvdec ! glimagesink sync=false")
# pipeline = Gst.parse_launch(
#     "rtmpsrc location=rtmp://192.168.1.50:1935/live/1695630109819 ! decodebin! videoconvert ! autovideosink")

pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        time.sleep(0.01)
        pass
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()
