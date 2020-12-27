// Question1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <iostream>
#include "Question1.h"

//构造函数
CTestKMeans::CTestKMeans()
{

}

//读取数据
void CTestKMeans::LoadFeatureFile(const string strFileName, std::vector<Tuple> &lDataList)
{
	double C1, C2, C3,C4,C5,C6,C7,C8,C9,C10, Constitution;
	ifstream iFile;
	iFile.open(strFileName.c_str(), ios::in);
	if (!iFile.is_open())		//文件无法正确打开
		cout << "open file failure!" << endl;
	if (iFile.peek() == EOF)		//文件若为空
	{
		cout << "file is empty!" << endl;
		return;
	}
	while (!iFile.eof())            // 若未到文件结束一直循环
	{
		iFile >> C1 >> C2 >> C3>>C4>>C5>>C6>>C7>>C8>>C9>>C10>> Constitution;
		struct Tuple sData;
		sData.C1 = C1;
		sData.C2 = C2;
		sData.C3 = C3;
		sData.C4 = C4;
		sData.C5 = C5;
		sData.C6 = C6;
		sData.C7 = C7;
		sData.C2 = C2;
		sData.C8 = C8;
		sData.C9 = C9;
		sData.C10 = C10;
		sData.Constitution = Constitution;
		lDataList.push_back(sData);

		iFile.get();//获取之后一个字符（后面这几行代码理解为会判断到最后是否为空即可）
		//peek方法可以返回下一个却不移动指针
		if (iFile.peek() == '\n')
		{
			break;
		}
	}

	iFile.close();   //关闭文件
}

//计算两个元组间的欧式距离
float CTestKMeans::GetDistXY(Tuple t1, Tuple t2)
{
	return sqrt((t1.C1 - t2.C1) * (t1.C1 - t2.C1) + (t1.C2 - t2.C2) * (t1.C2 - t2.C2) + (t1.C3 - t2.C3) * (t1.C3 - t2.C3) + (t1.C4 - t2.C4) * (t1.C4 - t2.C4) + (t1.C5 - t2.C5) * (t1.C5 - t2.C5) + (t1.C6 - t2.C6) * (t1.C6 - t2.C6) + (t1.C7 - t2.C7) * (t1.C7 - t2.C7) + (t1.C8 - t2.C8) * (t1.C8 - t2.C8) + (t1.C9 - t2.C9) * (t1.C9 - t2.C9) + (t1.C10 - t2.C10) * (t1.C10 - t2.C10) + (t1.Constitution - t2.Constitution) * (t1.Constitution - t2.Constitution));
}

//根据质心，决定当前项属于哪个簇
int CTestKMeans::ClusterOfTuple(Tuple tCentroid[], Tuple vDataList)
{
	float fDistance = GetDistXY(tCentroid[0], vDataList);//当前元组与第一个质心的欧式距离
	float fTmp;
	int nLabel = 0;//标示属于哪一个簇
	for (int i = 1; i < FEATURE_DIM; i++)
	{
		fTmp = GetDistXY(tCentroid[i], vDataList);//当前元组与第i个质心的欧氏距离
		if (fTmp < fDistance)//取最近的欧氏距离
		{
			fDistance = fTmp;
			nLabel = i;
		}
	}
	return nLabel;
}

//获得给定簇集的平方误差
float CTestKMeans::GetVar(vector<Tuple> vCluster[], Tuple tCentroid[]) {
	float fVar = 0;
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		vector<Tuple> vTuple = vCluster[i];
		for (int j = 0; j < vTuple.size(); j++)
		{
			fVar += GetDistXY(vTuple[j], tCentroid[i]);
		}
	}
	return fVar;

}

//获得当前簇的均值（质心）
Tuple CTestKMeans::GetMeans(vector<Tuple> vCluster) {

	int nNum = vCluster.size();
	double dMeansC1 = 0, dMeansC2 = 0, dMeansC3 = 0, dMeansC4 = 0, dMeansC5 = 0, dMeansC6 = 0, dMeansC7 = 0, dMeansC8 = 0, dMeansC9 = 0, dMeansC10 = 0, dMeansConstitution = 0;
	Tuple tTmp;
	for (int i = 0; i < nNum; i++)
	{
		dMeansC1 += vCluster[i].C1;
		dMeansC2 += vCluster[i].C2;
		dMeansC3 += vCluster[i].C3;
		dMeansC4 += vCluster[i].C4;
		dMeansC5 += vCluster[i].C5;
		dMeansC6 += vCluster[i].C6;
		dMeansC7 += vCluster[i].C7;
		dMeansC8 += vCluster[i].C8;
		dMeansC9 += vCluster[i].C9;
		dMeansC10 += vCluster[i].C10;
		dMeansConstitution += vCluster[i].Constitution;
	}
	tTmp.C1 = dMeansC1 / nNum;
	tTmp.C2 = dMeansC2 / nNum;
	tTmp.C3 = dMeansC3 / nNum;
	tTmp.C4 = dMeansC4 / nNum;
	tTmp.C5 = dMeansC5 / nNum;
	tTmp.C6 = dMeansC6 / nNum;
	tTmp.C7 = dMeansC7 / nNum;
	tTmp.C8 = dMeansC8 / nNum;
	tTmp.C9 = dMeansC9 / nNum;
	tTmp.C10 = dMeansC10 / nNum;
	tTmp.Constitution = dMeansConstitution / nNum;
	return tTmp;
}

