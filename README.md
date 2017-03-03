# Clickjacking Tester

A python script designed to check if the website is vulnerable of clickjacking and creates a poc.

### Screenshot
![alt img](https://github.com/nig/Clickjacking-Tester/blob/master/ss.PNG)

### Usage

```
python(3) clickjacking_tester.py <file_name>
```

### Example

##### Input

```
python clickjacking_tester.py sites.txt
```

##### sites.txt

```
www.google.com
www.turkhackteam.com
```

##### Output

```
[*] Checking www.google.com

 [-] Website is not vulnerable!

[*] Checking www.turkhackteam.org

 [+] Website is vulnerable!
 [*] Created a poc and saved to <URL>.html
```
