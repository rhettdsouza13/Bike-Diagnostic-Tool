import math
import pandas as pd
import ast
df = pd.read_csv('ontology.txt', sep='\t')

error_count = 14
symptom_count = 11
resolution_count = 12
part_count = 12
condition_count = 9

condDict = {}
partDict = {}

filecontent = """(in-microtheory KRR-Winter2019FactsMt)

;;; Collections
(isa BikePart FirstOrderCollection)
(genls BikePart Device)
(comment BikePart "The collection of all bike parts.")

(isa PartCondition FirstOrderCollection)
(genls PartCondition DescriptionTypeByFocus)
(comment PartCondition "The collection of all part conditions.")

(isa ProblemResolution FirstOrderCollection)
(genls ProblemResolution SolutionStepEventType)
(comment ProblemResolution "The collection of all bike problem resolutions.")

(isa ProblemSymptom FirstOrderCollection)
(comment ProblemSymptom "The collection of possible combinations of bike parts and conditions that cause a defect/problem.")

;;; Predicates / Functions

;;; This function should allow us to enter multiple symptoms
(isa SymptomFn BinaryFunction)
(arity SymptomFn 2)
(arg1Isa SymptomFn PartCondition)
(arg2Isa SymptomFn BikePart)
(resultIsa SymptomFn ProblemSymptom)
(comment SymptomFn “A symptom that includes the given part and condition.”)

;;; Predicate type that relates symptoms to resolutions
(isa solvesProblem DirectBinaryPredicate)
(arity solvesProblem 2)
(arg1Isa solvesProblem Set)
(arg2Isa solvesProblem List)
(comment solvesProblem "A relation indicating that the problem caused by the listed symptoms can be solved by the given list of problem resolutions.")

;;; Rules

;;; This rule allows us to find possible solutions for a given set of symptoms
(<== (partOfRequiredSymptoms ?symptoms ?required ?resolutions)
	(solvesProblem ?required ?resolutions)
	(subsetOf ?symptoms ?required))

;;; Queries

(solvesProblem ?symptoms ?resolutions)

(partOfRequiredSymptoms (TheSet (SymptomFn c7 p2)) ?required ?resolutions)

;;; Facts

"""

# Adding Facts for Parts
filecontent += ";;; Parts\n"
for i in range(part_count):
    filecontent += "(isa " + df.iloc[i].Part + " BikePart)\n"
    filecontent += "(comment " + df.iloc[i].Part + " \"" + df.iloc[i].PartComment + "\")\n\n"
    partDict[df.iloc[i].PartCode] = df.iloc[i].Part

# Adding Facts for Conditions
filecontent += "\n\n;;; Conditions\n"
for i in range(condition_count):
    filecontent += "(isa " + str(df.iloc[i].Condition) + " PartCondition)\n"
    filecontent += "(comment " + str(df.iloc[i].Condition) + " \"" + str(df.iloc[i].ConditionComment) + "\")\n\n"
    condDict[df.iloc[i].ConditionCode] = df.iloc[i].Condition

# Adding Facts for Resolutions
filecontent += "\n\n;;; Resolutions\n"
for i in range(resolution_count):
    filecontent += "(isa " + str(df.iloc[i].ResolutionCode) + " ProblemResolution)\n"
    filecontent += "(comment " + str(df.iloc[i].ResolutionCode) + " \"" + str(df.iloc[i].Resolution) + "\")\n\n"

# Adding Resolutions
filecontent += ";;; Which resolution solves which symptoms/problems\n"
for i in range(error_count):
    symptomlists = ast.literal_eval(df.iloc[i].Symptoms)
    filecontent += "(solvesProblem (TheSet"
    for symptom in symptomlists:
        filecontent += " (SymptomFn " + condDict[symptom[0]] + " " + partDict[symptom[1]] + ")"
    filecontent += ") (ListFn"
    resolutionlist = ast.literal_eval(str(df.iloc[i].Resolutions))
    for resolution in resolutionlist:
        filecontent += " " + resolution
    filecontent += "))\n"

with open('results.krf', 'w') as file:
    file.write(filecontent)