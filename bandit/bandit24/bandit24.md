# Bandit 24 -> 25

A daemon is listening on port 30002 and will give you the password for bandit25
if given the password for bandit24 and a secret numeric 4-digit pincode. There
is no way to retrieve the pincode except by going through all of the 1000
combinations, called brute-forcing

- Would it be easier to use bash or python script?

## Bash Script Approach
- Need to create a script to brute force all possible pincodes
    - UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ  [4-digit pincode]
- How to brute force 4-digit pincode?
    - 0000, 0001, ..., 9837, ..., 9999

```bash
#!/bin/bash

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

nc 127.0.0.1 30002

for ((i = 0; i < 1048576; i++)); do
    
done
```
