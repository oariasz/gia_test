# Git Procedures

* See video: https://www.youtube.com/watch?v=tRZGeaHPoaw

1. INITIALIZE A LOCAL REPOSITORY

git init
git config --global init.defaultBranch main    // this is to confirm we are using 'main' as our main branch

2. PUBLISH REPOSITORY TO GITHUB

Create a repository in GitHub        // https://github.com/oariasz/gia_test
git remote add origin <url>          // use the name of the created repository on GitHub
git branch -M main
git pull --rebase origin main        // WARNING: just in case a README file was created on the web
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

9. CHECK THE AVAILABLE BRANCHES

git branch -l

10. RESTORE A FILE FROM A PREVIOUS COMMIT

// This method completely replaces the current version of the file in your working directory with the version from the desired commit
git checkout <commit_hash> -- <file_path>    

// Commit hash can be found using:
git log