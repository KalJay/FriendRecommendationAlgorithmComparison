import networkx as nx
import time

exportTextFile = "results.txt"
TrainImportFile = "train.txt"
TestImportFile = "test.txt"

def adamic_adar_calculation(threshold):
    k = 1
    total = 0
    correct = 0
    incorrect = 0
    yes = 0
    no = 0
    yescorrect = 0
    nocorrect = 0

    print("Performing Adamic Adar Link Prediction with threshold value of " + str(threshold))

    startTime = time.time()

    preds = nx.adamic_adar_index(G)
    for u, v, p in preds:
        total += 1
        if((total / 10000) > k):
            k += 1
            print("Analysed " + str(k) + "0k possible connections with an Accuracy Rate of " + str(correct/total*100) + "%", end="\r")
        if(p > threshold):
            yes += 1
            if test.has_edge(v, u):
                yescorrect += 1
                correct += 1
            else:
                incorrect += 1
        else :
            no += 1
            if test.has_edge(v, u):
                incorrect += 1
            else:
                nocorrect += 1
                correct += 1
    print("Accuracy rate was " + str(correct) + " / " + str(total) + " = " + str(correct/total*100) + "%")
    TotalTime = time.time() - startTime
    resultsFile = open(exportTextFile, "a")
    resultsFile.write("Performed Adamic Adar Link Prediction with a threshold value of " + str(threshold) + ".\n")
    resultsFile.write("Analysed " + str(total) + " possible connections. " + str(correct) + " correct predictions and " + str(incorrect) + " incorrect predictions.\n")
    resultsFile.write(str(yes) + " yes predictions of which " + str(yescorrect) + " were correct. " + str(no) + " no predictions of which " + str(nocorrect) + " were correct.\n")
    resultsFile.write("Accuracy Rate of " + str(correct/total*100) + "%. Run time of " + str(TotalTime) + ".\n\n")
    resultsFile.close()

def jaccard_coefficients(threshold):
    
    k = 1
    total = 0
    correct = 0
    incorrect = 0
    yes = 0
    no = 0
    yescorrect = 0
    nocorrect = 0

    print("Performing Jaccard Coefficient Link Prediction with threshold value of " + str(threshold))
    
    startTime = time.time()

    preds = nx.jaccard_coefficient(G)
    for u, v, p in preds:
        total += 1
        if((total / 10000) > k):
            k += 1
            print("Analysed " + str(k) + "0k possible connections with an Accuracy Rate of " + str(correct/total*100) + "%", end="\r")
        if(p > threshold):
            yes += 1
            if test.has_edge(v, u):
                yescorrect += 1
                correct += 1
            else:
                incorrect += 1
        else :
            no += 1
            if test.has_edge(v, u):
                incorrect += 1
            else:
                nocorrect += 1
                correct += 1
    print("Accuracy rate was " + str(correct) + " / " + str(total) + " = " + str(correct/total*100) + "%")
    TotalTime = time.time() - startTime
    resultsFile = open(exportTextFile, "a")
    resultsFile.write("Performed Jaccard Coefficient Link Prediction with a threshold value of " + str(threshold) + ".\n")
    resultsFile.write("Analysed " + str(total) + " possible connections. " + str(correct) + " correct predictions and " + str(incorrect) + " incorrect predictions.\n")
    resultsFile.write(str(yes) + " yes predictions of which " + str(yescorrect) + " were correct. " + str(no) + " no predictions of which " + str(nocorrect) + " were correct.\n")
    resultsFile.write("Accuracy Rate of " + str(correct/total*100) + "%. Run time of " + str(TotalTime) + ".\n\n")
    resultsFile.close()

def within_inter_cluster(threshold):
    
    k = 1
    total = 0
    correct = 0
    incorrect = 0
    yes = 0
    no = 0
    yescorrect = 0
    nocorrect = 0

    print("Performing Within Inter Cluster Link Prediction with threshold value of " + str(threshold))
    
    startTime = time.time()

    preds = nx.jaccard_coefficient(G)
    for u, v, p in preds:
        total += 1
        if((total / 10000) > k):
            k += 1
            print("Analysed " + str(k) + "0k possible connections with an Accuracy Rate of " + str(correct/total*100) + "%", end="\r")
        if(p > threshold):
            yes += 1
            if test.has_edge(v, u):
                yescorrect += 1
                correct += 1
            else:
                incorrect += 1
        else :
            no += 1
            if test.has_edge(v, u):
                incorrect += 1
            else:
                nocorrect += 1
                correct += 1
    print("Accuracy rate was " + str(correct) + " / " + str(total) + " = " + str(correct/total*100) + "%")
    TotalTime = time.time() - startTime
    resultsFile = open(exportTextFile, "a")
    resultsFile.write("Performed Within Inter Cluster Link Prediction with a threshold value of " + str(threshold) + ".\n")
    resultsFile.write("Analysed " + str(total) + " possible connections. " + str(correct) + " correct predictions and " + str(incorrect) + " incorrect predictions.\n")
    resultsFile.write(str(yes) + " yes predictions of which " + str(yescorrect) + " were correct. " + str(no) + " no predictions of which " + str(nocorrect) + " were correct.\n")
    resultsFile.write("Accuracy Rate of " + str(correct/total*100) + "%. Run time of " + str(TotalTime) + ".\n\n")
    resultsFile.close()
        
    
print("Loading File...")
f = open(TrainImportFile, "r")
G = nx.Graph()
test = nx.Graph()
lines = f.readlines()

size = 0
for line in lines :
    nodes = line.split()
    if nodes[0] not in G:
        G.add_node(nodes[0])
        size += 1
    if nodes[1] not in G:
        G.add_node(nodes[1])
        size += 1
    G.add_edge(nodes[0],nodes[1])
print("Successfully imported " + str(size) + " nodes into training graph")
f.close()

f1 = open(TestImportFile, "r")
lines = f1.readlines()
sizetest = 0
for line in lines :
    nodes = line.split()
    if nodes[0] not in test:
        test.add_node(nodes[0])
        sizetest += 1
    if nodes[1] not in test:
        test.add_node(nodes[1])
        sizetest += 1
    test.add_edge(nodes[0],nodes[1])
print("Successfully imported " + str(sizetest) + " nodes into test graph")
f1.close()

adamic_adar_calculation(0)
jaccard_coefficients(0)
within_inter_cluster(0)
adamic_adar_calculation(6)
jaccard_coefficients(0.55)
within_inter_cluster(0.45)


    
