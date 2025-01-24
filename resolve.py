#!/usr/bin/env python3
import random
from operator import itemgetter
import math


def round_up_to_even(f):
    return math.floor(f / 2.) * 2


def ChromosomDictPrinter(_dict):
    for entry in _dict:
        print(entry)


#def PrepareChromosomProbes(_n, _weight): #chromosom prep with _n number of probes and 2^len(weights) # to fixed
#    out = []
#    maxValue = 2 ** len(_weight)
#    uniqueIntList = random.sample(range(1, maxValue), _n) #0x00001
#    #print(uniqueIntList)
#    for uniqueInt in uniqueIntList:
#        out.append('0'*(len(_weight) - len(str(bin(uniqueInt))[2:])) + str(bin(uniqueInt))[2:])
#    return(out)


def PrepareChromosomProbes(_n, _weight):
    out = []
    for i in range(_n):
        chrom_str = ""
        for j in range(len(_weight)):
            chrom_str += str(random.randint(0,1))
        out.append(chrom_str)
    return(out)


def GradeFunction(_w, _p, _c, _chr): # with -1 when criteria not met
    max_w = 0
    max_p = 0
    for i in range(len(_chr)):
        max_w += _w[i] * int(_chr[i])
        max_p += _p[i] * int(_chr[i])
    if(max_w > _c): #formula when weight ciriteria not met
        max_p = -1
    return {'chromosom' : _chr, 'weight' : max_w, 'value' : max_p}


def GradeFunction2(_w, _p, _c, _chr): # with price/weight grade when criteria not met
    max_w = 0
    max_p = 0
    for i in range(len(_chr)):
        max_w += _w[i] * int(_chr[i])
        max_p += _p[i] * int(_chr[i])
    if(max_w > _c): #formula when weight ciriteria not met
        max_p = round(max_p / max_w, 2)
    return {'chromosom' : _chr, 'weight' : max_w, 'value' : max_p}


def RankingFunction(_w, _p, _c, _chromosomList):  #simple ranking by value - turnamment?
    gradedChromosomsList = []
    for chromosom in _chromosomList:
        gradedChromosomsList.append(GradeFunction(weight, price, capacity, chromosom))
    #ChromosomDictPrinter(gradedChromosomsList)
    ratedChromosoms = sorted(gradedChromosomsList, key=itemgetter('value'), reverse=True)
    print("Ranked chromosoms - START")
    ChromosomDictPrinter(ratedChromosoms)
    print("Ranked chromosoms - DONE")
    return ratedChromosoms


