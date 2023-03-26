## **5. Troubleshooting**

1. [When I open Windows Explorer through Ubuntu, it goes to a different folder than in the guide](#1-When-I-open-Windows-Explorer-through-Ubuntu,-it-goes-to-a-different-folder-than-in-the-guide)
1. [Ubuntu on Windows 10 high CPU usage, crashes](#2-ubuntu-on-windows-10-high-cpu-usage,-crashes)
1. [When I pull from the `ds prep course-2023` repository, I get an error](#3-When-I-pull-from-the-ds-prep-course-2023-repository,-I-get-an-error)
1. [When I try to open `jupyter notebook`, I get an error](#4-When-I-try-to-open-jupyter-notebook,-I-get-an-error)
1. [When I use the `cp` command the `>` sign appears and the command does not execute](#5-When-I-use-the-`cp`-command-the->-sign-appears-and-the-command-does-not-execute)
1. [When setting up python 3.8 I get an error](#6-When-setting-up-python-3.8-I-get-an-error)
1. [Nothing happens when I type my password](#7-Nothing-happens-when-I-type-my-password)
1. [I still have a NotImplemented error](#8-I-still-have-a-NotImplemented-error)

#### _**1. When I open Windows Explorer through Ubuntu, it goes to a different folder than in the guide**_

Please make sure:

- you are running the command `explorer.exe .` including the dot at the end.
- you are running Windows 10 version `1909` or newer.

#### _**2. Ubuntu on Windows 10 high CPU usage, crashes**_

- Make sure you are running Windows 10 version `1909` or newer.
- Then, try following [these steps](https://teckangaroo.com/enable-windows-10-virtual-machine-platform/)

#### ___3. When I pull from the `ds-prep-course-2023` repository, I get an error___

If you get an error like the following when pulling:

```
error: Your local changes to the following files would be overwritten by merge:
<some files>
Please commit your changes or stash them before you merge.
Aborting
```

what _git_ is telling you is that changes were made by you to the files on the `~/projects/ds-prep-course-2023` folder, and is not pulling the changes made by the instructors because they would override the changes that you made there.

To fix this do the following:

1. Make sure that any change you made to the files on `~/projects/ds-prep-course-2023`  (that you don't want to lose) is saved in your `~/projects/ds-prep-workspace` repository (refer to [Updates to Learning Units](#3-updates-to-learning-units) on how to do this), and if you don't want to keep the changes you made to these files, just continue on to the next step;
2. Go to the `~/projects/ds-prep-course-2023` folder and run:

    ```bash
    cd ~/projects/ds-prep-course-2023
    git stash
    ```

3. Now you can pull from the `ds-prep-course-2023` repository:

    ```bash
    git pull
    ```

#### ___4. When I try to open `jupyter notebook`, I get an error___

If you get this error when trying to open a notebook:

```bash
migs-MBP% jupyter notebook
zsh: command not found: jupyter
```

make sure to activate your virtual environment **before** opening `jupyter notebook`:

```bash
source ~/.virtualenvs/prep-venv/bin/activate
```

#### ___5. When I use the `cp` command the `>` sign appears and the command does not execute___

```bash
cp -r ~/projects/ds-prep-course-2023/“Week 00" ds-prep-workspace
>
```

Make sure to use this type of quotes `"` and not these ones `“`.

#### _**6. When setting up python 3.8 I get an error**_

When I run this command:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

I get this error:

```bash
W: GPG error: http://apt.postgresql.org/pub/repos/apt focal-pgdg InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 7FCC7D46ACCC4CF8
```

Solution: Take the id in front of `NO_PUBKEY` (in my case its `7FCC7D46ACCC4CF8`) and run the following command:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCC7D46ACCC4CF8
```

#### _**7. Nothing happens when I type my password**_

In **step two** it asks me for the computer password. However, I am not being able to write anything

Solution:
When you write your password you might not get any visual feedback and that's okay! Write it as normal and hit <kbd>enter</kbd> when you're done!

#### _**8. I still have a NotImplemented error**_

I've completed the exercise in the Exercise Notebook but when I run the cell I get a **NotImplementedError**.

Solution:
The `raise NotImplementedError()` are added to the exercise cell as a placeholder for where you're supposed to add your solution/code. It is meant to be removed!

<br>

## **6. Tips and Tricks**

Coming soon.

<br>

## **7. Tutorial videos from Prep Course 2020

🎁🎬 Check the **tutorial videos** if you have any doubts after following this tutorial. These videos were made for the **Prep Course of year 2020**, so there may be some differences.

- [Setup guide for Windows - Part 1](https://www.youtube.com/watch?v=fWi3bYoHW18)
- [Setup guide for Windows - Part 2](https://www.youtube.com/watch?v=bnJOQHh9pJ4)
- [Setup guide for Mac](https://www.youtube.com/watch?v=qs0z4ibMFdU)
- [Updates to Learning Units guide for Windows 10](https://www.youtube.com/watch?v=Q2Cezm6ufrE)
- [Updates to Learning Units guide for Mac](https://www.youtube.com/watch?v=-fzIDfNBZ0I)
