import csv
count=0
mycsv = csv.reader(open('Crime.csv'))
for row in mycsv:
   crime_type = row[8] ### this will return type of crime
   crime_id = row[7] 
  if crime_type == crime_type :
       count=count+1  
   #mylist=text
  # newlist=set(mylist) 
  # for item in text:
   #   a=item.unique()
    #  print (a)  
 # for row in zip(text):
  #   print (' '.join(row))
   print(crime_type)
   print(crime_id)
   print(count)

