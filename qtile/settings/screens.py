# ____
#/ ___|  ___ _ __ ___  ___ _ __  ___
#\___ \ / __| '__/ _ \/ _ \ '_ \/ __|
# ___) | (__| | |  __/  __/ | | \__ \
#|____/ \___|_|  \___|\___|_| |_|___/

from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 30, opacity=0.8, margin=5)


screens = [Screen(top=status_bar(widgets))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))
