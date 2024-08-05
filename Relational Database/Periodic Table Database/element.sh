#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

QUERY () {
  TYPE=$($PSQL "SELECT type FROM types INNER JOIN properties ON types.type_id=properties.type_id WHERE properties.atomic_number=$ATOMIC_NUMBER")
  MASS=$($PSQL "SELECT atomic_mass FROM properties WHERE atomic_number=$ATOMIC_NUMBER")
  MELTING_POINT=$($PSQL "SELECT melting_point_celsius FROM properties WHERE atomic_number=$ATOMIC_NUMBER")
  BOILING_POINT=$($PSQL "SELECT boiling_point_celsius FROM properties WHERE atomic_number=$ATOMIC_NUMBER")
  echo "The element with atomic number ${ATOMIC_NUMBER// /} is$NAME (${SYMBOL// /}). It's a$TYPE, with a mass of ${MASS// /} amu.$NAME has a melting point of ${MELTING_POINT// /} celsius and a boiling point of ${BOILING_POINT// /} celsius."
}

if [[ -z $1 ]];
then
  echo -e "Please provide an element as an argument."
else
  if [[ $1 =~ ^[0-9]+$ ]]
  then
    ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE atomic_number=$1")
    if [[ -z $ATOMIC_NUMBER ]] 
    then
      echo "I could not find that element in the database."
    else
      SYMBOL=$($PSQL "SELECT symbol FROM elements WHERE atomic_number=$1")
      NAME=$($PSQL "SELECT name FROM elements WHERE atomic_number=$1")
      QUERY
    fi
  elif [[ ${#1} -eq 2 || ${#1} -eq 1 ]]
  then
    SYMBOL=$($PSQL "SELECT symbol FROM elements WHERE symbol='$1'")
    if [[ -z $SYMBOL ]]
    then
      echo "I could not find that element in the database."
    else
      ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE symbol='$1'")
      NAME=$($PSQL "SELECT name FROM elements WHERE symbol='$1'")
      QUERY
    fi
  else
    NAME=$($PSQL "SELECT name FROM elements WHERE name='$1'")
    if [[ -z $NAME ]]
    then
      echo "I could not find that element in the database."
    else
      ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE name='$1'")
      SYMBOL=$($PSQL "SELECT symbol FROM elements WHERE name='$1'") 
      QUERY
    fi
  fi
fi