// September 25 James Shirk for fourier transform of piecewise function
// Fourier transform to be performed with FFTW
// Going to attempt to plot with root

#include <fftw3.h>  //for fourier transform
#include <stdio.h>  //for printf
#include <math.h>   //for sin, pow, and sqrt
#include <chrono>   //time function
#include <iostream> // for cout

// for use with fftw_complex data type, 2D array where real is [i][0] and imag is [i][1]
// N is number of samples over range -5 to 5
// Time loops is defined as the number of times to run the ifft to get a good time average.

#define REAL 0
#define IMAG 1
#define N 64
#define timeLoops 1000

using namespace std;

// Function prototypes
double sinc(double x);
void displayComplex(fftw_complex *y);
void fft(fftw_complex *in, fftw_complex *out);
void ifft(fftw_complex *in, fftw_complex *out);

int main(){
    // Define const (unchangeable variable) for pi
    const double pi = 3.1415926535897;
    // Assumed normalization factor
    const double normalization = pi;
    // Defines the 2D fftw arrays y, the input, out, the ifft output, and outInv, the fft of the ifft
    fftw_complex y[N];
    fftw_complex out[N];
    fftw_complex outInv[N];
    // others arrays with N values used
    // xValues is for the original omega values used, y values is the original function, y original function using fftw_complex 2D array
    // yinv is the the ifft of fft y values, time is the x axis in real (not fourier) space
    double xValues [N];
    double yValues [N];
    double yMag [N];
    double yinv [N];
    double time [N];
    for (int i = 0; i < N; i++){
        // makes 64 points from -5 to 5 with spacing equal to 10 / 64
        float input = (i / 6.4) - 5.0;
        // Commented out parts were used for time scaling
        // input /= 2;
        xValues[i] = input;
	    // yValues[i] = (1.0/2.0) * sinc(input);
        // y[i][REAL] = (1.0/2.0) * sinc(input);
	    yValues[i] = sinc(input);
        y[i][REAL] = sinc(input);
        y[i][IMAG] = 0;
    }

    // Define the data for finding the time to run the function
    chrono::time_point<std::chrono::high_resolution_clock> t1;
    chrono::time_point<std::chrono::high_resolution_clock> t2;
    std::chrono::duration<double, std::micro> timeMicro;

    for(int i = 0; i < timeLoops; i++){
        // Takes time before running in clock cycles
        t1 = chrono::high_resolution_clock::now();
        // CHANGE THE TOLERANCE AND BISECTION ITERATIONS HERE
        ifft(y, out);
        // Takes time after running 
        t2 = chrono::high_resolution_clock::now();
        // Sums the delta time over 100 runs
        timeMicro += (t2 -t1);
    }

    // divides the time by the number of times the function ran and outputs it
    timeMicro /= timeLoops;
    cout << "The average time elapsed for this function is " << timeMicro.count() <<" microseconds." << endl;

    // Compute the inverse of sinc(x)
    fft(out, outInv);

    // for each point, puts the magnitude into yMag, and puts either 0 for 0 (to avoid inf errors) or 2pi/ x (assuming that the original is omega) to calculate time
    // the value for the 'real' x axis
    for(int i = 0; i < N; i++){
        yMag[i] = sqrt(pow(normalization * out[i][REAL], 2) + pow(normalization * out[i][IMAG], 2));
        if (xValues[i] == 0){
            time[i] = 0;
        } else{
            // 2. * for normal, 4. * for time scaled by 2
            time[i] = (2. * pi) / xValues[i];
            //time[i] = (4. * pi) / xValues[i];
            //printf("time being filled with %g\n", time[i]);
        }
        yinv[i] = outInv[i][REAL];
    }

    // Plotting in root, a graphing package for C++
    // Makes a new TGraph with N points and I give it the address of the first value of the array and it fills the graph from there 
    // Graph in Fourier space
    TGraph *start = new TGraph(N, &xValues[0], &yValues[0]);
    start->GetXaxis()->SetTitle("Omega");
    start->GetYaxis()->SetTitle("sinc(x)");
    start->SetTitle("Plot of function fourier space.");
    start->GetXaxis()->SetRangeUser(-10,10);
    start->Draw("ALP");

    // Graph in real space , inverse fourier transform calculated
    TCanvas *c2 = new TCanvas();
    TGraph *inversed = new TGraph(N, &time[0], &yMag[0]);
    inversed->GetXaxis()->SetTitle("t");
    inversed->GetYaxis()->SetTitle("Magnitude");
    inversed->SetTitle("Plot of function in normal space (After inverse Fourier transform).");
    inversed->SetMarkerStyle(6);
    inversed->SetMarkerColor(4);
    inversed->GetXaxis()->SetRangeUser(-10,10);
    inversed->Draw("ALP");

    // fft of ifft plotter
    TCanvas *c3 = new TCanvas();
    TGraph *ftofift = new TGraph(N, &xValues[0], &yinv[0]);
    ftofift->GetXaxis()->SetTitle("omega");
    ftofift->GetYaxis()->SetTitle("sinc(x)");
    ftofift->SetTitle("Function inversed and then transformed back");
    ftofift->SetMarkerStyle(6);
    ftofift->SetMarkerColor(4);
    ftofift->GetXaxis()->SetRangeUser(-10,10);
    ftofift->Draw("ALP");

    return 0;
}

// given function
double sinc(double x){
    if (x != 0){
        return (sin(x) / x);
    } else {
        return 1;
    }
}

// main function for calculating ffts, takes in a fftw_complex and puts one out, channging FFTW_FORWARD to FFTW_BACKWARD computes the ifft
void fft(fftw_complex *in, fftw_complex *out){
    fftw_plan p;
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);
    fftw_destroy_plan(p);
    fftw_cleanup();
}

// main function for calculating ffts, takes in a fftw_complex and puts one out
// Must scale down each values of the output by N due to how fftw computes the transform
void ifft(fftw_complex *in, fftw_complex *out){
    const double pi = 3.1415926535897;
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

// allows you to view each element of the fftw_complex 2D array in a + bi format
void displayComplex(fftw_complex *y){
    for (int i = 0; i < N; ++i){
        if (y[i][IMAG] < 0){
            printf("%g - %gi\n", y[i][REAL], abs(y[i][IMAG]));
        } else {
            printf("%g + %gi\n", y[i][REAL], y[i][IMAG]);
        }
    }
}
