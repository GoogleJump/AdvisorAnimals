def helloWorld():
  print "I'm just going to leave this right here."

for i in range(5):
  helloWorld()
print listBuilder()

def listBuilder():
  b = []
  for x in range(5):
    b.append(10 * x)
  return b

print "[done]"
