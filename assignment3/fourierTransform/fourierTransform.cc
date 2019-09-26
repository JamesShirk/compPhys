// September 25 James Shirk for fourier transform of piecewise function
// Fourier transform to be performed with FFTW
// Going to attempt to plot with root

#include <fftw3.h> //for fourier transform
#include <vector>  //vectors for storing values
#include <stdio.h> //for i/o
#include <string>  //for strings lol
#include <iostream> // for cout

#define REAL 0
#define IMAG 1
#define N 256

using namespace std;

vector<double> functionValues(double lowerBound, double upperBound, double division, string type);
int haarFunction(double x);
void displayComplex(fftw_complex *y);
void fft(fftw_complex *in, fftw_complex *out);

int main(){
    fftw_complex y[N];
    fftw_complex out[N];
    for (int i = 0; i < N; i++){
        float input = ((i / 10.) - 12.8);
        input = haarFunction(input);
        y[i][REAL] = input;
        y[i][IMAG] = 0;
    }
    // vector <double> yValues = functionValues(-12.8, 12.6, .1, "y");
    // vector <double> xValues = functionValues(-12.8, 12.6, .1, "x");
    fft(y, out);
    printf("FFT = \n");
    displayComplex(y);
    return 0;
}

int haarFunction(double x){
    if (x >= 0 && x < (.5)){
        return 1;
    } else if (x >= (.5) && x < 1){
        return -1;
    } else {
        return 0;
    }
}

vector<double> functionValues(double lowerBound, double upperBound, double division, string type){
    vector<double> Values;
    double a = lowerBound;
    while(a <= (upperBound + division)){
        if (type =="y"){
            Values.push_back(haarFunction(a));
        } else if (type == "x"){
            Values.push_back(a);
        } else {
            printf("Please input either x or y for type");
            Values.push_back(0);
            return Values;
        }
        a += division;
    }
    return Values;
}

void fft(fftw_complex *in, fftw_complex *out){
    fftw_plan plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(plan);
    fftw_destroy_plan(plan);
    fftw_cleanup();
}

void displayComplex(fftw_complex *y){
    for (int i = 0; i < N; ++i){
        if (y[i][IMAG] < 0){
            cout << y[i][REAL] << " - " << abs(y[i][IMAG]) << "i" << endl;
        } else {
            cout << y[i][REAL] << " + " << y[i][IMAG] << "i" << endl;
        }
    }
}