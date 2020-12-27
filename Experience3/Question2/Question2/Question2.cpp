// Question2.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "Question2.h"

//构造函数
CTestKMeans::CTestKMeans()
{

}

//读取数据
void CTestKMeans::LoadFeatureFile(const string strFileName, std::vector<Tuple> &lDataList)
{
	double X, Y;
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
		iFile >> X >> Y;
		struct Tuple sData;
		sData.X = X;
		sData.Y = Y;
		lDataList.push_back(sData);

		iFile.get();//获取之后一个字符（后面这几行代码理解为会判断到最后是否为空即可
		//peek方法可以返回下一个却不移动指针
		if (iFile.peek() == '\n')
		{
			break;
		}
	}

	iFile.close();   //关闭文件
}

//计算两个元组间的欧几里距离
float CTestKMeans::GetDistXY(Tuple t1, Tuple t2)
{
	return sqrt((t1.X - t2.X) * (t1.X - t2.X) + (t1.Y - t2.Y) * (t1.Y - t2.Y));
}

//根据质心，决定当前元组属于哪个簇
int CTestKMeans::ClusterOfTuple(Tuple tCentroid[], Tuple tTest)
{
	float fDistance = GetDistXY(tCentroid[0], tTest);//当前元组与第一个质心的欧式距离
	float fTmp;
	int nLabel = 0;//标示属于哪一个簇
	for (int i = 1; i < FEATURE_DIM; i++)
	{
		fTmp = GetDistXY(tCentroid[i], tTest);//当前元组与第i个质心的欧氏距离
		if (fTmp < fDistance)//取最近的欧氏距离
		{
			fDistance = fTmp;
			nLabel = i;
		}
	}
	return nLabel;
}

//获得给定簇集的平方误差
float CTestKMeans::GetVar(vector<Tuple> vCluster[], Tuple means[]) {
	float fVar = 0;
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		vector<Tuple> vTuple = vCluster[i];
		for (int j = 0; j < vTuple.size(); j++)
		{
			fVar += GetDistXY(vTuple[j], means[i]);
		}
	}
	return fVar;

}
//获得当前簇的均值（质心）
Tuple CTestKMeans::GetMeans(vector<Tuple> vCluster) {

	int nNum = vCluster.size();
	double dMeansX = 0, dMeansY = 0;
	Tuple tTmp;
	for (int i = 0; i < nNum; i++)
	{
		dMeansX += vCluster[i].X;
		dMeansY += vCluster[i].Y;
	}
	tTmp.X = dMeansX / nNum;
	tTmp.Y = dMeansY / nNum;
	return tTmp;
}

//训练集进行K-means算法
void CTestKMeans::TrainData(std::vector<Tuple> &vDataList, Tuple tCentroid[FEATURE_DIM])
{//vDataList：所有数据项	          tCentroid[FEATURE_DIM]：有FEATURE_DIM项数据，为每一类的质心位置
	
	vector<Tuple> vClusters[FEATURE_DIM];//可以理解为是个二维链表，存储某一类中的所有项


	//默认一开始将前FEATURE_DIM个元组的值作为FEATURE_DIM个簇的质心（均值）
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		tCentroid[i].X = vDataList[i].X;
		tCentroid[i].Y = vDataList[i].Y;
	}

	int nLable = 0;	//标注这一项为哪一类
	//根据默认的质心给簇赋值
	for (int i = 0; i < vDataList.size(); i++)
	{
		//ClusterOfTuple：返回项所属类
		nLable = ClusterOfTuple(tCentroid, vDataList[i]);
		//将此项放至对应类中
		vClusters[nLable].push_back(vDataList[i]);
	}

	float fOldVar = -1;//第一次初始化为-1确保至少迭代一次
	float fNewVar = GetVar(vClusters, tCentroid);//	//获得给定簇集的平方误差
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
		cout << "tCentroid" << i+1 << ": " <<"("<< tCentroid[i].X << "," << tCentroid[i].Y <<")"<< endl;
	}
}


//预测K-means后所属簇类结果
std::vector<double> CTestKMeans::Prediect(Tuple tCentroid[FEATURE_DIM], std::vector<Tuple> vTestList)
{
	//一维链表
	std::vector<double> vdResult;
	for (int i = 0; i < vTestList.size(); i++) 
	{
		Tuple tTest;
		tTest.X = vTestList[i].X;
		tTest.Y = vTestList[i].Y;
		int nRet = ClusterOfTuple(tCentroid, tTest);
		vdResult.push_back(nRet + 1);//类从1开始
		std::cout << "("<< vTestList[i].X<<","<< vTestList[i].Y<<")" << "\t" << vdResult[i] << endl;
	}

	return vdResult;
}



int main()
{
	CTestKMeans iKMeansTester;

	//vDataList:训练集数据链表			vTestList：测试集数据链表
	std::vector<Tuple> vDataList, vTestList;


	//确定聚类的簇数的质心，簇数默认为2，可进入.h文件中修改
	Tuple dataCentroid[FEATURE_DIM];

	//导入数据
	iKMeansTester.LoadFeatureFile("D:/DATA MINING/Experience3/train.txt", vDataList);
	iKMeansTester.LoadFeatureFile("D:/DATA MINING/Experience3/test.txt", vTestList);

	//训练集进行K-means算法
	std::cout << "各簇的质心：" << std::endl;
	iKMeansTester.TrainData(vDataList, dataCentroid);
	std::cout << "************************************" << std::endl;

	//预测K-means后所属簇类结果
	std::cout << "训练集测试情况：" << std::endl;
	std::vector<double> vdRecallResult = iKMeansTester.Prediect(dataCentroid, vDataList);
	std::cout << "************************************" << std::endl;

	//根据训练集测试测试集中项该属于哪类
	std::cout << "测试集测试情况：" << std::endl;
	std::vector<double> vdTestResult = iKMeansTester.Prediect(dataCentroid, vTestList);
	std::cout << "************************************" << std::endl;

	////定义文件输出流（用于可视化程序）
	//ofstream oFile;

	////打开要输出的文件
	//oFile.open("result.csv", ios::out | ios::trunc);
	//oFile << "X" << "," << "Y" << "," << "Center_X" <<","<<"Center_Y"<< "," << "Class" << endl;
	//for (int i = 0; i < vDataList.size(); i++)
	//{
	//	int a = vdRecallResult[i];
	//	oFile << vDataList[i].X<< "," << vDataList[i].Y << "," << dataCentroid[a-1].X<<","<<dataCentroid[a-1].Y << "," << vdRecallResult[i]<< endl;
	//}
	//oFile.close();

	return 0;
}


