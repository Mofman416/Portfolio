#pragma once

#include <vector>
#include <iostream>
#include <string>

class sorter
{
public:
	sorter();

	void SILLY_SALUTATION_FUNCTION(void);

	void bubbleSort(std::vector<int>& a);

	void printVector(std::vector<int> a);

	void farewell(void);

	~sorter();

private:
	std::string name = "____";
};

