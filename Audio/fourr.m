%Part 6
n=256;

hw=hann(length(sumsig)); %hann window
hw=hw'; %transpose
sig4=conv(sumsig,hw);
Y = fft(sig4,n);
Y=abs(Y/n);
P2 = abs(Y/n);
P1 = P2(1:n/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(n/2))/n;


figure
%Plot hann window | 256 fft
plot(f,P1);
xlabel('Frequency');
ylabel('Amplitude');
title('FFT Magnitude | hann window | N=256');


n=512;
Y = fft(sig4,n);
Y=abs(Y/n);
P2 = abs(Y/n);
P1 = P2(1:n/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(n/2))/n;
figure

%Plot hann window | 512 fft

plot(f,P1);
xlabel('Frequency Hz');
ylabel('Amplitude');
title('FFT Magnitude | hann window | N=512');

n=1024;
Y = fft(sig4,n);
Y=abs(Y/n);
P2 = abs(Y/n);
P1 = P2(1:n/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(n/2))/n;
figure

%Plot hann window | 1024 fft

plot(f,P1);
xlabel('Frequency Hz');
ylabel('Amplitude');
title('FFT Magnitude | hann window | N=1024');

n=2048;
Y = fft(sig4,n);
Y=abs(Y/n);
P2 = abs(Y/n);
P1 = P2(1:n/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(n/2))/n;
figure

%Plot hann window | 2048 fft

plot(f,P1);
xlabel('Frequency Hz');
ylabel('Amplitude');
title('FFT Magnitude | hann window | N=2048');
