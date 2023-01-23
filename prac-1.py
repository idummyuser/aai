import aiml
import time

print("Name - Pritesh Tayade - Roll No 15")

time.clock = time.time

kernel = aiml.Kernel()
kernel.learn(r"C:\Workspace\un-org\MScIT\Part-II-2022-23\Sem-3\Applied-Artificial-Intelligence\pracs\Pritesh\AIPracsProject\prac-1-std-startup.xml")
kernel.respond("LOAD")

while True:
  print(kernel.respond(input("Enter your message >> ")))
