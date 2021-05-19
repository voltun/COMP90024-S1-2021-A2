#!/bin/bash

# NOTE: Requires access email as argument 1 
# i.e. ./run-nectar.sh <email>

. ./MRC_COMP90024_API.sh $1; ansible-playbook --ask-become-pass -vvv mrc.yaml