def SelectFunctionTurnamment(_gradedChromosomsList):  #Selection - 2 groups turnamment? 
    selectedChromosoms = []
    uniqueIntList = random.sample(range(0, len(_gradedChromosomsList)), len(_gradedChromosomsList))
    for i in uniqueIntList:
        selectedChromosoms.append(_gradedChromosomsList[i])
    group1 = selectedChromosoms[:(len(selectedChromosoms)//2)]
    group2 = selectedChromosoms[(len(selectedChromosoms)//2):]
    ratedgroup1 = sorted(group1, key=itemgetter('value'), reverse=True)
    ratedgroup2 = sorted(group2, key=itemgetter('value'), reverse=True)
    #print("Rated group1:")
    #ChromosomDictPrinter(ratedgroup1)
    #print("Rated group2:")
    #ChromosomDictPrinter(ratedgroup2)
    selectedChromosoms = []
    for i in range(len(ratedgroup1)):
        selectedChromosoms.append(ratedgroup1[i])
        selectedChromosoms.append(ratedgroup2[i])
    #print(f"Rated by 2 group turnamment: {selectedChromosoms}")
    print("Selected by 2 group turnamment:")
    ChromosomDictPrinter(selectedChromosoms)
    return selectedChromosoms


def SelectFunctionRullete(_gradedChromosomsList):  #Random
    selectedChromosoms = []
    uniqueIntList = random.sample(range(0, len(_gradedChromosomsList)), len(_gradedChromosomsList))
    for i in uniqueIntList:
        selectedChromosoms.append(_gradedChromosomsList[i])
    print("Selected by Rullete:")
    ChromosomDictPrinter(selectedChromosoms)
    return selectedChromosoms


def GenCrossing(_rankedChromosomList, _crossPoint, _isOffsetRandom, ):   #todo fixed size of output population = input population 
    crossPoint = _crossPoint
    crossedChromosomsList = []
    if(_isOffsetRandom or crossPoint >= len(_rankedChromosomList[0]['chromosom'])):  #set random crossing point if not given or out of scope
        crossPoint = random.randint(1, len(_rankedChromosomList[0]['chromosom'])-1)
    #selekcja do krzyzowania
    selectedChromosoms = SelectFunctionRullete(_rankedChromosomList)
    for i in range(0, len(_rankedChromosomList)-1, 2):
        print(f"Evolving chromosom r{i} {selectedChromosoms[i]['chromosom']} with chromosom r{i+1} {selectedChromosoms[i+1]['chromosom']}")
        crossedChromosomsList.append(selectedChromosoms[i]['chromosom'][:_crossPoint]+selectedChromosoms[i+1]['chromosom'][_crossPoint:]) #a1b2
        crossedChromosomsList.append(selectedChromosoms[i+1]['chromosom'][:_crossPoint]+selectedChromosoms[i]['chromosom'][_crossPoint:]) #b1a2
    print("crossedChromosomsList - START")
    print(crossedChromosomsList)
    print("crossedChromosomsList - DONE")
    return(crossedChromosomsList)


#def GenCrossing2(_rankedChromosomList, _mutationOffset, _isOffsetRandom, ):  #to be fixed
#    mutationOffset = _mutationOffset
#    mutatedChromosomsList = []
#    if(_isOffsetRandom or mutationOffset >= len(_rankedChromosomList[0]['chromosom'])):
#        mutationOffset = random.randint(1, len(_rankedChromosomList[0]['chromosom'])-1)
#    for i in range(0, len(_rankedChromosomList)-1, 2):
#        #print(f"Evolving chromosom r{i*2} {_rankedChromosomList[i*2]['chromosom']} with chromosom r{i*2+1} {_rankedChromosomList[i*2+1]['chromosom']}")
#        mutatedChromosomsList.append(_rankedChromosomList[i]['chromosom'][:_mutationOffset]+_rankedChromosomList[i+1]['chromosom'][_mutationOffset:]) #a1b2
#        mutatedChromosomsList.append(_rankedChromosomList[i+1]['chromosom'][:_mutationOffset]+_rankedChromosomList[i]['chromosom'][_mutationOffset:]) #b1a2
#        mutatedChromosomsList.append(_rankedChromosomList[i]['chromosom'][_mutationOffset:]+_rankedChromosomList[i+1]['chromosom'][:_mutationOffset]) #b2a1
#        mutatedChromosomsList.append(_rankedChromosomList[i+1]['chromosom'][_mutationOffset:]+_rankedChromosomList[i]['chromosom'][:_mutationOffset]) #a2b1
#    #print(mutatedChromosomsList)
#    return(mutatedChromosomsList)


def GenCrossing2(_rankedChromosomList, _alpha):  #arithmetic crossover - less predictable + more diversity
    crossedChromosomsList = []
    #selekcja do krzyzowania
    selectedChromosoms = SelectFunctionRullete(_rankedChromosomList)
    for i in range(0, len(_rankedChromosomList)-1, 2):
        print(f"Arithmetic crossover chromosom r{i} {selectedChromosoms[i]['chromosom']} with chromosom r{i+1} {selectedChromosoms[i+1]['chromosom']} and ALPHA = {_alpha}")
        childGen1 = []
        childGen2 = []
        for chromosomBit1, chromosomBit2 in zip(selectedChromosoms[i]['chromosom'], selectedChromosoms[i+1]['chromosom']):
            new_chromosomBit1 = round(_alpha * int(chromosomBit1) + (1 - _alpha) * int(chromosomBit2))
            new_chromosomBit2 = round((1 - _alpha) * int(chromosomBit1) + _alpha * int(chromosomBit2))
            childGen1.append(new_chromosomBit1)
            childGen2.append(new_chromosomBit2)
        crossedChromosomsList.append(childGen1)
        crossedChromosomsList.append(childGen2)
    print("crossedChromosomsList - START")
    print(crossedChromosomsList)
    print("crossedChromosomsList - DONE")
    return(crossedChromosomsList)


def Evolution(_weight, _price, _capacity, _numOfStartingChromosoms, _numOfGeneration):
    inputChromosoms = PrepareChromosomProbes(_numOfStartingChromosoms, _weight)
    print(inputChromosoms)
    for i in range(_numOfGeneration):
        print("################NEW GENERATION###################")
        rankedChromosoms = RankingFunction(_weight, _price, _capacity, inputChromosoms)
        print(f"Best chromosom from this generation #{i} is {rankedChromosoms[0]}")
        inputChromosoms = GenCrossing2(rankedChromosoms, 0.3) #alpha = 0.3 - bardziej podobne do gen parent2


weight = [46, 40, 42, 38, 10]
price = [12, 19, 19, 15, 8]
capacity = 40

Evolution(weight, price, capacity, 10, 5)


#mutatedChromosoms = GenCrossing(out, 3 , False)
#mutatedChromosoms2 = GenCrossing2(out, 3 , False)
#print("crossing no1 \n")
#out2 = RankingFunction(weight, price, capacity, mutatedChromosoms)
#print("crossing no2 \n")
#out3 = RankingFunction(weight, price, capacity, mutatedChromosoms2)