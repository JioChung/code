// Created on iPad.

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

//三元组
struct Node{
    int x;
    int y;
    int data;
};

int main() {
    ifstream fin;
    fin.open("code/c++/matrix compression/input-UpperTriangular.txt");
    if(!fin.is_open()){
        cout<<"open file fail"<<endl;
    }
    char buff[1024] = {0};
    while(fin.getline(buff, sizeof(buff))){
        for(char c : buff)  
            cout<<c;
        cout<<strlen(buff)<<endl;
    }

    fin.close();
    return 0;
}