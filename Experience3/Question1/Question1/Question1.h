#pragma once
#ifndef CTESTKMEANS_H
#define CTESTKMEANS_H

#include <fstream>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

//确定聚类的簇数，可任意修改为大于1的值
#define FEATURE_DIM 2

//定义结构体，包含11科成绩
struct Tuple {
	double C1;
	double C2;
	double C3;
	double C4;
	double C5;
	double C6;
	double C7;
	double C8;
	double C9;
	double C10;
	double Constitution;
};

//定义CTestMeans类，声明各类函数
class CTestKMeans
{
public:
	CTestKMeans();
	//读取数据
	void LoadFeatureFile(const string strFileName, std::vector<Tuple> &lDataList);

	//根据质心，决定当前元组属于哪个簇
	int ClusterOfTuple(Tuple means[], Tuple tuple);

	//计算两个元组间的欧几里距离
	float GetDistXY(Tuple t1, Tuple t2);

	//获得给定簇集的平方误差
	float GetVar(vector<Tuple> vCluster[], Tuple tCentroid[]);

	//获得当前簇的均值（质心）
	Tuple GetMeans(vector<Tuple> vCluster);

	//训练集进行K-means算法
	void TrainData(std::vector<Tuple> &vDataList, Tuple tCentroid[FEATURE_DIM]);

	//预测K-means后所属簇类结果
	std::vector<double> Prediect(Tuple tCentroid[FEATURE_DIM], std::vector<Tuple> vTestList);
};

#endif // CTESTKMEANS_H
