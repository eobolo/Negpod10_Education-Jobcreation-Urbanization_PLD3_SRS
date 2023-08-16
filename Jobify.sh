#!/usr/bin/env bash
GREEN='\033[0;32m'
BLUE='\033[0;34m'
no_c='\033[0m'
RD='\033[0;31m'

echo -e "${GREEN}\n\n\n\n**************************************************************************************************************************************************\n\n\n  ==========================================================WELCOME TO NEGPOD 10 PLD PROJECT===================================================\n\n\n****************************************************************************************************************************************************${no_c}"

sleep 1
echo -e "${BLUE}\n==================================================================JOBIFY===========================================================================\n\n\n${no_c}"
sleep 1


echo "-----ENTER 1 TO CREATE AN ACCOUNT-----"
sleep 1
echo "-----ENTER 2 TO LOGIN-----"
sleep 1
echo "-----ENTER 3 TO RECOVER PASSWORD-----"
sleep 1
echo "-----ENTER 4 TO EXIT-----"
sleep 1
echo "ENTER VALID OPTION:"
read -r OPTION
while true;
do
	case $OPTION in
		1)
			python3 "create_account.py"
			;;
		2)
			python3 "login.py"
			;;
		3)
			python3 "forget_details.py"
			;;
		4)
			echo -e "${GREEN}Exiting app...${no_c}"
			sleep 2
			exit 0
			;;
		*)
			echo -e "${RD}Invalid input, enter a valid option!${no_c}"
			sleep 1
			;;
	esac
	echo -e  "\n Do you want to still use app?\n"
	sleep 2
	echo "Enter option yes or no: "
	read -r CHOICE
	if [ "$CHOICE" = "yes" ];
	then
		echo -e "\nSELECT AN OPTION\n 1 to create account\n 2 to login\n 3 to recover password\n 4 to log-out.\n ENTER VALID OPTION: "
		read -r OPTION
	else
		echo -e "${RD}\nExiting app ...${no_c}"
		sleep 1
		exit 0
	fi
done
