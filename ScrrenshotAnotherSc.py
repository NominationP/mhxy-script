# coding: utf-8
from datetime import datetime
from time import sleep

from mss import mss


with mss() as sct:
    while 'capturing':
        filename = datetime.today().strftime("%Y%m%d_%H%M%S.png")
        sct.shot(mon=1, output=filename)
        sleep(1)