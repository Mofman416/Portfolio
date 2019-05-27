// demoApplication.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "sorter.h"

using namespace std;

int main()
{
	int testInt;

	sorter mySorter = sorter();
	mySorter.SILLY_SALUTATION_FUNCTION();

	vector<int> sortThisVector = { 3, 10, 2, 5, 1, 8, 9, 7, 6, 4 };

	testInt = 5;
	sortThisVector.push_back(testInt);

	cout << "Unsorted list: " << endl;
	mySorter.printVector(sortThisVector);

	mySorter.bubbleSort(sortThisVector);

	cout << "Sorted list: " << endl;
	mySorter.printVector(sortThisVector);

	//add a call to mySorter.farewell() below this line



    return 0;
}

