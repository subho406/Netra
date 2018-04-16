import io
import time
import picamera
from .base_camera import BaseCamera

from fractions import Fraction

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)
            camera.resolution= BaseCamera.res
            camera.rotation=90
            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream,'jpeg'):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
