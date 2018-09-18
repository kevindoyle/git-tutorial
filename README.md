# git-tutorial
an intro to git and github. this introduction is more focused on version
control for personal work and less focused on collaborating on shared code
bases.

Help and documentation
------------------------
While learing to use git it may help to have the
[documentation](https://git-scm.com/docs) open in a tab. You can also run 
`git --help` on the command line. Adding `--help` after any git command will
display information about the command. For example, `git init --help`.

Often (always?) the documentation will have more information than you need at
one time. Don't feel like it should all make sense.


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



Find and push that button, or go to [https://github.com/new](https://github.com/new).

On the "Create a new repository" page, fill out the "Respository name" field.
The one referenced in examples here will be called "tutorial-repo". Now push
the button to create the repository.

With that done, you can start working locally to create content for your new
repository.

First create a folder with a file in it. This will simulate existing work that
you want to start storing on GitHub.

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

Now git will be paying attention to the state of files in this directory. Run
`git status` to view the current state of files.

```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	my_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Here `git status` is telling me that I have an untracked file called
`my_file.txt`. Untracked files are files that git is not paying attention to.
They have no stored version history, and will not be sent to GitHub.

I want git to track `my_file.txt`, so I add it

```
$ git add my_file.txt
```

The output of `git status` is different now that `my_file.txt` is tracked:

```
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   my_file.txt
```

Instead of showing me an untracked file, `git status` now displays a change
`new file` that is staged to be committed.

If photography analogies are your thing you can think of staging changes as
setting up a scene, and committing is like taking the picture.

A commit is a record of the respository's state that can be returned to at any
time. Making a commit is done with the command `git commit`

```
$ git commit -m "add a new, empty file to this repo"
[master (root-commit) 2c98290] add a new, empty file to this repo
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 my_file.txt

```

Every commit is made with a message that describes what change has been made
since the last commit, and why the change was made. Here I used `git commit`
with the `-m` flag, which allows me to put a comment in the command line. If
you ran it without the `-m` flag, then git would automatically open up a text
editor for you to type in your commit message. When you quit your editor, the
commit will be saved.

Writing meaningful commit messages is important. After writing code for long
enough there is inevitably going to be a time when you need to answer a
question like _when did I add this code_, _why did I add this code_, _what was
I thinking doing something this way_. Clear, thorough, and granular commits can
make answering those questions much, much easier.

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

Now it is time to push your work to GitHub. This local git repositiory does not
have any information about remote repositories, so you have to configure it.
Run the following command, but replace `kevindoyle` with your own username, and
`tutorial-repo` with the name of the repository you made at the beginning of
this tutorial.

```
$ git remote add origin https://github.com/kevindoyle/tutorial-repo.git
```

This creates a remote named "origin" ("origin" in a commonly used name for the
remote, but you can use any name) which exists at the given URL. To check the
configuration, run

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
Now you have a file stored, let's make changes and save them. Open
`my_file.txt`, change it, and save. Now check the state of the repo.

```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

You can see your change compared to the previously committed version of
`my_file.txt` using `git diff`:

```
$ git diff my_file.txt
```

Now stage the file with `git add`, run `git commit` to commit the change and
see your feshly created commit with `git log`.

Finally, push the change to your remote.

```
$ git push
```

Branches
-----------------------------
Branches allow for divergent commit histories. The default branch is called
`master`. To view a list of branches, and see which one is currently checked
out, run `git branch`.

```
$ git branch
* master
```

Create a new branch

```
$ git branch experiment-1
```

The new branch will now show up in the branch list

```
$ git branch
  experiment-1
* master
```

To checkout the branch, run

```
$ git checkout experiment-1
M	my_file.txt
Switched to branch 'experiment-1'
```

Any commits made to this branch will not show up on master. The act of adding
commits from this branch to master is called a merge. Run

```
$ git merge --help
```

For more details :)

Pulling
-----------------------
Sometimes your local version of a branch doesn't match the remote. This can
happen when someone else is working the same repositiory, or you push your work
from different computers. 

To update your local code, use `git pull`. To make sure you're pulling a
specific branch you can use `git pull origin branch-name`. 

Git will probably complain if you have uncommited local changes when pulling.
You may also run into something called a merge conflict.

Merge conflicts happen when git tries to combine two different versions of code
that each change the same lines of code. When git can't decide which version to
use, it declares a merge conflict and asks you to make the decision for it.

Here's one guide for resolving merge conflicts: https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/

I'm sure there are many other, possibly better, guides out there. Feel free to
contact me or anyone else familiar with git if you get stuck in a merge
conflict. They are a familiar pain point for all git users.


Revisit old versions
------------------------------
Get the commit hash
```
$ git log
```
Then checkout that hash
```
$ git checkout 1a2b3c4d
```
When you are done with the old version, return to the current state of your
code by checking out a branch. For example,
```
$ git checkout master
```


Releases
----------------------------
Releases can be used to identify important moments in a codebase's history and
make that state of the code easy to access.

For example, a release could be tagged whenever the current code state is used
to generate results that are submitted to a journal. Then, reproducing the
result could be as simple as downloading the .zip file with that version of the
code.


An exercise
--------------------------------
Clone this repository: https://github.com/kevindoyle/git-tutorial
```
$ cd ~/repos/
$ git clone https://github.com/kevindoyle/git-tutorial.git
$ cd git-tutorial
```

The respository contains a script called `street_crossing.py`. Look the the
script's doc string to see what it does and how to run it.

Checkout a new branch for your commits. This command is shorthand for creating
a new branch and checking it out in one step:

```
$ git checkout -b your-name-exercise-solution
```

Rewrite the code in `street_crossing.py` so that it matches the template
started in `exercise_stub.py`. Make incremental changes in `street_crossing.py`
and commit each step along the way. (Tip: The first step might be to simply
copy [this code](https://github.com/kevindoyle/git-tutorial/blob/e70a7c46a0032f4d33e7accd8c76e3b72d19ef55/exercise_stub.py#L15-L22) from `exercise_stub.py` into `street_crossing.py`)

Notice that you can take a working model, such as `street_crossing.py`, and
work on it, possibly breaking it at times, without worrying about losing the
working version of the code 😁

Push your branch to the repository and open a pull request against the existing
branch called `merge-exercises-into-this-branch`.

If you get stuck, my solution is on the branch
`kevins-refactor-exercise-solution`. You can view the commits [here](https://github.com/kevindoyle/git-tutorial/commits/kevins-refactor-exercise-solution).


Misc resources
------------------------

- ["a fairly comprehensive guide to recovering from what you did not mean to do when using git"](http://sethrobertson.github.io/GitFixUm/fixup.html)
- ["write down a command-line to see the help text that matches each argument"](https://explainshell.com/)
- ["how to write a git commit message"](https://chris.beams.io/posts/git-commit/)

Credits
------------------------------------
Some segments of this document were copied from https://github.com/TuftsBCB/git-tutorial
