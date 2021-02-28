#!/usr/bin/env python
import glob
from dotenv import dotenv_values

temp_file = open("/home/docker/.env", "wb")

files = glob.glob("/app/env/**/*.env", recursive=True)

for f in files:
  with open(f, "rb") as infile:
    temp_file.write(infile.read())

temp_file.close()

env_file = open("/app/.env", "w")

envs = dotenv_values(dotenv_path='/home/docker/.env')

for key, value in envs.items():
  env_file.write(key + "=" + value + "\n")

env_file.close()
