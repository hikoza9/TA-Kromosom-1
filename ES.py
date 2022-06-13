import math
import numpy as np
import random
import JST
import Loader as load

global inps
global num_input
global num_hidden
global num_output

def initKromosom1(kl, interval):
	kromosom = []
	for i in xrange(kl+1):
		kromosom.append((np.random.normal()*(2*interval))-interval)

def initKromosom(kl, interval):
	return np.asarray([(np.random.normal()*(2*interval))-interval for i in xrange(kl+1)])

def initPopulasi(pops, kl, interval):
	return np.random.uniform(-interval, interval, (pops,kl+1))

def selectParent(pop):
	return np.array((pop[int(math.floor(random.uniform(0,len(pop))))], pop[int(math.floor(random.uniform(0,len(pop))))]))

def rekombinasi(kl, par):
	# par = np.array([[(par[0][i]+par[1][i])/2 for i in xrange(kl+1)]])
	par = np.array([np.sum(par, axis=0)/2])
	return par
	# return np.array([np.sum(par, axis=0)/2])

def mutasi(kl, pop, interval):
	t = 1/math.sqrt(kl)
	# pop[...,-1] = pop[...,-1]*math.exp(t*random.normalvariate(0,1))
	for i in xrange(len(pop)):
		for j in xrange(kl):
			# pop[i][j] = pop[i][j]+(pop[...,-1][i]*random.normalvariate(0,1))
			pop[i][kl] = pop[i][kl]*math.exp(t*random.normalvariate(0,1))
			pop[i][j] = pop[i][j]+(pop[i][kl]*random.normalvariate(0,1))
	return pop

def fitness(pop):
	return 1/(JST.mse(inps, pop, num_input, num_hidden, num_output)+0.0001)
	# return 1/((math.pow((kr[0] + (2*kr[1]) - 7),2) + math.pow(((2*kr[0]) + kr[1] - 5),2))+0.0001)

def fitnessRank(pop):
	fit = np.array(fitness(pop))
	return np.array((  np.insert(pop, len(pop[0]), fit.T, axis=1)  ))

def evolution(kl, pop, threshold, interval, pC, pM):
	lamda = 0
	child = np.zeros((1,kl+1))

	while lamda < threshold:
		par = selectParent(pop)
		# rek = rekombinasi(kl, par)
		# mut = mutasi(kl, rek, interval)
		# child = np.append(child,mut,axis=0)
		# lamda += 1
		probRek = random.uniform(0,1)
		probMut = random.uniform(0,1)
		if probRek <= pC:
			rek = rekombinasi(kl, par)
			if probMut <= pM:
				mut = mutasi(kl, rek, interval)
				child = np.append(child,mut,axis=0)
				lamda += 1
			else:
				child = np.append(child,rek,axis=0)
				lamda += 1
		elif probMut <= pM:
			mut = mutasi(kl, par, interval)
			child = np.append(child,mut,axis=0)
			lamda += 2
		elif probMut > pM and probRek > pC:
			child = np.append(child,par,axis=0)
			lamda += 2

	child = np.delete(child,0,0)
	return child

def selectSurvivor(pop, child):
	fitRank = fitnessRank(child)
	sort = fitRank[np.argsort(fitRank[:,-1])][::-1][:len(pop),:]
	return sort[:,:-1], sort[:,-1]


def es(kl, pops, gens, pC, pM, num_inputx, num_hiddenx, num_outputx, data):
	threshold = 7*pops
	interval = 1
	# termination = 0
	global inps
	global num_input
	global num_hidden
	global num_output
	num_hidden = num_hiddenx
	num_input = num_inputx
	num_output = num_outputx
	inps = load.loadCsv(data)
	pop = initPopulasi(pops, kl, interval)
	gen = 0
	# while termination < 10000:
	while gen < gens:
		# child = evolution(kl, pop, threshold, interval)
		# pop, sortedFitness = selectSurvivor(pop, child)
		pop, sortedFitness = selectSurvivor(pop, evolution(kl, pop, threshold, interval, pC, pM))
		
		# termination = sortedFitness[0]
		gen += 1
		# print termination
		print gen, 1/sortedFitness[0]
	return pop[0]