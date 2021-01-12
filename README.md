# Desktop application for library

Our application is for library management for Universities, Schools, or something like this.
It makes work at the library much easier.
You can run it on Windows, Linux, MacOS.

## Technologies
 * Python + Tkinter
 * PostgreSQL

## To run it you need:
- Install Python
- Install PostgreSQL
- Clone this repository
```
  $ git clone https://github.com/GreatHorizon/library.git
  $ cd library
```
- 1)Install and create virtualenv from [this guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
  2)Activate your virtualenv.
  3)Install required packages by the following command:
```
  $ (env)pip3 install requests requirements.txt
  
```
- Create database and run library.sql
- Write your database config into .env file
```
  DB_NAME=<your db name>
  USER=<db user name>
  HOST=<localhost>
  PASSWORD=<your password>
```
## Thats all. Good luck!
