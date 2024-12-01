#!/usr/bin/env python3
import random
from operator import itemgetter
import math

def round_up_to_even(f):
    return math.floor(f / 2.) * 2

def ChromosomDictPrinter(_dict):
    for entry in _dict:
        print(entry)

def PrepareChromosomProbes(_n, _weight): #chromosom prep with _n number of probes and 2^len(weights)
    out = []
    maxValue = 2 ** len(_weight)
    uniqueIntList = random.sample(range(1, maxValue), _n)
    #print(uniqueIntList)
    for uniqueInt in uniqueIntList:
        out.append('0'*(len(_weight) - len(str(bin(uniqueInt))[2:])) + str(bin(uniqueInt))[2:])
    return(out)

def GradeFunction(_w, _p, _c, _chr):
    max_w = 0
    max_p = 0
    for i in range(len(_chr)):
        max_w += _w[i] * int(_chr[i])
        max_p += _p[i] * int(_chr[i])
    if(max_w > _c): #formula when weight ciriteria not met
        max_p = -1 #old formula
        #max_p = max_p + (_c - max_w) 
    #print("chromosom: " + _chr)
    #print("total weight: " + str(max_w))
    #print("total value: " + str(max_p) + "\n")
    return {'chromosom' : _chr, 'weight' : max_w, 'value' : max_p}

def RankingFunction(_w, _p, _c, _chromosomList):
    gradedChromosomsList = []
    for chromosom in _chromosomList:
        gradedChromosomsList.append(GradeFunction(weight, price, capacity, chromosom))
    #ChromosomDictPrinter(gradedChromosomsList)
    ratedChromosoms = sorted(gradedChromosomsList, key=itemgetter('value'), reverse=True)
    #print("ranked")
    ChromosomDictPrinter(ratedChromosoms)
    return ratedChromosoms

def GenCrossing(_rankedChromosomList, _mutationOffset, _isOffsetRandom, ):
    mutationOffset = _mutationOffset
    mutatedChromosomsList = []
    if(_isOffsetRandom or mutationOffset >= len(_rankedChromosomList[0]['chromosom'])):
        mutationOffset = random.randint(1, len(_rankedChromosomList[0]['chromosom'])-1)
    #print(mutationOffset)
    #for i, chromosom in enumerate(_rankedChromosomList[:round_up_to_even(len(_rankedChromosomList)/2):2]):
    print(f"len: {round_up_to_even(len(_rankedChromosomList)/2)}")
    for i in range(round_up_to_even(len(_rankedChromosomList)/2)):
        #print(f"Evolving chromosom r{i*2} {_rankedChromosomList[i*2]['chromosom']} with chromosom r{i*2+1} {_rankedChromosomList[i*2+1]['chromosom']}")
        mutatedChromosomsList.append(_rankedChromosomList[i*2]['chromosom'][:_mutationOffset]+_rankedChromosomList[i*2+1]['chromosom'][_mutationOffset:])
        mutatedChromosomsList.append(_rankedChromosomList[i*2+1]['chromosom'][:_mutationOffset]+_rankedChromosomList[i*2]['chromosom'][_mutationOffset:])
    #print(mutatedChromosomsList)
    return(mutatedChromosomsList)

def GenCrossing2(_rankedChromosomList, _mutationOffset, _isOffsetRandom, ):
    mutationOffset = _mutationOffset
    mutatedChromosomsList = []
    if(_isOffsetRandom or mutationOffset >= len(_rankedChromosomList[0]['chromosom'])):
        mutationOffset = random.randint(1, len(_rankedChromosomList[0]['chromosom'])-1)
    #print(mutationOffset)
    #for i, chromosom in enumerate(_rankedChromosomList[:round_up_to_even(len(_rankedChromosomList)/2):2]):
    for i in range(round_up_to_even(len(_rankedChromosomList)/2)):
        #print(f"Evolving chromosom r{i*2} {_rankedChromosomList[i*2]['chromosom']} with chromosom r{i*2+1} {_rankedChromosomList[i*2+1]['chromosom']}")
        mutatedChromosomsList.append(_rankedChromosomList[i*2]['chromosom'][:_mutationOffset]+_rankedChromosomList[i*2+1]['chromosom'][_mutationOffset:])
        mutatedChromosomsList.append(_rankedChromosomList[i*2+1]['chromosom'][:_mutationOffset]+_rankedChromosomList[i*2]['chromosom'][_mutationOffset:])
        mutatedChromosomsList.append(_rankedChromosomList[i*2]['chromosom'][_mutationOffset:]+_rankedChromosomList[i*2+1]['chromosom'][:_mutationOffset])
        mutatedChromosomsList.append(_rankedChromosomList[i*2+1]['chromosom'][_mutationOffset:]+_rankedChromosomList[i*2]['chromosom'][:_mutationOffset])
    #print(mutatedChromosomsList)
    return(mutatedChromosomsList)

def Evolution(_weight, _price, _capacity, _numOfStartingChromosoms, _numOfGeneration):
    inputChromosoms = PrepareChromosomProbes(_numOfStartingChromosoms, _weight)
    print(inputChromosoms)
    for i in range(_numOfGeneration):
        rankedChromosoms = RankingFunction(_weight, _price, _capacity, inputChromosoms)
        print(f"Best chromosom from this generations is {rankedChromosoms[0]}")
        inputChromosoms = GenCrossing2(rankedChromosoms, 3 , False)


weight = [46, 40, 42, 38, 10]
price = [12, 19, 19, 15, 8]
capacity = 40

Evolution(weight, price, capacity, 10, 3)


#mutatedChromosoms = GenCrossing(out, 3 , False)
#mutatedChromosoms2 = GenCrossing2(out, 3 , False)
#print("crossing no1 \n")
#out2 = RankingFunction(weight, price, capacity, mutatedChromosoms)
#print("crossing no2 \n")
#out3 = RankingFunction(weight, price, capacity, mutatedChromosoms2)