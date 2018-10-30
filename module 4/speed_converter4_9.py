# speed_converter4_9
# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.
# Start speed =60
# End speed=131
# increments = 10
# MPH=KPH * 0.6214

def main():
    # print the table headings.
    print('KPH\tMPH')
    print('----------------')


    # print the speed for kph in range.
    for KPH in range(60,131,10):
        MPH=KPH*0.6214
        print(KPH,'\t',format(MPH,'.1f'))

main()
        
