# Linux Terminal tricks
For bash tutorial, use this [link](https://www.thegeekstuff.com/tag/bash-tutorial/)

## How to create file with a numberic prefix within a range and fixed suffix using touch and sed

```bash
seq 10 28 | sed -En "s/(.*)/\1-answer.txt/p" | xargs -t touch
```

## Bash Positional parameters
A parameter is an entity that stores values. It can be a name, a number or some special characters. A variable is a parameter denoted by a name.

Bash provides two kind of parameters.

- Positional Parameter
- Special Parameter

> Positional parameters  are the arguments given to your scripts when it is invoked. It could be from `$1` to `$N`. When N consists of more than a single digit, it must be enclosed in a braces like `${N}`.

```bash
#!/usr/bin/env bash

echo -e  "\$1=$1"
echo -e "\$2=$2"

let add=$1+$2
let sub=$1-$2
```

> Shell builtin ‘let’ allows arithmetic operation to be performed on shell variables.

### How to Set / Unset Bash Positional Parameters
The built in set command is used to set and unset the positional parameter.

```bash
# Store positional parameters with -(hyphen)
set - -f -s -t
echo -e  "\$1=$1" 	# $1=-f
echo -e "\$2=$2"	# $2=-s
echo -e "\$3=$3"	# $3=-t

# Unset positional parameter
set --
echo -e  "\$1=$1"
echo -e "\$2=$2"
echo -e "\$3=$3"
```

## Bash shell Special parameters

The following are bash shell special parameters:
`$*, $@, $#, $$, $!, $?, $-, $_`

You can use bash shell special parameter `$?`

- To access the whole list of positional parameters, the two special parameters `$*` and `$@` are available.
	> Outside of double quotes, these two are equivalent: Both expand to the list of positional parameters starting with `$1` (separated by spaces).

	> Within double quotes, however, they differ: `$*` within a pair of double quotes is equivalent to the list of positional parameters, separated by the first character of `IFS` “$1c$2c$3…”.

	```bash
	# Printing the data available in $*
	echo "Values of \"\$*\":"
	for arg in "$*"
	do
	  echo "Arg #$cnt= $arg"
	  let "cnt+=1"
	done
	```

	```bash
	# Printing the data available in $@
	echo "Values of \"\$@\":"
	for arg in "$@"
	do
	  echo "Arg #$cnt= $arg"
	  let "cnt+=1"
	done
	```

	`$@` within a pair of double quotes is equivalent to the list of positional parameters, separated by unquoted spaces, i.e., “$1” “$2″..”$N”.
- `$#` is the special parameter in bash which gives you the number of positional parameter in decimal.
- The special parameter $$ will give the process ID of the shell. $! gives you the process id of the most recently executed background process.

- `$?` Gives the exit status of the most recently executed command.
- `$-` Options set using set builtin command
- `$_` Gives the last argument to the previous command. At the shell startup, it gives the absolute filename of the shell script being executed.



## Information about PIDs in Unix systems

> The default maximum value of PIDs is `32,767`. The maximum number of processes on a system is only limited by the amount of physical memory (i.e., RAM) available.

> The PIDs for the processes currently on the system can be found by using the [`ps`](http://www.linfo.org/ps.html) or the [`pstree`](http://www.linfo.org/pstree.html) command (which shows the process names and PIDs in a tree diagram).
> The `pidof` command provides the PID of a program whose name is passed to it as an argument (i.e., input).
> Information on current processes is stored in the [`/proc` filesystem](http://www.linfo.org/filesystem.html).

```shell
ls /proc | less
```

> There is a numbered directory in `/proc` corresponding to each PID currently on the system. Each of the directories contains several standard files containing information about the process. For example, the file `cmdline` contains the name of the command (along with any options and arguments) that the process was started with, and it can be easily read with the `cat` or `head` command.
```bash
cat /proc/1/cmdline
```

> More extensive information can be found about any PID and the process it represents by reading the PID's status file, which is also found in its directory in `/proc`. For example, the following would display the contents of the `status` file for PID 1:
```bash
cat /proc/1/status
```


## Linux process management

A process in Linux can go through different states after it’s created and before it’s terminated. These states are:

- Running
A process in running state means that it is running or it’s ready to run.
-   Sleeping
  The process is in a sleeping state when it is waiting for a resource to be available.
    - Interruptible sleep: A process in Interruptible sleep will wakeup to handle signals
    - Uninterruptible sleep: a process in Uninterruptible sleep will not wake to handle signals

- Stopped
A process enters a stopped state when it receives a stop signal.
- Zombie
Zombie state is when a process is dead but the entry for the process is still present in the table.




    A process in Interruptible sleep will wakeup to handle signals, whereas a process in Uninterruptible sleep will not.

    A process enters a stopped state when it receives a stop signal.

    Zombie state is when a process is dead but the entry for the process is still present in the table
