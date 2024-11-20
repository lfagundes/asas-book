#!/bin/bash

cat main.tex | gpg --armor --symmetric --output main.tex.gpg 
