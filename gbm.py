import pylab as p
import numpy as np

#setup parameter
mu= 0.10;
sigma= 0.26;
S0= 39;
n_path= 1000;
n=n_partitions= 1000;

#create brownian paths
t=p.linspace(0,3, n+1);
dB=p.randn(n_path, n+1)/p.sqrt(n);
dB[:,0]=0;
B=dB.cumsum(axis=1);

#calculate stock prices
nu= mu - (sigma*sigma)/2.0
S= p.zeros_like(B);
S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#plot 5 realizations
p.xlabel('Time,$t$');
p.ylabel('Stock Prices');
p.title('5 realization of the GBM')
p.plot(t, S[0:5].transpose()); 
p.show();

#calculation
S3 = p.array(S[:,-1]);
print('expectation of S(3) = ', np.mean(S3));
print('variance of S(3) = ',np.var(S3));

w = S3>39.0;
x = sum(w)/len(w);
print('P[S(3)>39]=',x);
y = S3*w;
z = sum(y)/sum(w);
print('E[S(3)|S(3)>39]=',z);
