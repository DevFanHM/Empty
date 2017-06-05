#include <iostream>
using namespace std;
void main()
{
  for (int i = 0; i <= 101; i++)
  {
    for (int s = 0; s <= i; s++)
    {
      cout << s * i << endl;
    }
  }
}
