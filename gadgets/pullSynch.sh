#!/bin/bash

echo " ### >>> synching w/local-repos"
git pull

echo " ### >>> synching w/BitBucket..."
git pull bitbucket

echo " ### >>> synching w/gitHub..."
git pull github
