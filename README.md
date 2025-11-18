# Expert System Report and Functionality

This laptop advisor is not built on an AI model, it is a simple expert system built on assertions, based on a couple rules that are provided to the user by the system. The rules are pre-loaded into json object which is later put into engine which utilizes a forward chaining engine function which follows the standard procedure of checking all the antecedents and then the consequent. The expert system has a main module which is where the user interacts with the system to assert if a need is “Yes” or “No” then spits out recommendations (if possible) and then it tells the user how it derived those specifications. 

# TO RUN MAIN MODULE (if needed)
```
python3 main.py
```