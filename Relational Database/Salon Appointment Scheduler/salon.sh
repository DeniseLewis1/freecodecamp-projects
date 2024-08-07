#! /bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"

echo -e "\n~~~~~ MY SALON ~~~~~\n"
echo "Welcome to My Salon, how can I help you?"

MAIN_MENU() {
  if [[ $1 ]]
  then
    echo -e "\n$1"
  fi

  SERVICES_LIST=$($PSQL "SELECT service_id, name FROM services")
 
  # display list of services
  echo "$SERVICES_LIST" | while read SERVICE_ID BAR SERVICE
  do
    echo "$SERVICE_ID) $SERVICE"
  done
  
  read SERVICE_ID_SELECTED

  # if service doesn't exist
  if [[ $SERVICE_ID_SELECTED -lt 1 || $SERVICE_ID_SELECTED -gt 5 ]]
  then
    # send to main menu
    MAIN_MENU "I could not find that service. What would you like today?"
  else
      # get service name
      SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id = $SERVICE_ID_SELECTED")
      SERVICE_NAME_FORMATTED=$(echo $SERVICE_NAME | sed -E 's/^ *| *$//g')

      echo -e "\nWhat's your phone number?"
      read CUSTOMER_PHONE

      CUSTOMER_PHONE_CHECK=$($PSQL "SELECT name FROM customers WHERE phone = '$CUSTOMER_PHONE'")

      # if customer doesn't exist
      if [[ -z $CUSTOMER_PHONE_CHECK ]]
      then
        # get new customer name
        echo -e "\nI don't have a record for that phone number, what's your name?"
        read CUSTOMER_NAME

        # insert new customer
        INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name, phone) VALUES('$CUSTOMER_NAME', '$CUSTOMER_PHONE')") 
      fi

      # get customer_id
      CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")

      # get customer name
      CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE customer_id = '$CUSTOMER_ID'")
      CUSTOMER_NAME_FORMATTED=$(echo $CUSTOMER_NAME | sed -E 's/^ *| *$//g')

      echo -e "\nWhat time would you like your $SERVICE_NAME_FORMATTED, $CUSTOMER_NAME_FORMATTED?"
      read SERVICE_TIME

      # insert new appointment
      INSERT_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")

      # send to main menu
       echo -e "I have put you down for a $SERVICE_NAME_FORMATTED at $SERVICE_TIME, $CUSTOMER_NAME_FORMATTED."

       exit 0
  fi
}

MAIN_MENU