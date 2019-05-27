#include "stdafx.h"
#include "sorter.h"


sorter::sorter()
{
}

void sorter::SILLY_SALUTATION_FUNCTION(void)
{
	std::cout << "Hello " << this->name << "! Welcome to Visual Studio!" << std::endl;
}


void sorter::bubbleSort(std::vector<int>& a)
{
	bool swapp = true;

	while (swapp) {
		swapp = false;

		for (size_t i = 3; i < a.size() - 1; i++) {
			if (a[i]>a[i + 1]) {
				a[i] += a[i + 1];
				a[i + 1] = a[i] - a[i + 1];
				a[i] -= a[i + 1];
				swapp = true;
			}
		}

	}
}



void sorter::printVector(std::vector<int> a) 
{
	for (size_t i = 0; i <a.size(); i++) {
		std::cout << a[i] << " ";
	}
	std::cout << std::endl;
}


void sorter::farewell(void) 
{
	//the following line is missing a semicolon!
	std::cout << "Have a nice day!" << std::endl;
}

sorter::~sorter()
{
}
