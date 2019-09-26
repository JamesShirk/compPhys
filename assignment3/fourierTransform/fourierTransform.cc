// September 25 James Shirk for fourier transform of piecewise function
// Fourier transform to be performed with FFTW
// Going to attempt to plot with root

#include <fftw3.h> //for fourier transform
#include <vector>  //vectors for storing values
#include <stdio.h> //for i/o
#include <string>  //for strings lol
#include <math.h>
#include <iostream> // for cout

#define REAL 0
#define IMAG 1
#define N 256

using namespace std;

int haarFunction(double x);
void displayComplex(fftw_complex *y);
void fft(fftw_complex *in, fftw_complex *out);

int main(){
    fftw_complex y[N];
    fftw_complex out[N];
    float xValues [N] = {0};
    for (int i = 0; i < N; i++){
        float input = ((i / 10.) - 12.8);
        xValues[i] = input;
        input = haarFunction(input);
        y[i][REAL] = input;
        y[i][IMAG] = 0;
    }
    // vector <double> yValues = functionValues(-12.8, 12.6, .1, "y");
    // vector <double> xValues = functionValues(-12.8, 12.6, .1, "x");
    fft(y, out);
    printf("FFT = \n");
    displayComplex(out);

    TGraph *normalPlot = new TGraph(N, &xValues[0], &y[0][REAL]);
    normalPlot->GetXaxis()->SetTitle("X");
    normalPlot->GetYaxis()->SetTitle("Y");
    normalPlot->SetTitle("Plot of function in normal space not shifted.");
    normalPlot->Draw("AL");

    TGraph *fourierTransform = new TGraph(N, &out[0][REAL], &out[0][IMAG]);
    fourierTransform->GetXaxis()->SetTitle("Real");
    fourierTransform->GetYaxis()->SetTitle("Imaginary");
    fourierTransform->SetTitle("Plot of function in fourier not shifted.");
    fourierTransform->Draw("AL");

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