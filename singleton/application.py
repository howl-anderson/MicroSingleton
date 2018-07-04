import logging
import os
import sys

import enum
import psutil

logger = logging.getLogger(__name__)


class Action(enum.Enum):
    SINGLETON = 1
    EXIT = 2


class SingletonApplication(object):
    def __init__(self, pid_file_path):
        self.pid_file_path = pid_file_path

    def get_old_pid(self):
        if os.path.exists(self.pid_file_path):
            with open(self.pid_file_path, "r") as pid_file:
                old_pid = int(pid_file.read())
                return old_pid
        else:
            return None

    def action(self, action):
        old_pid = self.get_old_pid()

        if old_pid is not None:
            if old_pid == os.getpid():
                # something is real weird
                msg = (
                    "The old_pid: {} is same with current one. "
                    "This is a small probability event or bug. "
                    "It is treated as previous type event. "
                    "Do nothing."
                ).format(old_pid)
                logger.info(msg)
                return None
            else:
                # if the process with pid pidString is still running
                if psutil.pid_exists(old_pid):
                    if action == Action.EXIT:
                        msg = (
                            "The old_pid: {} still running. "
                            "And the action is EXIT. "
                            "So exit now."
                        ).format(old_pid)
                        logger.info(msg)
                        sys.exit(-1)
                    elif action == Action.SINGLETON:
                        msg = (
                            "The old_pid: {} still running. "
                            "And the action is SINGLETON. "
                            "So kill it now."
                        ).format(old_pid)
                        logger.info(msg)
                        p = psutil.Process(old_pid)
                        p.terminate()  # or p.kill()

        # open pid file for writing
        logger.info("Log new pid")
        with open(self.pid_file_path, "w") as pid_file:
            pid_file.write(str(os.getpid()))
