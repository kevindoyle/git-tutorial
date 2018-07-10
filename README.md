# git-tutorial
an intro to git and github

Your first time with git
------------------------
If you've never used `git` before, then make sure it's installed and run the
following commands so that your name and email will show up with your commits:

```
$ git config --global user.name "Full Name"
$ git config --global user.email "You@Domain.com"
```

Setup and first steps
------------------------

To start, let's create a new repository on GitHub. When I'm logged in and go to https://www.github.com, I see a "New respository" button like this one: 


![new-repository-button](https://user-images.githubusercontent.com/7545321/42487005-ef88b4de-83cc-11e8-9c10-f968233fd22a.png)



Find and push that button, or go to (https://github.com/new)[https://github.com/new].

On the "Create a new repository" page, fill out the "Respository name" field. The one referenced in examples here will be called "tutorial-repo". Now push the button to create the repository. 

With that done, you can start working locally to create content for your new repository.

First create a folder with a file in it. This will simulate existing work that you want to start storing on GitHub.

```
$ mkdir -p ~/repos/tutorial-repo
$ cd ~/repos/tutorial-repo
$ echo "this is my file" > my_file.txt
```

Next tell git to create a new repository in the current directory. Run

```
$ git init
Reinitialized existing Git repository in /home/kevin/repos/tutorial-repo/.git/
```

Now git will be paying attention to the state of files in this directory. Run `git status` to view the current state of files.

```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	new_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Here `git status` is telling me that I have an untracked file called `new_file.txt`. Untracked files are files that git is not paying attention to. They have no stored version history, and will not be sent to GitHub. 

I want git to track `new_file.txt`, so I add it

```
git add new_file.txt
```

The output of `git status` is different now that `new_file.txt` is tracked:

```
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   new_file.txt
```

Instead of showing me an untracked file, `git status` now displays a change `new file` that is staged to be committed.

If photography analogies are your thing you can think of staging changes as setting up a scene, and committing is like taking the picture. 

A commit is a record of the respository's that can be returned to at any time. Making a commit is done with the command `git commit`

```
$ git commit -m "add a new, empty file to this repo"
[master (root-commit) 2c98290] add a new, empty file to this repo
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 new_file.txt

```

Every commit is made with a message that describes what change has been made since the last commit, and why the change was made. Here I used `git commit` with the `-m` flag, which allows me to put a comment in the command line. If you ran it without the `-m` flag, then git would automatically open up a text editor for you to type in your commit message. When you quit your editor, the commit will be saved.

Writing meaningful commit messages is important. After writing code for long enough there is inevitably going to be a time when you need to answer a question like _when did I add this code_, _why did I add this code_, _what was I thinking doing something this way_. Clear, thorough, and granular commits can make answering those questions much, much easier. 

After committing, running `git status` shows an upated state for the repo

```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

You can use `git log` to see a record of your commits

```
$ git log
commit 2c982906e3ed752ef5e7aa1276ca636355b782b8 (HEAD -> master, origin/master)
Author: Kevin Doyle <kjohndoyle@gmail.com>
Date:   Mon Jul 9 22:51:47 2018 -0400

    add a new, empty file to this repo
```

Now it is time to push your work to GitHub. This local git repositiory does not have any information about remote repositories, so you have to configure it. Run the following command, but replace `kevindoyle` with your own username, and `tutorial-repo` with the name of the repository you made at the beginning of this tutorial.

```
git remote add origin https://github.com/kevindoyle/tutorial-repo.git
```

This creates a remote named "origin" ("origin" in a commonly used name for the remote, but you can use any name) which exists at the given URL. To check the configuration, run 

```
$ git remote -v
origin	git@github.com:kevindoyle/tutorial-repo.git (fetch)
origin	git@github.com:kevindoyle/tutorial-repo.git (push)
```

Push the commit to GitHub now that everything is setup

```
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 882 bytes | 882.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:kevindoyle/tutorial-repo.git
 * [new branch]      master -> master
```

If you visit your repository on GitHub now, the file will be there.

Making changes
----------------------
Now you have a file stored, let's make changes and save them. Open `new_file.txt`, change it, and save. Now check the state of the repo.

```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   new_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

You can see your change compared to the previously committed version of `new_file.txt` using `git diff`:

```
$ git diff new_file.txt
```

Now stage the file with `git add`, run `git commit` to commit the change and see your feshly created commit with `git log`.

Finally, push the change to your remote.

```
git push
```


Some segments of this document were copied from https://github.com/TuftsBCB/git-tutorial
