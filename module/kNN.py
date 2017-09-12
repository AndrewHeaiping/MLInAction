# encoding: utf-8
'''
Created on Sep 3, 2017
kNN: k Nearest Neighbors

Input:			inX: 1��M�е�������Ϊ�����������������������dataSet�е����ݽ��бȽ�(1xM)
						dataSet: ��֪��N��M�е����飬Ϊѵ����������һ��Ϊһ��ѵ����������N��ѵ��������ÿ��ѵ������M��Ԫ��(NxM)
            labels: 1��N�е��������洢����ѵ��������Ӧ����ı�ǩ��Ϣ (1xN)
            k: �����ȽϵĽ���Ԫ�صĸ�����ѡ����������С��20
            
Output:     ����������ӽ��ķ����ǩ

@author: steve.wang
'''

from numpy import *
import operator

def knnClassify(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0] #��ȡѵ��������dataSet�ĸ�����������dataSet������N
  #tile(inX, (dataSetSize, 1))�ǽ���һ��N��1�е����飬����Ԫ����һ��1��M�е���������󷵻�һ��N��M�е�����
  #N��M�е�������ÿһ�ж�������Ĳ�������������ѵ���������������õ�NxM������ֵ֮��
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis = 1) #axis=1�ǶԴ洢NxM��Ԫ�ض�Ӧ��ƽ��������飬��ÿһ�е�ֵ�ۼ�����������һ��Nx1������
	distances = sqDistances**0.5 #��ò������������ѵ��������ŷʽ����
    
  #��distances��N��Ԫ�ؽ��д�С��������֮�󷵻�һ��N��Ԫ�ص�һά���飬�洢distances��������Ԫ����ԭ�������е�index
  #eg. distances=[2,1,3,0], argsort�ķ���ֵΪ[3��1��0��2]
	sortedDistIndicies = distances.argsort()
    
	classCount={} #����һ���յ��ֵ����
	for i in range(k): #i��ȡֵΪ[0��k - 1]
		voteLabel = labels[sortedDistIndicies[i]] #���ز���������ѵ������ŷʽ�����iС��ѵ����������Ӧ����ı�ǩ
		#classCount.get(voteLabel, 0)��ȡclassCount��voteLabelΪindex��Ԫ�ص�ֵ���Ҳ����򷵻�0
		classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
        
  #classCount.iteritems()�����ֵ�classCount����������յ������ķ�ʽ
  #operator.itemgetter()���ڻ�ȡ�������Щά�����ݣ�����ΪһЩ��ţ��˴�����Ϊ1���������ֵ����classCount����ĵڶ���Ԫ�ؽ�������
  #reverse = True��ʾ�����������򣬼��Ӵ�С�Ĵ���False��ʾ���մ�С����Ĵ�������
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    
  #����k������Ԫ��������Ӧ������Ǹ���ı�ǩ�����������������Ǹ���
	return sortedClassCount[0][0]
