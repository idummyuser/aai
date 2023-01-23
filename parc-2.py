#Design a bot using AIML.

import aiml
import time

time.clock = time.time

kernel = aiml.Kernel()
kernel.learn("prac-2-std-startup.xml")
kernel.respond("LOAD")

while True:
  print(kernel.respond(input("Enter your message >> ")))

