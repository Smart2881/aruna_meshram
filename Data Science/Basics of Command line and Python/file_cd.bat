@echo off

REM This file lets you create three new folders, sub-folders and remove two of them

mkdir sun sea sand
dir
cd sea

mkdir pebbles seagull fish
dir

rmdir pebbles seagull
dir

cd..