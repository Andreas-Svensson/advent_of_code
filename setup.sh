#!/bin/bash

# error message if no argument was passed when running the script
if [ $# -ne 2 ]; then
    echo "Please provide day and year as arguments"
    exit 1
fi

# name passed arguments
day=$1
year=$2

# create folder for year and data subfolder if they don't exist
mkdir -p "$year"
mkdir -p "$year/data"

if [ $day -lt 10 ]; then
    filename="0${day}" # prepend 0 to single digit days
else
    filename="$day"
fi

# name of .py and .txt file to be created
code_file="${year}/${filename}.py"
data_file="${filename}.txt"

# code to put in .py file
code="# day ${day}, {$year}

# read data
with open('${year}/data/${data_file}', 'r') as file:
    data = file.read()

"
# write code to .py file, and create empty .txt file
echo "$code" > "$code_file"
touch "${year}/data/${data_file}"

echo "Created files for day [${day}] in folder [${year}]"
