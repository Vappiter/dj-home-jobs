import csv


with open ('Z:\\2021-09-23_PYTHON\django\dj-home-jobs\dj-homeworks\\1.2-requests-templates\pagination\data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    my_csvfile = csv.DictReader (csvfile,delimiter = ",")
    print(my_csvfile)
    y = []
    for x in my_csvfile:
      y.append({'Name':x['Name'], 'Street': x['Street'], 'District':x['District']})  
      print (y)
      break
