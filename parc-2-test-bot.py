import aiml
import time

time.clock = time.time

kernel = aiml.Kernel()
kernel.learn("C:\Workspace\un-org\MScIT\Part-II-2022-23\Sem-3\Applied-Artificial-Intelligence\pracs\Pritesh\AIPracsProject\prac-2-std-startup.xml")
kernel.respond("LOAD")

while True:
  print(kernel.respond(input("Enter your message >> ")))

