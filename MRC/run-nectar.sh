#!/bin/bash

# NOTE: Requires access username as argument 1 
# i.e. ./run-nectar.sh <email_username>

. ./MRC_COMP90024_API.sh $1; ansible-playbook --ask-become-pass -i inventory mrc.yaml