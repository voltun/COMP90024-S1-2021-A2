#!/bin/bash

# NOTE: Requires access email as argument i.e. ./run-nectar.sh <email>

. ./MRC_COMP90024_API.sh $1; ansible-playbook mrc.yaml