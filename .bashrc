# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile

# It's NOT a good idea to change this file unless you know what you
# are doing. It's much better to create a custom.sh shell script in
# /etc/profile.d/ to make custom changes to your environment, as this
# will prevent the need for merging in future updates.

# are we an interactive shell?
if [ "$PS1" ]; then
  if [ -z "$PROMPT_COMMAND" ]; then
    case $TERM in
    xterm*|vte*)
      if [ -e /etc/sysconfig/bash-prompt-xterm ]; then
          PROMPT_COMMAND=/etc/sysconfig/bash-prompt-xterm
      elif [ "${VTE_VERSION:-0}" -ge 3405 ]; then
          PROMPT_COMMAND="__vte_prompt_command"
      else
          PROMPT_COMMAND='printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'
      fi
      ;;
    screen*)
      if [ -e /etc/sysconfig/bash-prompt-screen ]; then
          PROMPT_COMMAND=/etc/sysconfig/bash-prompt-screen
      else
          PROMPT_COMMAND='printf "\033k%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'
      fi
      ;;
    *)
      [ -e /etc/sysconfig/bash-prompt-default ] && PROMPT_COMMAND=/etc/sysconfig/bash-prompt-default
      ;;
    esac
  fi
  # Turn on parallel history
  shopt -s histappend
  history -a
  # Turn on checkwinsize
  shopt -s checkwinsize
  [ "$PS1" = "\\s-\\v\\\$ " ] && PS1="[\u@\h \W]\\$ "
  # You might want to have e.g. tty in prompt (e.g. more virtual machines)
  # and console windows
  # If you want to do so, just add e.g.
  # if [ "$PS1" ]; then
  #   PS1="[\u@\h:\l \W]\\$ "
  # fi
  # to your custom modification shell script in /etc/profile.d/ directory
fi

if ! shopt -q login_shell ; then # We're not a login shell
    # Need to redefine pathmunge, it get's undefined at the end of /etc/profile
    pathmunge () {
        case ":${PATH}:" in
            *:"$1":*)
                ;;
            *)
                if [ "$2" = "after" ] ; then
                    PATH=$PATH:$1
                else
                    PATH=$1:$PATH
                fi
        esac
    }

    # By default, we want umask to get set. This sets it for non-login shell.
    # Current threshold for system reserved uid/gids is 200
    # You could check uidgid reservation validity in
    # /usr/share/doc/setup-*/uidgid file
    if [ $UID -gt 199 ] && [ "`id -gn`" = "`id -un`" ]; then
       umask 002
    else
       umask 022
    fi

    SHELL=/bin/bash
    # Only display echos from profile.d scripts if we are no login shell
    # and interactive - otherwise just process them to set envvars
    for i in /etc/profile.d/*.sh; do
        if [ -r "$i" ]; then
            if [ "$PS1" ]; then
                . "$i"
            else
                . "$i" >/dev/null
            fi
        fi
    done

    unset i
    unset -f pathmunge
fi
# Remaps caps lock to ctrl
xmodmap ~/.speedswapper

# vim:ts=4:sw=4
unset SSH_ASKPASS
eval `ssh-agent -s`
ssh-add
alias install="sudo apt-get install"
alias search="sudo apt-cache search"
alias a="cd /home/gregmccoy/Programming"
alias c="cd /home/gregmccoy/Programming/gfa/gfa-apps"
alias d="cd /home/gregmccoy/Programming/gfa/templates/templates/templates"
alias kb="kubectl"
alias emails="cd /home/gregmccoy/Programming/emails/src/ca"
alias xclip="xclip -selection c"
#alias runemails="python ca.py -f new.html && cat default.html | xclip && echo 'Copied to Clipboard'"
#sh /home/gregmccoy/.scripts/init.sh
alias push="git push origin staging"
alias pull="git checkout master && git pull origin master && git checkout staging && git pull origin staging && git merge master"
alias next="playerctl next"
alias prev="playerctl previous"
alias pause="playerctl play-pause"
alias gitlines="git ls-files | xargs wc -l"
alias gep=grep
alias storage2="smbclient -U canada.gfa.org/gregmccoy //storage2/data/ -m SMB3"
alias shares="sudo mount -t cifs -o username=gregmccoy,domain=canada.gfa.org,vers=3.0 //storage2/data/ /mnt"

export PS1="\[\033[38;5;2m\]\u\[$(tput sgr0)\]\[\033[38;5;15m\]:\[$(tput sgr0)\]\[\033[38;5;21m\]\W\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"
#export KUBECONFIG=/home/gregmccoy/.kube/kubeconfig
# Carina
#source /home/gregmccoy/.dvm/dvm.sh

# The next line updates PATH for the Google Cloud SDK.
source '/home/gregmccoy/Programming/google-cloud-sdk/path.bash.inc'

# The next line enables shell command completion for gcloud.
source '/home/gregmccoy/Programming/google-cloud-sdk/completion.bash.inc'
