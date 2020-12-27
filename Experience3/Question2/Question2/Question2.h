#pragma once
#ifndef CTESTKMEANS_H
#define CTESTKMEANS_H

#include <fstream>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

//ȷ������Ĵ������������޸�Ϊ����1��ֵ
#define FEATURE_DIM 2

//����ṹ��
struct Tuple {
	double X;
	double Y;
};

//����CTestMeans�࣬�������ຯ��
class CTestKMeans
{
public:
	CTestKMeans();
	//��ȡ����
	void LoadFeatureFile(const string strFileName, std::vector<Tuple> &lDataList);

	//�������ģ�������ǰԪ�������ĸ���
	int ClusterOfTuple(Tuple means[], Tuple tuple);

	//��������Ԫ����ŷ�������
	float GetDistXY(Tuple t1, Tuple t2);

	//��ø����ؼ���ƽ�����
	float GetVar(vector<Tuple> vCluster[], Tuple means[]);

	//��õ�ǰ�صľ�ֵ�����ģ�
	Tuple GetMeans(vector<Tuple> vCluster);

	//ѵ��������K-means�㷨
	void TrainData(std::vector<Tuple> &vDataList, Tuple tCentroid[FEATURE_DIM]);

	//Ԥ��K-means������������
	std::vector<double> Prediect(Tuple tCentroid[FEATURE_DIM], std::vector<Tuple> vTestList);
};

#endif // CTESTKMEANS_H
