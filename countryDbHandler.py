import pandas
import csv


def checkForSpaces():
    outfile = open('links.csv', 'w', newline='')
    col_list = ["Country"]
    df = pandas.read_csv("country.csv", usecols=col_list)

    whitespace_char = " "
    hypen_char = "-"

    allTheCountries = []

    for country in df['Country']:
        country = country.strip("\r\n\t")
        country = country.strip()
        if(whitespace_char in country):
            split_country = country.split(" ")
            allTheCountries.append(hypen_char.join(split_country))
        else:
            allTheCountries.append(country)
    return allTheCountries
