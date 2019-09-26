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
void ifft(fftw_complex *in, fftw_complex *out);

int main(){
    fftw_complex y[N];
    fftw_complex out[N];
    fftw_complex invOut[N];
    double xValues [N];
    double yValues [N];
    double x [N];
    double invx [N];
    for (int i = 0; i < N; i++){
        float input = ((i / 10.) - 12.8);
        xValues[i] = input;
        input = haarFunction(input);
	    yValues[i] = input;
        y[i][REAL] = input;
        y[i][IMAG] = 0;
    }
    fft(y, out);
    ifft(out, invOut);

    for(int i = 0; i < N; i++){
        x[i] = out[i][REAL];
        invx[i] = invOut[i][REAL];
    }


    // Plotting in root, a graphing package for C++
    // Makes a new TGraph with N points and I give it the address of the first value of the array and it fills the graph from there 
    // Graph in normal space
    TGraph *normalPlot = new TGraph(N, &xValues[0], &yValues[0]);
    normalPlot->GetXaxis()->SetTitle("X");
    normalPlot->GetYaxis()->SetTitle("Y");
    normalPlot->SetTitle("Plot of function in normal space not shifted.");
    normalPlot->Draw("AL");

    // Graph in imaginary space
    TCanvas *c2 = new TCanvas();
    TGraph *fourierTransform = new TGraph(N, &out[0][REAL], &out[0][IMAG]);
    fourierTransform->GetXaxis()->SetTitle("Real");
    fourierTransform->GetYaxis()->SetTitle("Imaginary");
    fourierTransform->SetTitle("Plot of function in fourier not shifted.");
    fourierTransform->SetMarkerStyle(8);
    fourierTransform->SetMarkerColor(4);
    fourierTransform->Draw("APL");

    // Graph in imaginary space
    TCanvas *c3 = new TCanvas();
    TGraph *fourierTransform2 = new TGraph(N, &xValues[0], &x[0]);
    fourierTransform2->GetXaxis()->SetTitle("Real");
    fourierTransform2->GetYaxis()->SetTitle("Imaginary");
    fourierTransform2->SetTitle("Plot of function in fourier not shifted.");
    fourierTransform2->SetMarkerStyle(8);
    fourierTransform2->SetMarkerColor(4);
    fourierTransform2->Draw("APL");


    TCanvas *c4 = new TCanvas();
    TGraph *inversed = new TGraph(N, &xValues[0], &invx[0]);
    normalPlot->GetXaxis()->SetTitle("X");
    normalPlot->GetYaxis()->SetTitle("Y");
    normalPlot->SetTitle("Plot of function in normal space not shifted.");
    normalPlot->Draw("AL");

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
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    //fftw_one(plan, in, out);
    fftw_destroy_plan(p);
    fftw_cleanup();
}

void ifft(fftw_complex *in, fftw_complex *out){
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_BACKWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    //fftw_one(plan, in, out);
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
