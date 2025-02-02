@echo off
git reset --hard
git checkout master
git pull
cls
echo --------------------------
echo Pulled latest master
echo --------------------------
git status