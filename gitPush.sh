#!/bin/bash
IFS='
'

for tbl in $(git remote show origin); do    
  if [[ "$tbl" == *"pushes to"* ]]; then
    branchName=$(echo "$tbl" | awk '{print $1}')
    echo "Pushing branch: $branchName"
    echo $(git push origin $branchName)
  fi
done
