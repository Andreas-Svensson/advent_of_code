#!/bin/bash

# error message if no argument was passed when running the script
if [ $# -ne 2 ]; then
    echo "Please provide the day and year as arguments when running the script."
    exit 1
fi

# name passed arguments
day=$1
year=$2
foldername=$year

echo "Creating files for day [${day}] in folder [${foldername}]..."

# create target folder and subfolder if they don't exist
mkdir -p "$foldername"
mkdir -p "$foldername/data"

if [ $day -lt 10 ]; then
    filename="0${day}" # prepend 0 to single digit days
else
    filename="$day"
fi

# name of .py and .txt file to be created
code_file="${foldername}/${filename}.py"
data_file="${filename}.txt"

# boilerplate code to put in .py file
boilerplate_code="# day ${day}, {$year}

# read data
with open('${foldername}/data/${data_file}', 'r') as file:
    data = file.read()

# review data formatting
print(data)

# part 1
def part_one(data):
    return

print(f'Part one: {part_one(data)}')

# part 2
def part_two(data):
    return

print(f'Part two: {part_two(data)}')

"
# create .py file with boilerplate code, and empty .txt file
echo "$boilerplate_code" > "$code_file"
touch "${foldername}/data/${data_file}"

echo "Setup finished"
