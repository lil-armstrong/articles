## Resources

Read or watch:

-   [Loops sample](https://intranet.alxswe.com/rltoken/wT98UJfv_E2tk4yP9PcLLw)
-   [Variable assignment and arithmetic](https://intranet.alxswe.com/rltoken/olvOKX699pq50rkHRE5cSA)
-   [Comparison operators](https://intranet.alxswe.com/rltoken/HxohzllkOWh0t4dy_HptIQ)
-   [File test operators](https://intranet.alxswe.com/rltoken/g8of2ABPEJfCNtPrDQaqVw)
-   [Make your scripts portable](https://intranet.alxswe.com/rltoken/O0Ay21p7tDhfLMsYbtAKug)

man or help:

-   `env`
-   `cut`
-   `for`
-   `while`
-   `until`
-   `if`

**ShellCheck - A shell script static analysis tool**

> `ShellCheck` is a GPLv3 tool that gives warnings and suggestions for bash/sh shell scripts.

`Shellcheck` is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! **All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task**.

`Shellcheck` is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://intranet.alxswe.com/rltoken/jbz0_-i3TV3WpKgxhyrtpA).

## Operators

### **Assignment**

All-purpose assignment operator, which works for both arithmetic and string assignments.

```bash
var=27
category=minerals  # No spaces allowed after the "=".
```

**Caution**

Do not confuse the "=" assignment operator with the = test operator.

```bash
#   =  as a test operator

if [ "$string1" = "$string2" ]
then
   command
fi
```

**Arithmetic**

-   Plus (+)

```shell
n=1
let "n=$n + 1"
```

-   Minus (-)
-   Multiplication (\*)
-   Division (/)
-   Exponentiation (\*\*)

    ```bash
    # Bash, version 2.02, introduced the "**" exponentiation operator.

    let "z=5**3"    # 5 * 5 * 5
    echo "z = $z"   # z = 125
    ```

-   Modulo(%)
-   Plus-equal(`+=`)
-   Minus-equal(`-=`)
-   Times-equal(`*=`)
-   Slash-equal(`/=`)
-   Mod-equal(`%=`)

> Bash does not understand floating point arithmetic. It treats numbers containing a decimal point as strings.

```bash
a=1.5

let "b = $a + 1.3"  # Error.
# t2.sh: let: b = 1.5 + 1.3: syntax error in expression
#                            (error token is ".5 + 1.3")

echo "b = $b"       # b=1
```

> Use **bc** in scripts that that need floating point calculations or math library functions

**Bitwise**

-   Bitwise left shift(<<)
-   Left-shift-equal (<<=)
-   Left-shift-equal (<<=)
-   Bitwise right shift (>>)
-   Right-shift-equal (inverse of <<=)
-   Bitwise AND (&)
-   Bitwise AND-equal (&=)
-   Bitwise OR (|)
-   Bitwise OR-equal (|=)
-   Bitwise NOT(~)
-   Bitwise XOR (^)
-   Bitwise XOR-equal(^=)

**Logical**

-   NOT (!)
-   AND (&&)
-   OR (||)

**Miscllaneous**

-   Comma (,)

### Comparison

> There is some blurring between the arithmetic and string comparisons, since Bash variables are not strongly typed.

**Integer comparison**

-   Equal to (-eq)
-   Not equal to (-ne)
-   Greater than (-gt)
-   Greater than or equal to (-ge)
-   Less than (-lt)
-   Less than or equal to (-le)
-   Less than (<)
-   Less than or equal (<=)
-   Greater than (>)
-   Greater than or equal(>=)

**String comparison**

-   Equal to (`=`)

    ```bash
    if [ "$a" = "$b" ]
    ```

    > **Caution:**
    > Note the whitespace framing the =.

    `if [ "$a"="$b" ]` is not equivalent to the above.

-   Equal to (`==`)

    `if [ "$a" == "$b" ]`
    This is a synonym for `=`.
    The `==` comparison operator behaves differently within a double-brackets test than within single brackets.

    ```bash
    [[ $a == z* ]]   # True if $a starts with an "z" (pattern matching).
    [[ $a == "z*" ]] # True if $a is equal to z* (literal matching).

    [ $a == z* ]     # File globbing and word splitting take place.
    [ "$a" == "z*" ] # True if $a is equal to z* (literal matching).
    ```

-   Not equal to (!=):

```bash
if [ "$a" != "$b" ]
```

-   Less than (`<`)

```bash
if [[ "$a" < "$b" ]]
if [ "$a" \< "$b" ]
```

> **Note:** that the `<` needs to be escaped within a `[ ]` construct.

-   Greater than (`>`)

```bash
if [[ "$a" > "$b" ]]
if [ "$a" \> "$b" ]
```

> **Note:** that the `>` needs to be escaped within a `[ ]` construct.

-   is NULL (`-z`): string is null

```bash
 String=''   # Zero-length ("null") string variable.

if [ -z "$String" ]
then
  echo "\$String is null."
else
  echo "\$String is NOT null."
fi     # $String is null.
```

-   is NOT NULL (`-n`) - string is not null

**Compound comparison**

-   Logical and (-a)

    `exp1 -a exp2` returns true if both exp1 and exp2 are true.

-   Logical or (-o)

    `exp1 -o exp2` returns true if either exp1 or exp2 is true.

> These are similar to the Bash comparison operators `&&` and `||`, used within double brackets.

```bash
if [ "$expr1" -a "$expr2" ]
then
  echo "Both expr1 and expr2 are true."
else
  echo "Either expr1 or expr2 is false."
fi
```

But

```bash
[ 1 -eq 1 ] && [ -n "`echo true 1>&2`" ]   # true
[ 1 -eq 2 ] && [ -n "`echo true 1>&2`" ]   # (no output)
# ^^^^^^^ False condition. So far, everything as expected.
# However ...
[ 1 -eq 2 -a -n "`echo true 1>&2`" ]       # true
# ^^^^^^^ False condition. So, why "true" output?

# Is it because both condition clauses within brackets evaluate?
[[ 1 -eq 2 && -n "`echo true 1>&2`" ]]     # (no output)
# No, that's not it.

# Apparently && and || "short-circuit" while -a and -o do not.
```

## Loops

### for loops

```bash
for arg in [list]
do
 command(s)...
done
```

```bash
for arg in "$var1" "$var2" "$var3" ... "$varN"
# In pass 1 of the loop, arg = $var1
# In pass 2 of the loop, arg = $var2
# In pass 3 of the loop, arg = $var3
# ...
# In pass N of the loop, arg = $varN

# Arguments in [list] quoted to prevent possible word splitting.
```

> The argument list may contain wild cards. If do is on same line as for, there needs to be a semicolon after list.

```bash
for arg in [list] ; do
```

> A variable may supply the [list] in a for loop.

```bash
#!/bin/bash
# fileinfo.sh

FILES="/usr/sbin/accept
/usr/sbin/pwck
/usr/sbin/chroot
/usr/bin/fakefile
/sbin/badblocks
/sbin/ypbind"     # List of files you are curious about.
                  # Threw in a dummy file, /usr/bin/fakefile.

echo

for file in $FILES
do

  if [ ! -e "$file" ]       # Check if file exists.
  then
    echo "$file does not exist."; echo
    continue                # On to next.
   fi

  ls -l $file | awk '{ print $8 "         file size: " $5 }'  # Print 2 fields.
  whatis `basename $file`   # File info.
  # Note that the whatis database needs to have been set up for this to work.
  # To do this, as root run /usr/bin/makewhatis.
  echo
done

exit 0
```

> If the [list] in a for loop contains wild cards (\* and ?) used in filename expansion, then globbing takes place.

```bash
#!/bin/bash

filename="*txt"

for file in $filename
do
 echo "Contents of $file"
 echo "---"
 cat "$file"
 echo
done
```

> Omitting the in [list] part of a for loop causes the loop to operate on $@ -- the positional parameters.

```bash
#!/bin/bash

#  Invoke this script both with and without arguments,
#+ and see what happens.

for a
do
 echo -n "$a "
done

#  The 'in list' missing, therefore the loop operates on '$@'
#+ (command-line argument list, including whitespace).

echo

exit 0
```

_Example: A grep replacement for binary files_

```bash
#!/bin/bash
# bin-grep.sh: Locates matching strings in a binary file.

# A "grep" replacement for binary files.
# Similar effect to "grep -a"

E_BADARGS=65
E_NOFILE=66

if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` search_string filename"
  exit $E_BADARGS
fi

if [ ! -f "$2" ]
then
  echo "File \"$2\" does not exist."
  exit $E_NOFILE
fi


IFS=$'\012'       # Per suggestion of Anton Filippov.
                  # was:  IFS="\n"
for word in $( strings "$2" | grep "$1" )
# The "strings" command lists strings in binary files.
# Output then piped to "grep", which tests for desired string.
do
  echo $word
done

# As S.C. points out, lines 23 - 30 could be replaced with the simpler
#    strings "$2" | grep "$1" | tr -s "$IFS" '[\n*]'


#  Try something like  "./bin-grep.sh mem /bin/ls"
#+ to exercise this script.

exit 0
```

_Example: Listing all users on the system_

```bash
#!/bin/bash
# userlist.sh

PASSWORD_FILE=/etc/passwd
n=1           # User number

for name in $(awk 'BEGIN{FS=":"}{print $1}' < "$PASSWORD_FILE" )
# Field separator = :    ^^^^^^
# Print first field              ^^^^^^^^
# Get input from password file  /etc/passwd  ^^^^^^^^^^^^^^^^^
do
  echo "USER #$n = $name"
  let "n += 1"
done


# USER #1 = root
# USER #2 = bin
# USER #3 = daemon
# ...
# USER #33 = bozo

exit $?

#  Discussion:
#  ----------
#  How is it that an ordinary user, or a script run by same,
#+ can read /etc/passwd? (Hint: Check the /etc/passwd file permissions.)
#  Is this a security hole? Why or why not?
```

### While loops

```bash
while [ condition ]
do
 command(s)...
done

# One liner
while [ condition ] ; do
```

_Example_

```bash
#!/bin/bash

var0=0
LIMIT=10

while [ "$var0" -lt "$LIMIT" ]
#      ^                    ^
# Spaces, because these are "test-brackets" . . .
do
  echo -n "$var0 "        # -n suppresses newline.
  #             ^           Space, to separate printed out numbers.

  var0=`expr $var0 + 1`   # var0=$(($var0+1))  also works.
                          # var0=$((var0 + 1)) also works.
                          # let "var0 += 1"    also works.
done                      # Various other methods also work.

echo

exit 0
```

_Example_

```bash
#!/bin/bash

echo
                               # Equivalent to:
while [ "$var1" != "end" ]     # while test "$var1" != "end"
do
  echo "Input variable #1 (end to exit) "
  read var1                    # Not 'read $var1' (why?).
  echo "variable #1 = $var1"   # Need quotes because of "#" . . .
  # If input is 'end', echoes it here.
  # Does not test for termination condition until top of loop.
  echo
done

exit 0
```

_Example: C-style syntax in a while loop_

```bash
#!/bin/bash
# wh-loopc.sh: Count to 10 in a "while" loop.

LIMIT=10                 # 10 iterations.
a=1

while [ "$a" -le $LIMIT ]
do
  echo -n "$a "
  let "a+=1"
done                     # No surprises, so far.

echo; echo

# +=================================================================+

# Now, we'll repeat with C-like syntax.

((a = 1))      # a=1
# Double parentheses permit space when setting a variable, as in C.

while (( a <= LIMIT ))   #  Double parentheses,
do                       #+ and no "$" preceding variables.
  echo -n "$a "
  ((a += 1))             # let "a+=1"
  # Yes, indeed.
  # Double parentheses permit incrementing a variable with C-like syntax.
done

echo

# C and Java programmers can feel right at home in Bash.

exit 0
```

### Until loops

This construct tests for a condition at the top of a loop, and keeps looping as long as that condition is false (opposite of while loop).

```bash
until [ condition-is-true ]
do
 command(s)...
done

until [ condition-is-true ] ; do
```

_Example_

```bash
#!/bin/bash

END_CONDITION=end

until [ "$var1" = "$END_CONDITION" ]
# Tests condition here, at top of loop.
do
  echo "Input variable #1 "
  echo "($END_CONDITION to exit)"
  read var1
  echo "variable #1 = $var1"
  echo
done

#                     ---                        #

#  As with "for" and "while" loops,
#+ an "until" loop permits C-like test constructs.

LIMIT=10
var=0

until (( var > LIMIT ))
do  # ^^ ^     ^     ^^   No brackets, no $ prefixing variables.
  echo -n "$var "
  (( var++ ))
done    # 0 1 2 3 4 5 6 7 8 9 10


exit 0
```

## case Statement
The Bash case statement takes the following form:
```bash
case EXPRESSION in

  PATTERN_1)
    STATEMENTS
    ;;

  PATTERN_2)
    STATEMENTS
    ;;

  PATTERN_N)
    STATEMENTS
    ;;

  *)
    STATEMENTS
    ;;
esac
```

- Each case statement starts with the case keyword, followed by the case expression and the in keyword. The statement ends with the esac keyword.
- You can use multiple patterns separated by the | operator. The ) operator terminates a pattern list.
- A pattern can have special characters .
- A pattern and its associated commands are known as a clause.
- Each clause must be terminated with ;;.
- The commands corresponding to the first pattern that matches the expression are executed.
- It is a common practice to use the wildcard asterisk symbol (*) as a final pattern to define the default case. This pattern will always match.
- If no pattern is matched, the return status is zero. Otherwise, the return status is the exit status of the executed commands

_Example_
```bash
#!/bin/bash

echo -n "Enter the name of a country: "
read COUNTRY

echo -n "The official language of $COUNTRY is "

case $COUNTRY in

  Lithuania)
    echo -n "Lithuanian"
    ;;

  Romania | Moldova)
    echo -n "Romanian"
    ;;

  Italy | "San Marino" | Switzerland | "Vatican City")
    echo -n "Italian"
    ;;

  *)
    echo -n "unknown"
    ;;
esac

```

## File test operators
For more information, visit [here](https://tldp.org/LDP/abs/html/fto.html)
- File exists(`-e`)
- Regular file and not a directory (-f)
- File is not zero size (-s)
- File is a directory (-d)
- File is a block device (-b)
- File is a character device (-c)
- File is a pipe (-p)
- File is a symbolic link (-h | -L)
- File is a socket
- File is associated with terminal device (-t)
- File has read permission (`-r`)
- File has write permission (`-w`)
- File has execute permission (`-x`)
- Set file group ID(-g)
- Set file user ID(-u)


