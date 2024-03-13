import pyautogui
import time


class RunningLogicAb:
    def process(self):
        raise NotImplementedError("Subclass must implement abstract method")


class AreYouSureYouAreInCopy(RunningLogicAb):
    def process(self):
        pass  # Implement specific logic here


class AccessTeammate(RunningLogicAb):
    def process(self):

        pass  # Implement specific logic here


class Input520(RunningLogicAb):
    def process(self):
        pyautogui.typewrite('520')
        pass  # Implement specific logic here
