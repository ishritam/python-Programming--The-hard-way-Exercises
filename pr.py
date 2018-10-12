import csv

with open("D:\Python\python Sendex\demodata.txt") as csvFile:
    Readcsv = csv.reader(csvFile, delimiter=",")

    date = []
    price = []
    color = []

    for i in Readcsv:
        dates = i[0]
        prices = i[1]
        colors = i[2]

        date.append(dates)
        price.append(prices)
        color.append(colors)

    print(date)
    print(price)
    print(color)


try:
    whatcol = input("Enter the color name you want to see the date of sell:   ")
    coldex = color.index(whatcol.capitalize())
    whatdate = date[coldex]

    print(f"The date is {whatdate} and the sold color is {whatcol}. ")
except Exception as e:
    print(e)
    print("Continue...")
