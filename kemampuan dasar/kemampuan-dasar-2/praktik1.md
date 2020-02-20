asus@DESKTOP-98O1J1U MINGW64 /i/praktik1
$ mkdir rhymes

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1
$ cd rhymes

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes
$ git init
Initialized empty Git repository in I:/praktik1/rhymes/.git/

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ touch README.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git add README.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git commit -m 'First commit.'
[master (root-commit) 98abf2d] First commit.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.txt

no changes added to commit (use "git add" and/or "git commit -a")

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git diff
warning: LF will be replaced by CRLF in README.txt.
The file will have its original line endings in your working directory
diff --git a/README.txt b/README.txt
index e69de29..c83e022 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.
asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git add README.txt
warning: LF will be replaced by CRLF in README.txt.
The file will have its original line endings in your working directory

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git commit -m 'Added project overview to README.txt'
[master 3e9025d] Added project overview to README.txt
 1 file changed, 1 insertion(+)

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git add all-around-the-mulberry-bush.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   all-around-the-mulberry-bush.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        hickory-dickory-dock.txt
        hokey-pokey.txt
        jack-and-jill.txt
        old-mother-hubbard.txt
        roses-are-red.txt
        twinkle-twinkle.txt


asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git commit -m 'Added all-around-the-mulberry-bush.txt.'
[master 3106a51] Added all-around-the-mulberry-bush.txt.
 1 file changed, 19 insertions(+)
 create mode 100644 all-around-the-mulberry-bush.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git add jack-and-jill.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git commit -m 'Added jack-and-jill.txt.'
[master 40eabf7] Added jack-and-jill.txt.
 1 file changed, 12 insertions(+)
 create mode 100644 jack-and-jill.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git add .

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git commit -m 'Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt'
[master 28c5bbd] Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt
 5 files changed, 69 insertions(+)
 create mode 100644 hickory-dickory-dock.txt
 create mode 100644 hokey-pokey.txt
 create mode 100644 old-mother-hubbard.txt
 create mode 100644 roses-are-red.txt
 create mode 100644 twinkle-twinkle.txt

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git log
commit 28c5bbdd4e1fa9f29650f88e3a628af513885b9a (HEAD -> master)
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:02:46 2020 +1400

    Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt

commit 40eabf75f375c76875dd9dc3574ddacb7cd3e2d1
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:02:11 2020 +1400

    Added jack-and-jill.txt.

commit 3106a51fcad27927e679091c8c938e4673cfb220
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:01:52 2020 +1400

    Added all-around-the-mulberry-bush.txt.

commit 3e9025dc520088225509d46f17d5563d8f16c115
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:00:15 2020 +1400

    Added project overview to README.txt

commit 98abf2df921682da4c378785e2dca15bc1ab8c06
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 16:58:59 2020 +1400

    First commit.
asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git log --oneline
28c5bbd (HEAD -> master) Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt
40eabf7 Added jack-and-jill.txt.
3106a51 Added all-around-the-mulberry-bush.txt.
3e9025d Added project overview to README.txt
98abf2d First commit.

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git log -p
commit 28c5bbdd4e1fa9f29650f88e3a628af513885b9a (HEAD -> master)
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:02:46 2020 +1400

    Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt

