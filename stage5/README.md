Stage 5: Choose Your Path - Back End
====================================

For the fifth part of the Introduction to Programming Nanodegree at Udacity, I decided to choose the Tournament Results project from the Full Stack Nanodegree.

`tournament.py` is a Python module that uses a PostgreSQL database to keep track of players and matches in a game tournament. Following the Swiss system, players are not eliminated, instead being paired up with a player with the same or closest to the same amount of wins.

This does not follow the Swiss system entirely, being a more simplified version. `tournament_test.py` is a series of tests to check that the parts all work correctly.

The work in `tournament.sql` is all my own, with all the function code besides the `connect` function also done by me. Udacity provided the rest of  `tournament.py` and created `tournament_test.py` entirely.


Requirements
------------

Python 2.7 should be installed.

This project also makes use of PostgreSQL, but the instructions below will walk through setting up a virtual machine with PostgreSQL.


How to Setup VM
---------------

These instructions setup a virtual machine, which will be assumed to be used with this project. More details and troubleshooting can be found here: [Installing the Vagrant VM for ud197](https://www.udacity.com/wiki/ud197/install-vagrant)

### Step 1

Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads). Ubuntu 14.04 users should install VirtualBox from the repositories.

### Step 2

Clone the [fullstack-nanodegree-vm repository](http://github.com/udacity/fullstack-nanodegree-vm).

### Step 3

Open a terminal window at the `vagrant` directory of the cloned repository. Run the command:
```
vagrant up
```

Vagrant will then setup a virtual machine.


How to Run Project
------------------

### Step 1

You need `tournament.py`, `tournament.sql`, and `tournament_test.py`. You can clone this repository to download all the files.

Inside the `vagrant` directory from setting up your virtual machine previously, there is a `tournament` folder. Copy the three files into that folder, overwriting the existing files.

(If you'd rather not overwrite the files, feel free to create a separate folder within `vagrant` and follow the instructions with the new folder instead.)

### Step 2

Open a terminal window at the `vagrant` directory. Run the commands:
```
vagrant up
vagrant ssh
```

This will start up the virtual machine and log into it.

### Step 3

Change the VM's directory to the `tournament` folder with the command:
```
cd /vagrant/tournament
```

### Step 4

The following command will startup PostgreSQL:
```
psql
```

You will then want to create a database named `tournament` with the following command:
```sql
CREATE DATABASE tournament;
```

Exit psql by pressing Ctrl+Z (Cmd+Z on Macs).

### Step 5

Then, something similar is done for setting up the `tournament` database. Enter the command:
```
psql tournament
```

Then import `tournament.sql` into the database with:
```sql
\i tournament.sql
```

After that, exit psql.

### Step 6

You can now run `tournament_test.py` with:
```
python tournament_test.py
```


How to Run Project Afterward
----------------------------

Once you have done all the previous steps, there's only a few you need to repeat whenever you want to run this project later on.

### Step 1

Open a terminal window at the `vagrant` directory. Start up Vagrant and log in.

```
vagrant up
vagrant ssh
```

### Step 2

Change the VM's directory to the `tournament` folder.

```
cd /vagrant/tournament
```

### Step 3

You can now run `tournament_test.py` with:
```
python tournament_test.py
```

