## 1. Introduction to Version Control Systems ##

~/random_numbers$ git status

## 2. The .git Folder ##

~/random_numbers$ ls -al

## 3. Creating Files in the Repository ##

~/random_numbers$ nano script.py

## 4. Checking File Status ##

~/random_numbers$ git add README.md

## 5. Configuring Identity in Git ##

~/random_numbers$ git config --global user.name "kcthogiti"

## 6. Committing Changes ##

~/random_numbers$ git commit -m "Intial commit. Added script.py and README.md"

## 7. Viewing File Differences ##

~/random_numbers$ git status

## 8. Making a Second Commit ##

~/random_numbers$ git commit -m "displays random numbers"

## 9. Reviewing the Commit History ##

~/random_numbers$ git log

## 10. Viewing Commit Differences ##

~/random_numbers$ git log --stat