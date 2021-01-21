# Telegram Bot for Lviv university
Hello and welcome to my project!
The main goal of the bot is to help students in the learning process. In thin moment bot have two main functions. /get_employeee <faculty> <Name> this function return all info about employee, and /newsletter, this function once a day return actual news in your faculty. In order to set the name of your faculty, you should call function /set_faculty <your_faculty>.
  
  # Bot structure 
  ```
LNUBOT
    ├──  data                 - this folder contains all database models.
    │   ├── database.py             - database for bot
    │
    ├── parse_functions             - this folder contains all parse functions.
    │   └── parse_request.py    
    │   
    │   
    ├── settings               - here stored different constant values, connection parameters, etc.
    │   └── constants.py        -  multiple constants storage for their convenient usage.
    │ 
    └── bot.py                  - bot file to run.
    
```
## Main components
python-telegram-bot, sqlalchemy, BeautifulSoup

# Example how functions work

## Function /get_employee 

<div align="center">
    <img align="center" src="https://github.com/Fesh1/LNUBOT/blob/main/get_employee?raw=true" width="320">
</div>

## Function /reminder

<div align="center">
    <img align="center" src="https://github.com/Fesh1/LNUBOT/blob/main/reminder?raw=true" width="320">
</div>

## Function /get_article_by_id

<div align="center">
    <img align="center" src="https://github.com/Fesh1/LNUBOT/blob/main/get_article_by_id?raw=true" width="320">
</div>