//训练集进行K-means算法
void CTestKMeans::TrainData(std::vector<Tuple> &vDataList, Tuple tCentroid[FEATURE_DIM])
{	//vDataList：所有数据项	          tCentroid[FEATURE_DIM]：有FEATURE_DIM项数据，为每一类的质心位置

	vector<Tuple> vClusters[FEATURE_DIM];	//可以理解为是个二维链表，存储某一类中的所有项

	//默认一开始将前FEATURE_DIM个元组的值作为FEATURE_DIM个簇的质心
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		tCentroid[i].C1 = vDataList[i].C1;
		tCentroid[i].C2 = vDataList[i].C2;
		tCentroid[i].C3 = vDataList[i].C3;
		tCentroid[i].C4 = vDataList[i].C4;
		tCentroid[i].C5 = vDataList[i].C5;
		tCentroid[i].C6 = vDataList[i].C6;
		tCentroid[i].C7 = vDataList[i].C7;
		tCentroid[i].C8 = vDataList[i].C8;
		tCentroid[i].C9 = vDataList[i].C9;
		tCentroid[i].C10 = vDataList[i].C10;
		tCentroid[i].Constitution = vDataList[i].Constitution;
	}

	int nLable = 0;		//标注这一项为哪一类
	//根据默认的质心给簇赋值
	for (int i = 0; i < vDataList.size(); i++)
	{
		//ClusterOfTuple：返回项所属类
		nLable = ClusterOfTuple(tCentroid, vDataList[i]);
		//将此项放至对应类中
		vClusters[nLable].push_back(vDataList[i]);
	}

	float fOldVar = -1;//第一次初始化为-1确保至少迭代一次
	float fNewVar = GetVar(vClusters, tCentroid);//获得给定簇集的平方误差
	while (fabs(fNewVar - fOldVar) > 0.1) //当新旧函数值相差不到1即准则函数值不发生明显变化时，算法终止
	{
		for (int i = 0; i < FEATURE_DIM; i++) //更新每个簇的中心点
		{
			//GetMeans返回每一类的质心
			tCentroid[i] = GetMeans(vClusters[i]);
			//cout<<"means["<<i<<"]:"<<tCentroid[i].Height<<"  "<<tCentroid[i].Weight<<endl;
		}
		fOldVar = fNewVar;
		//获得给定簇集的平方误差
		fNewVar = GetVar(vClusters, tCentroid); //计算新的准则函数值
		for (int i = 0; i < FEATURE_DIM; i++) //清空每个簇
		{
			vClusters[i].clear();
		}
		//根据新的质心获得新的簇
		for (int i = 0; i < vDataList.size(); i++)
		{
			//ClusterOfTuple：返回项所属类
			nLable = ClusterOfTuple(tCentroid, vDataList[i]);
			//将此项放至对应类中
			vClusters[nLable].push_back(vDataList[i]);
		}
	}
	//打印质心位置
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		cout << "tCentroid"<< i + 1 <<": "<<"("<< tCentroid[i].C1 << "," << tCentroid[i].C2 << "," << tCentroid[i].C3 << "," << tCentroid[i].C4 << "," << tCentroid[i].C5 << "," << tCentroid[i].C6 << "," << tCentroid[i].C7 << "," << tCentroid[i].C8 << "," << tCentroid[i].C9 << "," << tCentroid[i].C10 << "," << tCentroid[i].Constitution<<")" << endl;
	}
}


//预测K-means后所属簇类结果
std::vector<double> CTestKMeans::Prediect(Tuple tCentroid[FEATURE_DIM], std::vector<Tuple> vTestList)
{
	//一维链表
	std::vector<double> vdResult;
	for (int i = 0; i < vTestList.size(); i++) {
		Tuple tTest;
		tTest.C1 = vTestList[i].C1;
		tTest.C2 = vTestList[i].C2;
		tTest.C3 = vTestList[i].C3;
		tTest.C4 = vTestList[i].C4;
		tTest.C5 = vTestList[i].C5;
		tTest.C6 = vTestList[i].C6;
		tTest.C7 = vTestList[i].C7;
		tTest.C8 = vTestList[i].C8;
		tTest.C9 = vTestList[i].C9;
		tTest.C10 = vTestList[i].C10;
		tTest.Constitution = vTestList[i].Constitution;
		int nRet = ClusterOfTuple(tCentroid, tTest);
		vdResult.push_back(nRet+1);//类从1开始
		std::cout <<"ID:"<<i<<"\t"<< vdResult[i] << endl;
	}

	return vdResult;
}


int main()
{
	CTestKMeans iKMeansTester;

	//DataList:训练集数据链表	
	std::vector<Tuple> DataList;


	//确定聚类的簇数的质心，簇数默认为2，可进入.h文件中修改
	Tuple dataCentroid[FEATURE_DIM];

	//导入数据
	iKMeansTester.LoadFeatureFile("D:/DATA MINING/Experience3/归一化数据矩阵.txt", DataList);

	//训练集进行K-means算法
	std::cout << "各簇的质心：" << std::endl;
	iKMeansTester.TrainData(DataList, dataCentroid);
	std::cout << "************************************" << std::endl;

	//预测K-means后所属簇类结果
	std::cout << "学生所属的簇类：" << std::endl;
	iKMeansTester.Prediect(dataCentroid, DataList);
	std::cout << "************************************" << std::endl;

	return 0;
}
