#$Author: ee364e03 $
#$Date: 2015-08-31 22:01:34 -0400 (Mon, 31 Aug 2015) $
#$Revision: 80958 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab01/svncheck.bash $
#$ID$ 

while read line || [[ -n "$line" ]]
do
STATUS=$(svn status $line | head -c 1)
if [[ $STATUS == "?" && -e $line ]] 
  then  
    if [[ ! -x $line ]]
      then
        echo -n  "Executable? y/n "
        read input < /dev/tty
        if [[ $input == "y" ]]
          then 
          chmod  a+x $line
        fi
    fi
  svn add $line
fi
if [[ $STATUS != "?" &&  ! -x $line && -e $line ]]
  then
  svn propset svn:executable ON $line
fi
if [[ ! -e $line ]]
  then
  echo "Error:File $line appears to not exist here or in svn"
fi

done < file_list
svn commit -m "Auto committing code"
echo "Auto committing code"
exit 0
