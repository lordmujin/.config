if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting

setenv EDITOR micro

alias ls="eza -a --icons"
alias ll="eza -al --icons"

neofetch
