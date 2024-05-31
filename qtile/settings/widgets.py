#__        ___     _            _
#\ \      / (_) __| | __ _  ___| |_ ___
# \ \ /\ / /| |/ _` |/ _` |/ _ \ __/ __|
#  \ V  V / | | (_| | (_| |  __/ |_\__ \
#   \_/\_/  |_|\__,_|\__, |\___|\__|___/
#                    |___/

from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=15, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerlinel(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=35,
        padding=-2
    )

def powerliner(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=35,
        padding=-2
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Hack Nerd Font',
            fontsize=16,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=2,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['color4'],
            this_screen_border=colors['dark'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=16, padding=5),
        separator(),
    ]

widgets = [
    *workspaces(),

    powerlinel('color4', 'dark'),

    icon(bg="color4", text=' '),
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerliner('color4', 'dark'),

    separator(),
    
    powerlinel('color3', 'dark'),

    icon(bg="color3", text=' '),
    
    widget.CPU(**base(bg='color3'), format = 'Cpu: {load_percent}%'),

    powerliner('color3', 'dark'),

    powerlinel('dark', 'dark'),
        
    icon(bg="dark", fg="light", fontsize=17, text=' '),
    
    widget.Memory(background=colors['dark'], measure_mem='G'),

    powerliner('dark', 'dark'),

    powerlinel('color2', 'dark'),

    icon(bg="color2", fg="dark", fontsize=17, text=' '),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerliner('color2', 'dark'),

    powerlinel('dark', 'dark'),
    
    icon(bg="dark", fg="light", fontsize=17, text='󰕾 '),

    widget.Volume(background=colors['dark'], padding=5, step=5, limit_max_volume=True),

    powerliner('dark', 'dark'),

    powerlinel('color1', 'dark'),

    icon(bg="color1", fontsize=17, text='󰥔 '),

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerliner('color1', 'dark'),

    powerlinel('dark', 'dark'),

    widget.Systray(background=colors['dark'], padding=5),

    powerliner('dark', 'dark'),

]

widget_defaults = {
    'font': 'Hack Nerd Font',
    'fontsize': 15,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
