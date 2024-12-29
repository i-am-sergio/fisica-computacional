function [xmin,fval] = RPS(d,T,n)
%% Função Objetivo 
 fun = @(x)norm(x(4).*(((x(1)*x(2))./((d + x(1)).*(d +x(2)))).^x(3)).*exp(-0.15002*d)+(1-x(4))*(0.2880*exp(-0.2897*d)+0.5000*exp(-0.2807*d)+0.1690*exp(-0.2417*d)+0.0430*exp(-0.2342*d)) - T)^2;
 %%  Loop
 for i = 1:n;
 %% Tentativa inicial
 x0 = [rand;rand;rand;rand];
 %x0 = [0;0;0;0];
 %% Resolvedor
options = optimset('Algorithm','sqp','Maxiter',1e6,'MaxFunEvals',1e6,'TolFun',1e-5);
[x,fval] = fmincon(fun,x0,[],[],[],[],[0;0;0;0],[10;10;10;10],[],options);
 vfval(:,i) = fval; %vetor que armazena os valores da função objetivo a cada iteração i
 vx(:,i)= x; %vetor que armazena os valores dos parâmetros a cada iteração i
 end
 [~,Imin] = min(vfval);
 fval = vfval(:,Imin);
 xmin = vx(:,Imin);
%Encontrar mínimo global com GlobalSearch
%     opts = optimoptions(@fmincon,'Algorithm','interior-point','TolFun',TolFun);
%     problem = createOptimProblem('fmincon','objective',...
%      fun,'x0',E_0,'lb',lb,'ub',ub,'options',options);
%     gs = GlobalSearch('PlotFcns',@gsplotbestf,'NumTrialPoints',1e5,'MaxTime',300,'TolFun',TolFun);
%     rng(14,'twister') %para reprodutbilidade
%     [E_fmincon,fval] = run(gs,problem);
%     Peso = E_fmincon;%/max(E_fmincon);
 