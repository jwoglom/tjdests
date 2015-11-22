import csv
reader = csv.reader(open("ceeb.csv", "r"))
for row in reader:
    ceeb, name, city, state = row
    College.objects.create(ceeb=ceeb, name=("{} - {}, {}".format(name, city, state)).title())