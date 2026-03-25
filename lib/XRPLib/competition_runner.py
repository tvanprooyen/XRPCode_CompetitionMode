from XRPLib.competition import *
import time

class CompetitionRunner:
    def __init__(self, board, disable_mode, auto_init, auto_mode, teleop_init, teleop_mode):
        self.board = board
        self.disable_mode = disable_mode
        self.auto_init = auto_init
        self.auto_mode = auto_mode
        self.teleop_init = teleop_init
        self.teleop_mode = teleop_mode

        self.is_auto_init = False
        self.is_teleop_init = False
        self.last_mode = None

    def reset_init(self):
        self.is_auto_init = False
        self.is_teleop_init = False
        self.disable_mode()

    def run(self):
        while True:
            if competition_is_disabled():
                current_mode = "disabled"
            elif competition_is_autonomous():
                current_mode = "auto"
            else:
                current_mode = "teleop"

            if current_mode != self.last_mode:
                self.reset_init()
                self.last_mode = current_mode

            if current_mode == "disabled":
                self.disable_mode()
                self.board.led_off()

            elif current_mode == "auto":
                self.board.led_on()

                if not self.is_auto_init:
                    self.is_auto_init = True
                    self.auto_init()

                self.auto_mode()

            else:
                self.board.led_on()

                if not self.is_teleop_init:
                    self.is_teleop_init = True
                    self.teleop_init()

                self.teleop_mode()

            time.sleep_ms(10)