# getmanga(1) completion
have getmanga &&
_getmanga()
{
    local cur
    local pathFile="/home/esanchez/lenguajes/python/wget/list_manga.cfg"
    local cmdLine

    while read line
    do
	arrayManga=$(echo $line | tr "\t" "\n")
	for x in $arrayManga
	do
    		cmdLine="$cmdLine $x"
		break
	done
    done < $pathFile
    arrayManga=$(echo $line | tr "\t" "\n")
    for x in $arrayManga
    do
     cmdLine="$cmdLine $x"
     break
    done

    COMPREPLY=()
    _get_comp_words_by_ref cur

    if [[ "$cur" == -* ]] ; then
        COMPREPLY=( $( compgen -W "--help -h --info -U -C -L -V" -- "$cur" ) )
    else
        if [ $COMP_CWORD -eq 1 ]; then
            #COMPREPLY=( $( compgen -W 'ant btooom claymore liar_game i_am_a_hero zetman \
            #                           dorohedoro slam-dunk sun_ken_rock' -- "$cur" ) )
            COMPREPLY=( $( compgen -W "$cmdLine" -- "$cur" ) )
        else
            _filedir rar
        fi
    fi

} &&
complete -F _getmanga getmanga

