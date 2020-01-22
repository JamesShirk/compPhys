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
//void displayComplex(fftw_complex *y);
void fft(fftw_complex *in, fftw_complex *out);
void ifft(fftw_complex *in, fftw_complex *out);

int main(){
    const double pi = 3.1415926535897;
    fftw_complex y[N];
    fftw_complex out[N];
    // fftw_complex invOut[N];
    double xValues [N];
    double yValues [N];
    double x [N];
    double xx [N];
    // double invx [N];
    for (int i = 0; i < N; i++){
        //float input = ((i / 10.) - (((N / 10) / 2 )));
        float input = (i / 64.);
        xValues[i] = input;
	    yValues[i] =  haarFunction(input);
        y[i][REAL] = haarFunction(input);
        y[i][IMAG] = 0;
    }
    fft(y, out);
    ///ifft(out, invOut);

    for(int i = 0; i < N; i++){
        x[i] = sqrt(pow(out[i][REAL], 2) + pow(out[i][IMAG], 2));
        // invx[i] = invOut[i][REAL];
        if (xValues[i] != 0){
            //xx[i] = 2*pi/xValues[i];
            xx[i] = 1/xValues[i];
        } else {
            xx[i] = 0;
        }
    }

    // Plotting in root, a graphing package for C++
    // Makes a new TGraph with N points and I give it the address of the first value of the array and it fills the graph from there 
    // Graph in normal space
    TGraph *normalPlot = new TGraph(N, &xValues[0], &yValues[0]);
    normalPlot->GetXaxis()->SetTitle("X");
    normalPlot->GetYaxis()->SetTitle("Y");
    normalPlot->SetTitle("Plot of function in normal space not shifted.");
    normalPlot->Draw("AL");

    TCanvas *c2 = new TCanvas();
    TGraph *omega = new TGraph(N, &xx[0], &x[0]);
    omega->GetXaxis()->SetTitle("X");
    omega->GetYaxis()->SetTitle("Y");
    omega->SetTitle("Plot of function in normal space not shifted.");
    omega->SetMarkerStyle(6);
    omega->SetMarkerColor(4);
    omega->GetXaxis()->SetRangeUser(-10.0,10.0);
    omega->Draw("ALP");

    return 0;
}

int haarFunction(double x){
    if (x >= 1 && x < (1.5)){
        return 1;
    } else if (x >= (1.5) && x < 2){
        return -1;
    } else {
        return 0;
    }
}


void fft(fftw_complex *in, fftw_complex *out){
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    fftw_destroy_plan(p);
    fftw_cleanup();
}

// void ifft(fftw_complex *in, fftw_complex *out){
//     fftw_plan p;
//     p = fftw_plan_dft_1d(N, in, out, FFTW_BACKWARD, FFTW_ESTIMATE);
//     fftw_execute(p);
//     //fftw_one(plan, in, out);
//     fftw_destroy_plan(p);
//     fftw_cleanup();
//     for (int i = 0; i < N; ++i){
//         out[i][REAL] /= N;
//         out[i][IMAG] /= N;
//     }
// }

// void displayComplex(fftw_complex *y){
//     for (int i = 0; i < N; ++i){
//         if (y[i][IMAG] < 0){
//             cout << y[i][REAL] << " - " << abs(y[i][IMAG]) << "i" << endl;
//         } else {
//             cout << y[i][REAL] << " + " << y[i][IMAG] << "i" << endl;
//         }
//     }
// }
