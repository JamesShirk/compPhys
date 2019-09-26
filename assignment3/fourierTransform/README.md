# Running the Program in Root

1. Locate libfftw3.so.3 file (sudo find / -name "libfftw3.so.3")
2. Start root (root -l)
3. link library (gSystem->Load("/path/to/libfftw3.so.3")
4. .L fourierTransform.cc
5. main()
