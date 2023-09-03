%Part 2

N = 2000;
x = [0:100]/50;
f = ones(1,101)*1/2;
for i = 1:2:N
a = 1/pi/i;
f = f+ a*sin(2*pi*i*x);
end
plot(x,f)
xlabel ("Time");
ylabel ("Frequency");

