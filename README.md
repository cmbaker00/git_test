"# git_test" 

## Some Basic Git Commands
# Creating a repo
* Local repo:
git init
* Downloading a repo:
git clone <url> .

# Version control 
* Check which files have been changed
git status
* Check what the changes are
git diff
* Stage all altered files
git add .
* Commit changes
git commit -m "<comments>"

# Sending changes to github
* Always pull first to check you have the most most updated version
git pull origin master
* Push changes
git push origin master

# Branching code
* Get current branches
git branch
* Create a branch
git branch <name>
* Switch to a branch
git checkout <name>
* Pushing new branch to github
git push -u origin <name>
* Merging changes into master
get checkout master
git pull origin master
git branch --merged
git merge <name>
git push origin master
* Delete a branch locally
git branch -d <name>
* Delete a branch on github
git push origin --delete test
