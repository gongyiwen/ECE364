if [[ $# != 3 ]]
	then
	    echo "Error: Insufficient information."
	    exit 1
	fi
	
	while getopts f:-: thisopt
	do
	        case $thisopt in         
	          f)echo $OPTARG
		    if [[ ! -e $OPTARG ]]
		    then
			echo "Error: File does not exist."
			exit 1
		    else	    
			input=$OPTARG
			output=$input'.sorted'
		    fi;;
	          -)val=$(echo $OPTARG  | cut -d'=' -f2)
	            #echo $val ;;
			if [[ $val > 4 ]]
			then
			    echo "Error: Column number $val does not exist."
			    exit 1
			fi
			if [[ $val < 0 ]]
			then
			    echo "Error: Unknown option."
			    exit 1
			fi
			sort -k $val,$val -t" " $input >> $output;;
	          *)echo "Invalid arg";;
	        esac
	done
	exit 0