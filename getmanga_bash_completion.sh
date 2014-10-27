# getmanga(1) completion
have getmanga &&
_getmanga()
{
    local cur

    COMPREPLY=()
    _get_comp_words_by_ref cur

    if [[ "$cur" == -* ]] ; then
        COMPREPLY=( $( compgen -W '--help -h --info -U -C -L -V' -- "$cur" ) )
    else
        if [ $COMP_CWORD -eq 1 ]; then
            COMPREPLY=( $( compgen -W 'ant btooom claymore liar_game i_am_a_hero zetman \
                                       dorohedoro slam-dunk sun_ken_rock' -- "$cur" ) )
        else
            _filedir rar
        fi
    fi

} &&
complete -F _getmanga getmanga

