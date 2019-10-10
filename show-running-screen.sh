#!/usr/bin/env bash
#screen -ls
LIST=$(screen -ls | grep mc- | cut -c 2- | cut -f1)

#echo $LIST #list all the sessions
i=0
while read -r line; do
	echo -e "\t$i - $line"
	i=$((i+1))
done <<< "$LIST"

#echo ${LIST[0]} #list all the first session
read -p "[ IN ] Write the number of the session: " num
if [ $num -gt '-1' ] && [ $num -lt $i ]; then
	echo "[INFO] Opening: ${LIST["$num"]}..."
	echo "[INFO] Press Ctrl+A+D to exit."
	sleep 2
	screen -r "${LIST["$num"]}"
else
	echo "[FAIL] $num isn't a valid session number."
fi

exit
