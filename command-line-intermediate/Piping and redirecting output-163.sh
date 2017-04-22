## 1. Appending ##

~$ nano beer.txt

## 2. Redirecting from a file ##

~$ sort -r < beer.txt

## 3. The grep command ##

~$ grep "bottles of" beer.txt coffee.txt

## 4. Special characters ##

~$ grep "beer" beer?.txt

## 5. The star wildcard ##

~$ grep "beer" *.txt

## 6. Piping output ##

~$ python script2.py | grep "Hello"

## 7. Chaining commands ##

~$ echo "Added a line" >> beer.txt && cat beer.txt

## 8. Escaping characters ##

~$ echo "Added \" a double quote" >> beer.txt