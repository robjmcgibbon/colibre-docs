#!/bin/bash -e

# Generate html docs
make clean
make html

# Package into a .war file
# Only necessary for deploying to the same server as the data access API.
cd maven && mvn clean package
