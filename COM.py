# coding:utf-8
import os

import pandas as pd

import ruleMap
from machineLearing.classification import preprocess

rootDir = os.path.dirname(os.getcwd())
print(rootDir)
cameraDataDirPath = os.path.join(rootDir, 'data', 'cameraData')
filePath = os.path.join(cameraDataDirPath, 'Trimmed_hanwenshan_p1.trc')
data = preprocess.getCameraTypeData(filePath)


def calMeanPoint(row, pointList):
    x_mean = 0.0
    y_mean = 0.0
    for mark in pointList:
        targetColumns = row[ruleMap.markAxisMap[mark]]
        x = targetColumns[ruleMap.markAxisMap[mark][0]]
        y = targetColumns[ruleMap.markAxisMap[mark][1]]
        x_mean += x
        y_mean += y
    x_mean = x_mean / len(pointList)
    y_mean = y_mean / len(pointList)
    return x_mean, y_mean


def calCom(data, gender):
    for index in data.index:
        row = data.loc[index]
        com_x = 0.0
        com_y = 0.0
        for people_part, features in ruleMap.MarkMap.items():
            au = features['a_u']
            al = features['a_l']
            au_x, au_y = calMeanPoint(row, au)
            al_x, al_y = calMeanPoint(row, al)
            com_x += (features['gender'][gender]['p_s']/100) * ((1 - features['gender'][gender]['l_s']/100) * au_x + (features['gender'][gender]['l_s']/100) * al_x) / \
                     ruleMap.correctMap[gender]
            com_y += (features['gender'][gender]['p_s']/100) * ((1 - features['gender'][gender]['l_s']/100) * au_y + (features['gender'][gender]['l_s'] * al_y)/100) / \
                     ruleMap.correctMap[gender]
        data.loc[index,'com_x'] = com_x
        data.loc[index,'com_y'] = com_y
    return data


data = calCom(data, 'M')
data.rename(columns={'Unnamed: 0':'frame', 'Unnamed: 1':'time'}, inplace = True)
calColumn=['frame','time','com_x','com_y']
for key,pos in ruleMap.footPos.items():
    calColumn.extend(pos)
careData = data[calColumn]
writer = pd.ExcelWriter('com.xls')
careData.to_excel(writer, sheet_name='com', index=False)
writer.save()
