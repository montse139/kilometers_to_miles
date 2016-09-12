print "Convert kilometers to miles!"

while True:
    kilometers = int(raw_input("Number of kilometers to convert: "))
    print (kilometers * 0.621371)

    convert = raw_input("Do you want to convert something else? (answer Y or N): ")

    if convert != "Y":
        print "Thanks for using me!"
        break
#kilometers_to_miles
