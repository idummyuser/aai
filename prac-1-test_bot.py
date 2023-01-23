import aiml
import time

print("Name - Pritesh Tayade - Roll No 15")

time.clock = time.time

kernel = aiml.Kernel()
kernel.learn(r"prac-1-std-startup.xml")
kernel.respond("LOAD")

while True:
  print(kernel.respond(input("Enter your message >> ")))
