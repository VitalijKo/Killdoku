import pyautogui
from paddleocr import PaddleOCR

pyautogui.PAUSE = 0.02
SCREENSHOT_DELAY = 1
OCR = PaddleOCR(lang='en', use_gpu=True)
