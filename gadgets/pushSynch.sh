#!/bin/bash

echo " ### >>> synching w/local-repos"
git push

echo " ### >>> synching w/BitBucket..."
git push bitbucket

echo " ### >>> synching w/gitHub..."
git push github
