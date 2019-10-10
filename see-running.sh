#!/usr/bin/env bash
screen -ls
LIST=$(screen -ls | grep mc-)
echo $LIST
