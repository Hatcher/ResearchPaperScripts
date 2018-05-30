import csv

processedStudentsArr = []
questionsSeenArr = []
questionsSeenCountArr = []

# This script takes in the student data, and appends the question response iteration to the current question response
# Question response iteration answers the question: "How many times has the student seen this question?"
newCSVFile = open('./processedRows.csv', 'wb')
writer = csv.writer(newCSVFile, delimiter=",")
with open('./temp.csv', 'rU') as csvfile:
    table2Reader = csv.reader(csvfile)
    for row in table2Reader:
        if(row[1] not in processedStudentsArr):
            questionsSeenArr = []
            questionsSeenCountArr = []
            processedStudentsArr.append(row[1])
        if(row[2] not in questionsSeenArr):
            questionsSeenArr.append(row[2])
            questionsSeenCountArr.append(1)
        else:
            questionIndex = questionsSeenArr.index(row[2])
            questionsSeenCountArr[questionIndex] = questionsSeenCountArr[questionIndex] + 1
        row.append(questionsSeenCountArr[questionsSeenArr.index(row[2])])
        writer.writerow(row)