diff --git a/hickory-dickory-dock.txt b/hickory-dickory-dock.txt
new file mode 100644
index 0000000..a337f4c
--- /dev/null
+++ b/hickory-dickory-dock.txt
@@ -0,0 +1,5 @@
+Hickory, dickory, dock,
+The mouse ran up the clock.
+The clock struck one,
+The mouse ran down!
+Hickory, dickory, dock.
diff --git a/hokey-pokey.txt b/hokey-pokey.txt
new file mode 100644
index 0000000..97f425b
--- /dev/null
+++ b/hokey-pokey.txt
@@ -0,0 +1,16 @@
+You put your right foot in,
+You put your right foot out;
+You put your right foot in,
+And you shake it all about.
+You do the Hokey-Pokey,
+And you turn yourself around.
+That's what it's all about!
+
+You put your left foot in...
+You put your right hand in...
+You put your right side in...
+You put your nose in...
+You put your tail in...
+You put your head in...
+You put your whole self in...
+
diff --git a/old-mother-hubbard.txt b/old-mother-hubbard.txt
new file mode 100644
index 0000000..c91ff71
--- /dev/null
+++ b/old-mother-hubbard.txt
@@ -0,0 +1,34 @@
+Old Mother Hubbard
+Went to the cupboard
+To fetch her poor dog a bone;
+But when she came there
+The cupboard was bare,
+And so the poor dog had none.
+She took a clean dish
+To get him some tripe;
+But when she came back
+He was smoking a pipe.
+She went to the grocer's
+To buy him some fruit;
+But when she came back
+He was playing the flute.
+
+She went to the baker's
+To buy him some bread;
+But when she came back
+The poor dog was dead.
+
+She went to the undertaker's
+To buy him a coffin;
+But when she came back
+The poor dog was laughing.
+
+She went to the hatter's
+To buy him a hat;
+But when she came back
+He was feeding the cat.
+
+The dame made a curtsey,
+The dog made a bow;
+The dame said, "Your servant."
+The dog said, "Bow wow!"
diff --git a/roses-are-red.txt b/roses-are-red.txt
new file mode 100644
index 0000000..efba165
--- /dev/null
+++ b/roses-are-red.txt
@@ -0,0 +1,8 @@
+Roses are red
+-------------
+
+Roses are red
+Violets are blue
+Nobody loves GitHub
+More than government agencies do!
+
diff --git a/twinkle-twinkle.txt b/twinkle-twinkle.txt
new file mode 100644
index 0000000..5585462
--- /dev/null
+++ b/twinkle-twinkle.txt
@@ -0,0 +1,6 @@
+Twinkle, twinkle, little star,
+How I wonder what you are.
+Up above the world so high,
+Like a diamond in the sky.
+Twinkle, twinkle, little star,
+How I wonder what you are.

commit 40eabf75f375c76875dd9dc3574ddacb7cd3e2d1
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:02:11 2020 +1400

    Added jack-and-jill.txt.

diff --git a/jack-and-jill.txt b/jack-and-jill.txt
new file mode 100644
index 0000000..1596bce
--- /dev/null
+++ b/jack-and-jill.txt
@@ -0,0 +1,12 @@
+Jack and Jill
+Went up the hill
+To fetch a pail of water.
+Jack fell down
+And broke his crown
+And Jill came tumbling after.
+Up Jack got
+And home did trot
+As fast as he could caper
+Went to bed
+And plastered his head
+With vinegar and brown paper.

commit 3106a51fcad27927e679091c8c938e4673cfb220
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:01:52 2020 +1400

    Added all-around-the-mulberry-bush.txt.



    Added all-around-the-mulberry-bush.txt.

diff --git a/all-around-the-mulberry-bush.txt b/all-around-the-mulberry-bush.txt
new file mode 100644
index 0000000..b77d989
--- /dev/null
+++ b/all-around-the-mulberry-bush.txt
@@ -0,0 +1,19 @@
+All around the mulberry bush
+The monkey chased the weasel.
+The monkey thought 'twas all in fun.
+Pop! goes the weasel.
+
+A penny for a spool of thread,
+A penny for a needle.
+That's the way the money goes.
+Pop! goes the weasel.
+
+Up and down the City Road,
+In and out of the Eagle,
+That's the way the money goes.
+Pop! goes the weasel.
+
+Half a pound of tuppenney rice,
+Half a pound of treacle,
+Mix it up and make it nice,
+Pop! goes the weasel.

commit 3e9025dc520088225509d46f17d5563d8f16c115
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:00:15 2020 +1400

    Added project overview to README.txt

diff --git a/README.txt b/README.txt
index e69de29..c83e022 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.

