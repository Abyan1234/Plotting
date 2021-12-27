import csv
import plotly.express as px

rows = []

with open("final_total_stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]


mass = []
radius = []
star_name=[]
for star_data in star_data_rows:
  mass.append(star_data[4])
  radius.append(star_data[5])
  star_name.append(star_data[2])

star_gravity = []

for index, name in enumerate(star_name):
  gravity = (float(mass[index])*1.989+30) / (float(radius[index])*float(radius[index])*6.957e+8)
  star_gravity.append(gravity)

fig = px.scatter(x=radius, y=mass, size=star_gravity, hover_data=[star_name])
fig.show()

