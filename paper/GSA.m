function [xo,fo,time] = GSA(fun,x,l,u,qv,qa,Imax)
%% GSA find the optimum of a function by the Generalized Simulated Annealing Method
% Inputs: 
%        fun: objective function
%        x: initial guess for the optimum
%        l: lower bounds for the optimum
%        u: upper bounds for the optimum
%        qv: visiting parameter
%        qa: acceptance parameter
%        Imax: maximum number of iterations
% Outputs:
%        xo: solution vector
%        fo: objective function value at solution vector
%        time: calculation time

%% Example (see: https://www.mathworks.com/help/gads/isolated-global-minimum.html)
%f = @(x)-10*sech(norm(x(:)-x1)) -20*sech((norm(x(:)-x2))*3e-4) -1;
%This function has a global minimum: 1.0e+05 *[1.0000   -1.0000] with objective function value: -21. 
%The solution set up utilized for solving this function was:
%x0 = [0;0]
%l = [-1e6;-1e6]
%u = [1e6;1e6]
%[xo,fo,t] = GSA(f,x0,l,u,2.7,-5,500)

%% References:
%  [1] Tsallis, C., & Stariolo, D. A. (1996). Generalized simulated annealing. Physica A: Statistical Mechanics and its Applications, 233(1), 395-406.
%  [2] Mundim, K. C., & Tsallis, C. (1996). Geometry optimization and conformational analysis through generalized simulated annealing. International Journal of Quantum Chemistry, 58(4), 373-381.
%  [3] Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by simmulated annealing. science, 220(4598), 671-680.
%  [4] Szu, H., & Hartley, R. (1987). Fast simulated annealing. Physics letters A, 122(3-4), 157-162.
%  [5] Xiang, Y., & Gong, X. G. (2000). Efficiency of generalized simulated annealing. Physical Review E, 62(3), 4473.
%  [6] Schanze, T. (2006). An exact D-dimensional Tsallis random number generator for generalized simulated annealing. Computer physics communications, 175(11), 708-712.
%  [7] Xiang, Y., Gubian, S., Suomela, B., & Hoeng, J. (2013). Generalized simulated annealing for global optimization: the GenSA Package. R Journal, 5(1), 13-28.
%  [8] Won Y. Yang, Wenwu Cao, Tae-Sang Chung, John Morris, "Applied Numerical Methods Using MATLAB", John Whiley & Sons, 2005.

%% Author:
%          Jorge H. Wilches Visbal
%          Doctor of Science - Applied Physics in Medicine and Biology
%          University of Magdalena
%          Colombia
%% Contact:
%          email: jhwilchev@gmail.com

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Initializing the Algorithm %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tic
if nargin<7
   Imax = 400; %% Maximum number of iterations by default (It could be increased for very complex objective functions
   if nargin<6
       qa = -5;%% Acceptance parameter by default
   end
   if nargin<5
      qv = 2.7; %% Visiting parameter by default
   end
   if nargin<4
      l = []; u = []; %% Lower and upper bounds by default
   end
end

%% Input parameters
xo = x; fx = feval(fun,x); fo = fx; 
Dim = size(x); %Size of solution vector
if qv >= 3 || qv < 1
    error('Please enter a valid value for qv: 1 <= qv <= 3');
elseif qa < -5
    error('Please enter a valid value for qa: -5 <= qa <= -1');
end
k = physconst('Boltzmann'); %Boltzmann constant (1.38 x 10^-23 J/K)

%% External loop
for t = 1:Imax 
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Cooling Schedule [1][2]%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
Tqvo = Imax; %Initial visiting temperature
 if   qv == 1.00
      Tqv = Tqvo/log(1+t); %Visiting temperature for Classical Simulated Annealing (CSA)[3]
 elseif qv == 2.00 
      Tqv = Tqvo/(1+t);%Visiting temperature for Fast Simulated Annealing (FSA) [4]
 else 
      Tqv = Tqvo*((2^(qv-1))-1)/(((1+t)^(qv-1))-1); %Visiting temperature for Generalized Simulated Annealing (GSA) [1][2][5][6]
 end
 
 %% Acceptance temperature [7]
Tqa = Tqv/t; 
%% %%%%%%%%%%%%%%%%%%%%%%%%% Visiting Distribution of Tsallis %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for j = 1:Imax/5 %For each temperature Imax/5 points are tested to simulate the thermal equilibrium
%% For constrained problems
        if isempty(l) == 0 && isempty(u) == 0
            dx = Tsallis_rnd(qv,Tqv,Dim).*(u-l); %% Trial jump distance generated from Tsallis number generator [7]
            x1 = x + dx; %New solution generated
            x1 = (x1 < l).*l +(l <= x1).*(x1 <= u).*x1 +(u < x1).*u;% confine the generated solution to the admissible region bounded by l and u [8]
            
%% For unconstrained problems
        elseif isempty(l) == 1 && isempty(u) == 1
            dx = Tsallis_rnd(qv,Tqv,Dim);
            x1 = x + dx; 
        end
        
       %% %%%%%%%%%%%%%%%%%%%%%%%%%%% Evaluation of objective function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        fx1 = feval(fun,x1);%objective function value at x1
        df = (fx1 - fx);% Differences in objective function values 
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Probabilidade de Aceita��o %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Acceptance Probability [8]
        Pa = rand; %% Initial value of acceptance probability
        if  df < 0
            Pa = 1;
        elseif df>=0 && qa < 1 && 1/(1+(qa-1)*df/(k*Tqa)) <0
            Pa = 0;
        elseif df>=0 && 1/(1+(qa-1)*df/(k*Tqa)) > 0    
            Pa = 1/((1+(qa-1)*df/(k*Tqa))^(1/(qa-1)));
        end
        
%% Acceptance Probability Criterion [6][1]         
        if (df < 0 || Pa > rand) == 1 
            x = x1; fx = fx1; %
        end

%% Update of the solution vector
         if (fx < fo)
            xo = x; fo = fx1;
         end
    end
end
%% Calculation time
time = toc;
end

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Auxiliar Function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function Z = Tsallis_rnd(qv,Tqv,Dim)
%  D-dimensional Tsallis random number generator
%      Inputs:
%               qv: visiting parameter
%               Tqv: visiting temperature
%               Dim: dimension of solution vector
%      Outputs:
%               Z: Tsallis random numbers
%
%      References:
%               [1] Tsallis, C., & Stariolo, D. A. (1996). Generalized simulated annealing. Physica A: Statistical Mechanics and its Applications, 233(1), 395-406.
%               [2] Schanze, T. (2006). An exact D-dimensional Tsallis random number generator for generalized simulated annealing. Computer physics communications, 175(11), 708-712.
%               [3] Gaussianwaves.com - Signal Processing Simplified. Simulation and Analysis of White Noise in Matlab. Recuperado de: http://www.gaussianwaves.com/2013/11/simulation-and-analysis-of-white-noise-in-matlab/
%               [4] MathWorks (v2015a). Normally distributed random numbers. Recuperado de: http://www.mathworks.com/help/matlab/ref/randn.html
%               [5] MathWorks (v2015a). Random Numbers from Normal Distribution with Specific Mean and Variance https://www.mathworks.com/help/matlab/math/random-numbers-with-specific-mean-and-variance.html
%               [6] MathWorks (v2015a). Gamma random numbers. Recuperado de: http://www.mathworks.com/help/stats/gamrnd.html
% Author:
%          Jorge H. Wilches Visbal
%          Doctor of Science - Applied Physics in Medicine and Biology
%          University of S�o Paulo
%          Brazil
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Input parameters
n = (3-qv)/(qv-1);
s = sqrt(2*(qv-1))/(Tqv^(1/(3-qv)));
cov = (n*(qv-1)/(Tqv^(2/(3-qv))))^-1; %Covariance
mu = 0; %Mean
sigma = sqrt(cov);%Standard deviation
%% Independent and identical normal random numbers generator [3]
X = mu + sigma*randn(Dim);% iid normal numbers [4][5]
%% Chi-squared distribution random number generator
U = gamrnd(n/2,1);%gamma random number [6]
Y = s*sqrt(U);
%% Tsallis random number
Z = (X/Y);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% function [xo,fo,tempo] = GSA(f,x,l,u,qv,qa,Imax)
% %% M�todo de Recozimento Simulado Generalizado para minimizar uma fun��o f(x) com componentes restritas l <= xo <= u
% % ENTRADAS: 
% %        f: fun��o objetivo
% %        x: tentativa inicial de solu��o
% %        l: restri��es inferiores nas componentes do vetor solu��o
% %        u: restri��es superiores nas componentes do vetor solu��o
% %        qv: par�metro de visita��o
% %        qa: par�metro de aceita��o
% %        Imax: n�mero m�ximo de itera��es
% %SA�DAS:
% %        xo: vetor solu��o encontrado
% %        fo: valor da fun��o objetivo em xo
% 
% % Refer�ncias:
% %  [1] Tsallis, C., & Stariolo, D. A. (1996). Generalized simulated annealing. Physica A: Statistical Mechanics and its Applications, 233(1), 395-406.
% %  [2] Mundim, K. C., & Tsallis, C. (1996). Geometry optimization and conformational analysis through generalized simulated annealing. International Journal of Quantum Chemistry, 58(4), 373-381.
% %  [3] Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by simmulated annealing. science, 220(4598), 671-680.
% %  [4] Szu, H., & Hartley, R. (1987). Fast simulated annealing. Physics letters A, 122(3-4), 157-162.
% %  [5] Xiang, Y., & Gong, X. G. (2000). Efficiency of generalized simulated annealing. Physical Review E, 62(3), 4473.
% %  [6] Schanze, T. (2006). An exact D-dimensional Tsallis random number generator for generalized simulated annealing. Computer physics communications, 175(11), 708-712.
% %  [7] Won Y. Yang, Wenwu Cao, Tae-Sang Chung, John Morris, "Applied Numerical Methods Using MATLAB", John Whiley & Sons, 2005.
% %  [8] Xiang, Y., Gubian, S., Suomela, B., & Hoeng, J. (2013). Generalized simulated annealing for global optimization: the GenSA Package. R Journal, 5(1), 13-28.
% 
% % Autor:
% %          Jorge H. Wilches Visbal
% %          Doutor em Ci�ncias - F�sica aplicada � Medicina e Biologia
% %          Universidade de S�o Paulo
% %          Brasil
% %x = [x;y];
% tic
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Inicio do Programa%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% if nargin<7
%    Imax = 500;
%    if nargin<6
%        qa = -5;
%    end
%    if nargin<5
%        qv = 2.7;
%    end
%    if nargin<4
%        l = []; u = [];
%    end
% end
% 
% %% Par�metros de Entrada
% xo = x; fx = feval(f,x); fo = fx; %Estabele�a o vetor solu��o atual(xo) como sendo o vetor tentativa inicial x0
% Dim = size(x); %Dimens�es do vetor solu��o
% qv = qv + eps; 
% qa = qa + eps;
% if qv >= 3 || qv < 1
%     error('Please enter a valid value for qv: 1 <= qv <= 3');
% elseif qa < -5
%     error('Please enter a valid value for qa: -5 <= qa <= -1');
% end
% k = physconst('Boltzmann'); %Constante de Boltzmann (1.38 x 10^-23 J/K)
% %% Inicio do Bucle 
% for t = 1:Imax 
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Esquema de resfriamento da temperatura no GSA [1][2]%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% %% Par�metros iniciais para as temperaturas
% Tqvo = Imax; %temperatura de visita��o inicial
% %% Esquema de resfriamento para a temperatura de visita��o (Tqv)
%  if     qv == 1.00 + eps
%       Tqv = Tqvo/log(1+t); %temperatura de visita��o (CSA): Classical Simulated Annealing [3]
%  elseif qv == 2.00 + eps
%       Tqv = Tqvo/(1+t);%temperatura de visita��o (FSA): Fast Simulated Annealing [4]
%  else 
%       Tqv = Tqvo*((2^(qv-1))-1)/(((1+t)^(qv-1))-1);%temperatura de visita��o (GSA): Generalized Simulated Annealing [1][2][5][6]
%  end
% %% Esquema de resfriamento para a temperatura de aceita��o (Tqa)[8]
% Tqa = Tqv/t;
% %% %%%%%%%%%%%%%%%%%%%%%%%%% Distribui��o de Visita��o de Tsallis - GSA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     for j = 1:Imax/5; %Para cada temperatura s�o Imax/2 pontos de teste para simular o equilibrio t�rmico
% %% Com restri��es nas componentes do vetor solu��o
%         if isempty(l) == 0 && isempty(u) == 0
%         dx = Tsallis_rnd(qv,Tqv,Dim).*(u-l);
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Mudan�a Configuracional%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%             x1 = x + dx; %Novo estado gerado a partir da mudan�a (Z) aleat�ria do estado atual(x).
%             x1 = (x1 < l).*l +(l <= x1).*(x1 <= u).*x1 +(u < x1).*u;%Garante que o novo ponto esteja dentro das restri��es estabelecidas [7]
%             
% %% Sem restri��es nas componentes do vetor solu��o
% 
%         elseif isempty(l) == 1 && isempty(u) == 1
%             dx = Tsallis_rnd(qv,Tqv,Dim);
%             x1 = x + dx; %Novo estado gerado a partir da mudan�a (Z) aleat�ria do estado atual(x).
%         end
%        
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Avalia��o da fun��o objetivo (f) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%         fx1 = feval(f,x1);%valor da fun��o objetivo em x1
%         df = (fx1 - fx);%Diferen�a no valor da fun��o quando avaliada em x e x1 --> Probabilidade de aceita��o = 1
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Probabilidade de Aceita��o %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %% Criterio Generalizado para GSA [1]
%         Pa = 0; %% Valor inicial de Pa
%         if  df < 0
%             Pa = 1;
%         elseif df >= 0 && (1-(1-qa)*(df/(k*Tqa))) > 0
%             Pa = (1-(1-qa)*(df/(k*Tqa)))^(1/(1-qa)); %%1/((1+(qa-1)*df/(1*Tqa))^(1/(qa-1)));
%         elseif qa < 1 && ((1-(1-qa)*(df/(k*Tqa)))) < 0 %% (1/((1+(qa-1)*df/(1*Tqa)))) < 0 %%
%             Pa = 0;
%         end
%         
% %% Criterio Probabilidade de Aceita��o
%          
%          if (df < 0 || rand < Pa) == 1 %Caso df negativa (x1 diminui o valor da FO) ou a probabilidade de aceita��o for m do que um valor aleat�rio entre 0 e 1
%              x = x1; fx = fx1; %O novo vetor � aceito como solu��o (atualiza-se o esquema)
%          end
% 
% %% Atualiza��o do vetor solu��o        
%          if (fx < fo)%Se o ponto atual for maior do que a atual solu��o, a solu��o � atualizada
%             xo = x; fo = fx1;
%          end
%     end
% %% Valor m�nimo que Tqv pode adquirir
% %     if Tqv < 0.1
% %         break
% %     end
% %   
% end
% %% Tempo de C�lculo
% tempo = toc;
% end
% 
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Fun��o Auxiliar %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% function Z = Tsallis_rnd(qv,Tqv,Dim)
% % Gerador de n�meros aleat�rios Tsallis de dimens�o D [1][2]
% %      Entradas:
% %               qv: par�metro de visita��o
% %               Tqv: temperatura de visita��o
% %               Dim: dimens�es do vetor solu��o
% %      Sa�das:
% %               Z: vetor n�meros aleat�rios Tsallis de dimsens�o D
% %
% %      Refer�ncias:
% %               [1] Tsallis, C., & Stariolo, D. A. (1996). Generalized simulated annealing. Physica A: Statistical Mechanics and its Applications, 233(1), 395-406.
% %               [2] Schanze, T. (2006). An exact D-dimensional Tsallis random number generator for generalized simulated annealing. Computer physics communications, 175(11), 708-712.
% %               [3] Gaussianwaves.com - Signal Processing Simplified. Simulation and Analysis of White Noise in Matlab. Recuperado de: http://www.gaussianwaves.com/2013/11/simulation-and-analysis-of-white-noise-in-matlab/
% %               [4] MathWorks (v2015a). Normally distributed random numbers. Recuperado de: http://www.mathworks.com/help/matlab/ref/randn.html
% %               [5] MathWorks (v2015a). Random Numbers from Normal Distribution with Specific Mean and Variance https://www.mathworks.com/help/matlab/math/random-numbers-with-specific-mean-and-variance.html
% %               [6] MathWorks (v2015a). Gamma random numbers. Recuperado de: http://www.mathworks.com/help/stats/gamrnd.html
% %      Autor:
% %          Jorge H. Wilches Visbal
% %          Doutor em F�sica Aplicada � Medicina e Biologia
% %          Universidade de S�o Paulo
% %          Brasil
% %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %% Par�metros de entrada
% n = (3-qv)/(qv-1);
% s = sqrt(2*(qv-1))/(Tqv^(1/(3-qv)));
% cov = (n*(qv-1)/(Tqv^(2/(3-qv))))^-1; %Covarian�a
% mu = 0; %M�dia
% sigma = sqrt(cov);%Desvio padr�o
% %% Gerar n�meros aleat�rios independentes e id�nticos de uma distribui��o normal[3]
% X = mu + sigma*randn(Dim);%n�meros aleat�rios normais iid[4][5]
% %% Gerar um n�mero aleat�rio de uma distribui��o qui-quadrado
% U = gamrnd(n/2,1);%n�mero aleat�rio gamma (forma,escala)[6]
% Y = s*sqrt(U);
% %% Gerador de n�meros aleat�rios[3] para o m�todo de recozimento simulado generalizado[1]
% Z = (X/Y);
% end