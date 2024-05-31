# _                            _
#| |    __ _ _   _  ___  _   _| |_ ___
#| |   / _` | | | |/ _ \| | | | __/ __|
#| |__| (_| | |_| | (_) | |_| | |_\__ \
#|_____\__,_|\__, |\___/ \__,_|\__|___/
#            |___/

from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = { 'border_focus': colors['focus'][0],
                'border_width': 1,
                'margin': 5}

layouts = [ layout.Max(),
            layout.MonadTall(**layout_conf),
            layout.Matrix(columns=2, **layout_conf),]

floating_layout = layout.Floating(float_rules=[
                    *layout.Floating.default_float_rules,
                    Match(wm_class="confirmreset"), Match(wm_class="dialog"),        
                    Match(wm_class="download"), Match(wm_class="error"),   
                    Match(wm_class="file_progress"), Match(wm_class='kdenlive'),     
                    Match(wm_class="makebranch"), Match(wm_class="maketag"),       
                    Match(wm_class="notification"), Match(wm_class='pinentry-gtk-2'), 
                    Match(wm_class="ssh-askpass"), Match(wm_class="toolbar"),       
                    Match(wm_class="Yad"), Match(title="branchdialog"),     
                    Match(title='Confirmation'), Match(title='Qalculate!'),      
                    Match(title="pinentry"), Match(title="tastycharts"),      
                    Match(title="tastytrade"), Match(title="tastytrade - Portfolio Report"), 
                    Match(wm_class="tasty.javafx.launcher.LauncherFxApp"),
                    Match(wm_class="pavucontrol"),
                    Match(wm_class="nvidia-settings"),
                    Match(wm_class="octopi"),

                    ],
                    border_focus=colors["color2"][0])
