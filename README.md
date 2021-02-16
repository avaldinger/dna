DNA
==== 

Applications written in python as part of the [![CS50 Badge](https://img.shields.io/badge/-CS50-red)](https://cs50.harvard.edu) class problem sets.

Table of content
----
* [General info](#general-info)
* [Setup](#setup)
* [Technologies](#technologies)

### General info

DNA sequence "analyzer" program written in python. The aim of the application is to find so-called STRs (Short Tandem Repeats) in a given DNA code. The program reads in the sequence then it searches for the longest occurence of given STRs. The it cross-checks if the result is matching with any "suspect" that can be found in the database.


### Setup

The application can be run locally or using the [![CS50 Badge](https://img.shields.io/badge/-CS50-red)](https://cs50.harvard.edu) <a href="https://ide.cs50.io">IDE</a> after logging in with your GitHub account.

To run the program:
 1. You need to have Python installed or using the CS50 IDE
 2. To run: `$ python dna.py`
 3. Usage: `python dna.py data.csv sequence.txt`
 
### Technologies
 
 Libraries:
 * csv
 * sys
 * panda
 * [![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
