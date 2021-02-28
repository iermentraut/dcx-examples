#!/bin/bash
set -e

exec yaml-merge $(find . -type f -regex ".*\.\(yaml\|yml\)" | sort)
