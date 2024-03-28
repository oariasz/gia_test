# Git Procedures

1. INITIALIZE A LOCAL REPOSITORY

git init
git config --global init.defaultBranch main    // this is to confirm we are using 'main' as our main branch

2. PUBLISH REPOSITORY TO GITHUB

Create a repository in GitHub
git remote add <remote_name> <url>   // use the name of the created repository on GitHub
git push -u origin main              // initial push

3. SYNC MY REPOSITORY COMMITTING ALL THE UPDATES

git add .      // stage the changes
git commit - m "Informative Commit Message"
git push

4. GET THE GIT STATUS

git status

5. VIEW THE GIT COMMIT HISTORY

git log

6. UNLINK MY LOCAL REPOSITORY

git remote -v
git remote <remote_name>

7. CHANGE THE BRANCH TO MAIN (if it was MASTER)

git branch -m master main

8. MERGE THE SPECIFIED BRANCH'S HISTORY INTO THE CURRENT ONE

git merge [branch]