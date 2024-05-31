#  ____
# / ___|_ __ ___  _   _ _ __  ___
#| |  _| '__/ _ \| | | | '_ \/ __|
#| |_| | | | (_) | |_| | |_) \__ \
# \____|_|  \___/ \__,_| .__/|___/
#                      |_|

from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.command import lazy
from .keys import mod, keys

groups = [  Group("1", label="一", layout="monadtall"),
            Group("2", label="二", layout="monadtall"),
            Group("3", label="三", layout="monadtall"),
            Group("4", label="四", layout="monadtall"),
            Group("5", label="五", layout="monadtall"),  ]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([Key([mod], actual_key, lazy.group[group.name].toscreen()),
                 Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))])

# ____                 _       _                     _
#/ ___|  ___ _ __ __ _| |_ ___| |__  _ __   __ _  __| |___
#\___ \ / __| '__/ _` | __/ __| '_ \| '_ \ / _` |/ _` / __|
# ___) | (__| | | (_| | || (__| | | | |_) | (_| | (_| \__ \
#|____/ \___|_|  \__,_|\__\___|_| |_| .__/ \__,_|\__,_|___/
#                                   |_|

groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'term',
                'alacritty',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=0.95
            ),
            DropDown(
                'mixer',
                'pavucontrol',
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1
            ),
            DropDown(
                'btop',
                'alacritty -e btop',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=0.95
            ),
            DropDown(
                'ranger',
                'alacritty -e ranger',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=0.95
            ),
        ]))

keys.extend([
    Key([mod], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('btop')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('mixer')),
])
