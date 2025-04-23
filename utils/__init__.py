import sys
sys.path.append(__file__)

from .config import DEBUG

from .videoCapture import VideoCapture
from .inference import Inference
from .videoStream import VideoStream
