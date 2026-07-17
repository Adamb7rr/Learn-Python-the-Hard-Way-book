from sys import argv

script, user_name = argv
prompt = 'Enter: '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What Kind of computer do you have?")
computer = input(prompt)

print("Do you have brothers?")
brothers = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And you said you %r have brothers.
""" % (likes, lives, computer, brothers))