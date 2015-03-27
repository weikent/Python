#!/bin/sh

echo $1


for i in {1..8};do
    aaa=ping$1" "$i
    `$aaa`
    echo $aaa
done;
