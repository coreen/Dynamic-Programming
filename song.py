# program that sings a song, puts repeated lyrics in methods for reduced repetition

def repeat1():
    print("I don't know why she swallowed that fly,");
    print("Perhaps she'll die.")
    print()


def repeat2():
    print("She swallowed the bird to catch the spider,")
    print("She swallowed the spider to catch the fly,")


def repeat3():
    print("She swallowed the dog to catch the cat,")
    print("She swallowed the cat to catch the bird,")


# main
print("There was an old woman who swallowed a fly.")
repeat1()

print("There was an old woman who swallowed a spider,")
print("That wriggled and iggled adn jiggled inside her.")
print("She swallowed the spider to catch the fly,")
repeat1()

print("There was an old woman sho swallowed a bird,")
print("How absurd to swallow a bird.")
repeat2()
repeat1()

print("There was an old woman who swallowed a cat,")
print("Imagine that to swallow a cat.")
print("She swallowed the cat to catch the bird")
repeat2()
repeat1()

print("There was an old woman who swallowed a dog,")
print("What a hog to swallow a dog.")
repeat3()
repeat2()
repeat1()

print("There was an old woman who swallowed a pig,")
print("So then she grew oh-so very very big.")
print("She swallowed the pig to catch the dog,")
repeat3()
repeat2()
repeat1()

print("There was an old woman who swallowed a horse,")
print("She died of course.")
