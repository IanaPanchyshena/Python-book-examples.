# The following code opens file and appends additional data
# to its existing contents.

def main():
    myfile=open('friends.txt','a')
    myfile.write('Matt\n')
    myfile.write('Chris\n')
    myfile.write('Suze\n')
    myfile.close()


main()
