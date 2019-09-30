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
#define N 640

using namespace std;

double sinc(double x);
void displayComplex(fftw_complex *y);
void fft(fftw_complex *in, fftw_complex *out);
void ifft(fftw_complex *in, fftw_complex *out);

int main(){
    const double pi = 3.1415926535897;
    fftw_complex y[N];
    fftw_complex out[N];
    fftw_complex outInv[N];
    double xValues [N];
    double yValues [N];
    double x [N];
    double xinv [N];
    double time [N];
    for (int i = 0; i < N; i++){
        float input = (i / 64.) - 5.0;
        xValues[i] = input;
	    yValues[i] = sinc(input);
        y[i][REAL] = sinc(input);
        y[i][IMAG] = 0;
    }
    ifft(y, out);
    fft(out, outInv);

    // displayComplex(out);

    for(int i = 0; i < N; i++){
        x[i] = sqrt(pow(out[i][REAL], 2) + pow(out[i][IMAG], 2));
        if (xValues[i] == 0){
            time[i] = 0;
        } else{
            time[i] = (2. * pi) / xValues[i];
            printf("time being filled with %g\n", time[i]);
        }
        xinv[i] = outInv[i][REAL];
    }

    // Plotting in root, a graphing package for C++
    // Makes a new TGraph with N points and I give it the address of the first value of the array and it fills the graph from there 
    // Graph in normal space
    TGraph *start = new TGraph(N, &xValues[0], &yValues[0]);
    start->GetXaxis()->SetTitle("X");
    start->GetYaxis()->SetTitle("Y");
    start->SetTitle("Plot of function fourier space.");
    start->GetXaxis()->SetRangeUser(-10,10);
    start->GetYaxis()->SetRangeUser(-1,1.5);
    start->Draw("AL");

    TCanvas *c2 = new TCanvas();
    TGraph *inversed = new TGraph(N, &time[0], &x[0]);
    inversed->GetXaxis()->SetTitle("X");
    inversed->GetYaxis()->SetTitle("Y");
    inversed->SetTitle("Plot of function in normal space.");
    inversed->SetMarkerStyle(6);
    inversed->SetMarkerColor(4);
    inversed->GetXaxis()->SetRangeUser(-10,10);
    inversed->Draw("ALP");

    TCanvas *c3 = new TCanvas();
    TGraph *fuck = new TGraph(N, &xValues[0], &xinv[0]);
    fuck->GetXaxis()->SetTitle("X");
    fuck->GetYaxis()->SetTitle("Y");
    fuck->SetTitle("Plot of function in fourier space.");
    fuck->SetMarkerStyle(6);
    fuck->SetMarkerColor(4);
    fuck->GetXaxis()->SetRangeUser(-10,10);
    fuck->Draw("AP");

    return 0;
}

double sinc(double x){
    if (x != 0){
        return (sin(x) / x);
    } else {
        return 1;
    }
}


void fft(fftw_complex *in, fftw_complex *out){
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    fftw_destroy_plan(p);
    fftw_cleanup();
}

void ifft(fftw_complex *in, fftw_complex *out){
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_BACKWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    fftw_destroy_plan(p);
    fftw_cleanup();
    for (int i = 0; i < N; ++i){
        out[i][REAL] /= N;
        out[i][IMAG] /= N;
    }
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