commit 98abf2df921682da4c378785e2dca15bc1ab8c06
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 16:58:59 2020 +1400

    First commit.

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..e69de29
 ESCOC
/all-around-the-mulberry-bush.txt


























.ac.id>









ry rhymes.


.ac.id>







 ESCOD

    Added all-around-the-mulberry-bush.txt.

diff --git a/all-around-the-mulberry-bush.txt b/all-around-the-mulberry-bush.txt
new file mode 100644
index 0000000..b77d989
--- /dev/null
+++ b/all-around-the-mulberry-bush.txt
@@ -0,0 +1,19 @@
+All around the mulberry bush
+The monkey chased the weasel.
+The monkey thought 'twas all in fun.
+Pop! goes the weasel.
+
+A penny for a spool of thread,
+A penny for a needle.
+That's the way the money goes.
+Pop! goes the weasel.
+
+Up and down the City Road,
+In and out of the Eagle,
+That's the way the money goes.
+Pop! goes the weasel.
+
+Half a pound of tuppenney rice,
+Half a pound of treacle,
+Mix it up and make it nice,
+Pop! goes the weasel.

commit 3e9025dc520088225509d46f17d5563d8f16c115
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:00:15 2020 +1400

    Added project overview to README.txt

diff --git a/README.txt b/README.txt
index e69de29..c83e022 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.

commit 98abf2df921682da4c378785e2dca15bc1ab8c06
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 16:58:59 2020 +1400

    First commit.

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..e69de29
(END)
asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)

commit 28c5bbdd4e1fa9f29650f88e3a628af513885b9a (HEAD -> master)
Author: cintiakus <cintia1700016127@webmail.uad.ac.id>
Date:   Thu Feb 20 17:02:46 2020 +1400

    Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt

diff --git a/hickory-dickory-dock.txt b/hickory-dickory-dock.txt
new file mode 100644
index 0000000..a337f4c
--- /dev/null
+++ b/hickory-dickory-dock.txt
@@ -0,0 +1,5 @@
+Hickory, dickory, dock,
+The mouse ran up the clock.
+The clock struck one,
+The mouse ran down!
+Hickory, dickory, dock.
diff --git a/hokey-pokey.txt b/hokey-pokey.txt
new file mode 100644
index 0000000..97f425b
--- /dev/null
+++ b/hokey-pokey.txt
@@ -0,0 +1,16 @@
+You put your right foot in,
+You put your right foot out;
+You put your right foot in,
+And you shake it all about.
+You do the Hokey-Pokey,
+And you turn yourself around.
+That's what it's all about!
+
+You put your left foot in...
+You put your right hand in...
+You put your right side in...
+You put your nose in...
+You put your tail in...
+You put your head in...
+You put your whole self in...
+
diff --git a/old-mother-hubbard.txt b/old-mother-hubbard.txt
new file mode 100644
index 0000000..c91ff71
--- /dev/null
+++ b/old-mother-hubbard.txt
@@ -0,0 +1,34 @@
+Old Mother Hubbard
+Went to the cupboard
+To fetch her poor dog a bone;
28c5bbd (HEAD -> master) Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt
40eabf7 Added jack-and-jill.txt.
3106a51 Added all-around-the-mulberry-bush.txt.
3e9025d Added project overview to README.txt
98abf2d First commit.
asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git remote add origin https://github.com/sekarnurhidayah99/kemampuan-dasar-2.git

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git push -u origin master
To https://github.com/sekarnurhidayah99/kemampuan-dasar-2.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/sekarnurhidayah99/kemampuan-dasar-2.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

asus@DESKTOP-98O1J1U MINGW64 /i/praktik1/rhymes (master)
$ git push --force origin master
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 4 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (19/19), 2.50 KiB | 183.00 KiB/s, done.
Total 19 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/sekarnurhidayah99/kemampuan-dasar-2.git
 + 24d6eeb...28c5bbd master -> master (forced update)
