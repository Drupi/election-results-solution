#!/usr/local/bin/python3
import csv


# C - Conservative Party
# L - Labour Party
# UKIP - UKIP
# LD - Liberal Democrats
# G - Green Party
# Ind - Independent
# SNP - SNP

def pairs(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i +n]

def constituencyReplace(string):
  if string == "C":
    string = "Conservative Party"
  elif string == "L":
    string = "Labour Party"
  elif string == "LD":
    string = "Liberal Democrats"
  elif string == "G":
    string = "Green Party"
  elif string == "Ind":
    string = "Independent"
  return string

def calculatePercents(part, total):
  part = 100 * float(part)/float(total)
  return round(part, 0)



with open('../../data.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    constituencyName = row[0]
    totalVotes = row[1]
    for execution in range(2):
      row.pop(0)
    # Split the list for pairs
    pairRow = list(pairs(row, 2))
    print(constituencyName+"with :"+totalVotes+" votes")
    for pair in pairRow:
      pair = [listObject.strip(' ') for listObject in pair]
      if len(pair) % 2 == 0:
        # Handle errors if the value for constituency will be not int value
        try:
          pair[1] = int(pair[1])
        except:
          pair[1] = 0
      else:
        pair.append(0)
      for iter, _ in enumerate(pair):
        if isinstance(pair[iter], str):
          pair[iter] = constituencyReplace(pair[iter])
        else:
          pair[iter] = calculatePercents(pair[iter], totalVotes)
      print(pair)
          