# GitTest
Team 1418's github test. Team 1418 is currently introducing their new members to git through codecademy. This is designed in order to prove that new members have a working knowledge of git syntax. Each member will complete this test in front of a leader.

# The Challenges

### Cloning this repository

- Clone this repository
- `cd` into the cloned repo
- Update the repository with `git pull` (it will already be updated)
- Use the command `git status` to make sure you are on the `master` branch
- Use the command `git log` to view the commit history

### Merge Conflicts

- Merge the branch called `alpha` into the `master` branch
- Fix the merge conflicts in `text.txt` by taking the changes from `alpha` and discarding those in `master`
- Fix the merge conflicts in `robo.py` by keeping both changes
- Create a new commit with the merged files

### Commiting files

- Create a new file called `happy.txt`
- Write out `Happy birthday to you` on the first line and save the file
- Add the file to git tracking
- Make a commit with a good message including that file creation

### Branching

- Create a new branch called `beta`
- Edit `text.txt` to add your name and date at the bottom of the file.
- Add the `text.txt` changes to the staging area
- Make a commit with a good message that includes that file


### Forking with GitHub

- Create a fork of this repository on your github account
- Add your fork as a `git remote` named `me`
- Checkout the branch you edited called `beta`
- Push your changes of `text.txt` to your fork of this repo on the `beta`branch

### Pull requests

- Create a GitHub pull request from the branch `beta` on **your fork** to `master` on the **main repo** on Team 1418's GitHub

### Reseting

- Checkout the `master` branch
- Use the command `git reset` to reset to the commit before the first challenge task
- The first commit in the log should then be `Changed bravo to beta`
