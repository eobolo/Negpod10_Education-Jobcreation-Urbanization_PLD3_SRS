!/usr/bin/env bash
echo "============================================WELCOME TO NEGPOD 10 PLD PROJECT==========================================="
sleep 1
echo "=====================================================JOBIFY============================================================"
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
                        echo "Exiting app..."
                        sleep 2
                        exit 0
                        ;;
                *)
                        echo "Invalid input, enter a valid option!"
                        sleep 1
                        ;;
        esac
        echo "Do you want to still use app?"
        sleep 2
        echo "Enter option yes or no:"
        read -r CHOICE
        if [ "$CHOICE" = "yes" ];
        then
                echo "ENTER AN OPTION, 1 to create account, 2 to login, 3 to recover password, 4 to log-out."
                read -r OPTION
        else
                exit 0
        fi
done
