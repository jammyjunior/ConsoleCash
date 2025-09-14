# ConsoleCash
A cash register without a traditional UI. ConsoleCash brings you a console interface that feels just like Linux. It looks simple, but it’s powerful — just like the Linux terminal.

[Before you begin](#before-you-begin)
- [Requirement](#requirement)
- [Download ConsoleCash](#download-consolecash)
- [Run ConsoleCash](#run-consolecash)

[User Guide](#user-guide)
- [Add Command](#add-command)
- [Calculate Command](#calculate-command)
- [Clear Command](#clear-command)
- [Exit Command](#exit-command)
- [Help Command](#help-command)
- [List Command](#list-command)
- [Remove Command](#remove-command)
- [Update Command](#update-command)

[Contributing](#contributing)

## Before you begin

### Requirement
Python 3 must be installed. Download Python from [python.org](https://python.org).

### Download ConsoleCash
If you've installed Git, we highly recommend clone the repository.
```
git clone https://github.com/jammyjunior/ConsoleCash.git
```
Or you can also go to `code`, click `Download ZIP` to download the project. Then unzip the file.

![download](assets/readme/image1.png)

### Run ConsoleCash
On Windows, open Command Prompt.    <br/>
On Linux or macOS, open Terminal.

Then type:
```
python3 /path/to/your/file/ConsoleCash/ConsoleCash.py
```
If you see this one, congrats, now you can start using ConsoleCash.
```
    #############################
    #                           #
    #        ConsoleCash        #
    #                           #
    #############################

Welcome to ConsoleCash! For a new user, type 'help' for help, 'exit' to exit.
console@consolecash:~$ 
```

## User Guide
### Add Command
To add a new item, type `a` or `add` to the console. Then, you enter the values ​​one by one. For example:
```
console@consolecash:~$ add
Item name: Iphone 16
Price: 999
Quantity: 2
```

### Calculate Command
To calculate the total of all the items, type `c` or `calculate`.
```
console@consolecash:~$ calculate
Items in register:

Name                                Price      Quantity  
-------------------------------------------------------
Iphone 16                           999.00     2         
Macbook Pro                         1999.00    1         

Total: 3997.00 $
````

### Clear Command
To clear the console, type `clear`.     <br/>
*Note: Clear command doesn't wiped out your data. It just makes your console looks much cleaner.


### Exit Command
To exit the console, type `e` or `exit`.    <br/>
*Note: All your data you've add will be removed.

### Help Command
To display all available commands, type `h` or `help`.


### List Command
To list all existing items, type `l` or `list`.
```
console@consolecash:~$ list
Items in register:

Name                                Price      Quantity  
-------------------------------------------------------
Iphone 16                           999.00     2         
Macbook Pro                         1999.00    1   
```

### Remove Command
To remove an item, type `r` or `remove`. Then type the item name that you want to remove. For example:
```
console@consolecash:~$ remove 
Item name to remove: Iphone 16
```

To remove all existing items, type `r -a` or `remove -all`. <br/>
*Note: All your data you've add will be removed.

### Update Command
To update an existing item, type `u` or `update`. Then, you enter the new values ​​one by one. For example:
```
console@consolecash:~$ update 
Item name to update: Iphone 16
Price: 899
Quantity: 2
```

## Contributing
Pull requests are welcome!

This project isn't perfect, and I'm always looking for ways to improve it. If you're interested in helping, feel free to submit a pull request.

I want to make ConsoleCash more complicated. If you have any ideas, share it with me.

Thanks for your help! ❤️

