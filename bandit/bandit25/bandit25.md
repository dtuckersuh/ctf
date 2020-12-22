# Bandit 25 -> 26

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

- Helpful commands
    - ssh, cat, more, vi, ls, id, pwd

- Given a private key to ssh into bandit26 but connection immediately closed
- If ssh executed with "-t" or "-T" command and any subsequent command there is no terminal output
    - Intended?
    - -T: Disables pseudo-terminal allocation
    - -t: Force pseudo-terminal allocation. Used to execute arbitrary screen-based programs
- Unable to execute commands
    - ssh -i bandit26.sshkey -t bandit26@localhost "ls -la"
    - ... "cd /bin; ls -la"

- Created bash script to direct input into ssh command
    - ssh ... 'bash -s' < /tmp/boogaloo26/exec.sh

- Script does not seem to execute, but /home/bandit26/text.txt is displayed in terminal

## Solution

'''bash
cat /etc/passwd | grep bandit26
'''

- Reveals /usr/bin/showtext file that is a script

'''bash
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
'''

- Script calls more to show the bandit26 ASCII art then exits
- Resizing the terminal on ssh login will cause `more` to give us an
  exploitation entry
- Use vim commands to edit /etc/bandit\_pass/bandit26 to see password
- `set shell=/bin/bash`
- Execute shell command in vim to get a shell
