# NATAS Writeups

## Level 4

- Access only allowed from the level 5 webpage
- Use Burp Suite to change request referer to correct user

## Level 8

- PHP Source code
- Encoded secret = bin2hex(strrev(base64\_encode(secret)))

## Level 9

- Needle in a haystack
- passthru function: execute an external program and display raw output
    - similar to exec()
    - Exploit this to gain code execution?
    - grep -i $key dictionary.txt
- grep -i needles dictionary.txt; cat dictionary.txt
- We have code execution but how can we obtain flag?
- Use ls -la to find hidden files
- needles dictionary.txt; cat .htpasswd; grep -i needles
    - outputs three different passwords
    - $1$p1kwO0uc$UgW30vjmwt4x31BP1pWsV.
    - $1$H1h4/vhv$sGSIWyboB82roKx9lNLlE/
    - $1$G56GGLB5$XS1TpsdfDa8t4tvOx.V660
- None of these are correct
- cat /etc/natas\_pass/natas10 
    - Obvious solution how did I forget

## Level 10

- Sanitize input
    - preg\_match()
        - Performs regex match
        - /[;|&]/
        - No obvious command line operations
- Transformation method
    - XOR two strings to get character blocked by regex
- **grep can search multiple files**
    - input: <query> /etc/natas\_webpass/natas11

## Level 11

- Topics
    - XOR encryption
    - Cookies
    - User input
- Source code
    - Functions
        - xorEncrypt($in)
        - loadData($def)
        - saveData($d)
    - We need $data["showpassword"] == "yes"
        - setcookie("data", base64\_encode(xor_encrypt(json_encode($d))))
    - $defaultData -> loadData -> $mydata
- Modify the cookie to set showpassword to yes
- We don't know key to xorEncrypt
- XOR is two-way so we (output ^ input) should equal key
