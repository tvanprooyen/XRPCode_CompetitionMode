import sys
import time
import _thread

COMP_MODE_TELEOP = 0
COMP_MODE_AUTONOMOUS = 1
COMP_MODE_DISABLED = 2
COMP_MODE_ENABLED = 3

_COMP_PREFIX = chr(30)  # ASCII Record Separator (\x1e) — competition mode packet prefix
_mode_ref = [COMP_MODE_TELEOP]      # teleop or autonomous
_enabled_ref = [True]               # enabled or disabled

__all__ = [
    "COMP_MODE_TELEOP",
    "COMP_MODE_AUTONOMOUS",
    "COMP_MODE_DISABLED",
    "COMP_MODE_ENABLED",
    "competition_get_mode",
    "competition_get_mode_name",
    "competition_is_autonomous",
    "competition_is_enabled",
    "competition_is_disabled",
    "competition_set_mode",
    "competition_set_enabled",
    "competition_set_disabled",
    "competition_init",
]


def competition_get_mode():
    """Return the current competition mode (COMP_MODE_TELEOP or COMP_MODE_AUTONOMOUS)."""
    return _mode_ref[0]


def competition_get_mode_name():
    """Return the current mode as a string ('TELEOP' or 'AUTONOMOUS')."""
    return "AUTONOMOUS" if _mode_ref[0] == COMP_MODE_AUTONOMOUS else "TELEOP"


def competition_is_autonomous():
    """Return True if the current competition mode is Autonomous."""
    return _mode_ref[0] == COMP_MODE_AUTONOMOUS


def competition_is_enabled():
    """Return True if the robot is currently enabled."""
    return _enabled_ref[0]


def competition_is_disabled():
    """Return True if the robot is currently disabled."""
    return not _enabled_ref[0]


def competition_set_mode(mode):
    """
    Set the competition mode from code.

    :param mode: COMP_MODE_TELEOP or COMP_MODE_AUTONOMOUS
    """
    if mode not in (COMP_MODE_TELEOP, COMP_MODE_AUTONOMOUS):
        raise ValueError("mode must be COMP_MODE_TELEOP or COMP_MODE_AUTONOMOUS")
    _mode_ref[0] = mode


def competition_set_enabled(enabled=True):
    """
    Enable or disable the robot from code.

    :param enabled: True to enable, False to disable
    :type enabled: bool
    """
    _enabled_ref[0] = bool(enabled)


def competition_set_disabled():
    """Disable the robot from code. Shorthand for competition_set_enabled(False)."""
    _enabled_ref[0] = False


def _competition_mode_listener():
    """Background thread: listens on stdin for live mode-switch packets from the IDE."""
    while True:
        try:
            c = sys.stdin.read(1)
            if not c:
                time.sleep(0.01)
                continue
            if c == _COMP_PREFIX:
                m = ''
                for _ in range(20):
                    m = sys.stdin.read(1)
                    if m:
                        break
                    time.sleep(0.005)
                if m == '0':
                    _mode_ref[0] = COMP_MODE_TELEOP
                elif m == '1':
                    _mode_ref[0] = COMP_MODE_AUTONOMOUS
                elif m == '2':
                    _enabled_ref[0] = False  # disabled
                elif m == '3':
                    _enabled_ref[0] = True   # enabled
        except Exception:
            time.sleep(0.05)


def competition_init(initial_mode=COMP_MODE_TELEOP, initial_enabled=True):
    """
    Set the starting mode/state and start the background listener thread.
    Called automatically by Competition Mode in the XRP Code IDE.
    Safe to call from user code to manually enable competition mode.
    """
    _mode_ref[0] = initial_mode
    _enabled_ref[0] = initial_enabled
    _thread.start_new_thread(_competition_mode_listener, ())
