// Lesson on conditionals and logic from Codecademy

#include <iostream>

int main() {

	double weight;
	int x;

	std::cout << "Please enter you weight on Earth in lbs\n";
	std::cin >> weight;

	std::cout << "These are the planetary number assignments:\n\n";
	std::cout << "   1. Venus   2. Mars   3. Jupiter\n";
	std::cout << "   4. Saturn   5. Uranus  6. Neptune\n\n";

	std::cout << "Which planet do you plan on visiting? Please enter the number that matches the planet:\n";
	std::cin >> x;

	if (x == 1) {

		weight = weight * 0.78;

	}

	else if (x == 2) {

		weight = weight * 0.39;

	}

	else if (x == 2) {

		weight = weight * 2.65;

	}

	else if (x == 2) {

		weight = weight * 1.17;

	}

	else if (x == 2) {

		weight = weight * 1.05;

	}

	else if (x == 2) {

		weight = weight * 1.23;

	}

	std::cout << "\nYour weight is " << weight << ", good luck on your match!\n";

}