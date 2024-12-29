%% %% GSA FOTONES BAJA ENERGIA
function [E,F,Er] = RPS(Eo,dE,Ef,Energia,um,de,T,nomect,nomesp)
%% Función Reconstrucción de Espectros de Energía de Rayos X

%% Salidas
%E: Energia del Espectro
%F: Espectro de Energía Reconstruído
%Er: Error relativo entre la Capa Semirreductora de T y la Capa
%Semirreductora del Espectro

%% Entradas
%Eo: Energía Inicial del Vector Energía del Espectro
%dE: Intervalo de Energía del Vector Energía del Espectro
%Ef: Energía Final del Vector Energía del Espectro
%um: Coeficiente Másico de Atenuación
%Energia: Vector Energía del Coeficiente Másico de Atenuación
%T: Curva de Transmisión Medida Experimentalmente
%de: Vector Espesor asociado a T
%n: Número de Ejecuciones del Algoritmo de Ajuste a T
%nomect: Nombre Acuñado a la Curva de Transmisión
%nomesp: Nombre Acuñado al Espectro Reconstruído

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Inicio del Algoritmo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tic; %Contador de tiempo;
timerval = tic;
%% Espesor (cm2/g)
d = 2.7*0.1*de;

%% Parametrización del coeficiente de atenuación másico
El = log10(Energia);
uml = log10(um);
fo = fitoptions('Method','NonlinearLeastSquares','StartPoint',[0,0,0,0,0,0]);        
exeqn = fittype('a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 + a5*x^5','options',fo);
[f,~] = fit(El,uml,exeqn); %% curva de ajuste com valores em f
c = coeffvalues(f); %extrai os coeficientes de f
%r2 = extractfield(goff,'rsquare'); %coeficiente de determinação do ajuste

%% Bucle
Er = 10;
if Ef == 80
    um0 = 0.20;
elseif Ef == 120
    um0 = 0.15;
end
r = 1;
er = 2;
pe = 2;
while Er > 1 || pe > 1 %|| r < 0.5 
    
%% Função Objetivo 
%fun = @(x)norm(T - (x(4).*(((x(1)*x(2))./((d + x(1)).*(d + x(2)))).^x(3)).*exp(-0.200053733*d) + (1-x(4))*(0.2880*exp(-0.2897*d)+0.5000*exp(-0.2807*d)+0.1690*exp(-0.2417*d)+0.0430*exp(-0.2342*d))))^2;
fun = @(x)norm(T - (x(4).*(((x(1)*x(2))./((d + x(1)).*(d + x(2)))).^x(3)).*exp(-um0*d) + (1-x(4))*(0.2880*exp(-0.2897*d)+0.5000*exp(-0.2807*d)+0.1690*exp(-0.2417*d)+0.0430*exp(-0.2342*d))))^2;
%% Tentativa inicial
x0 = [rand;rand;rand;rand];
%x0 = [1;1;1;1];
%% Solucionador
ls = [10;0.99;.99;0.99];
li = [0;0;0;0];

[x,fval] = GSA(fun,x0,li,ls,2.7,-5,200);

%% Ajuste da Curva pela Equação de Transmissão 
d1 = 2.7*0.1*(0:0.001:max(de));
T1 = x(4).*(((x(1)*x(2))./((d1 + x(1)).*(d1 +x(2)))).^x(3)).*exp(-um0*d1)+(1-x(4))*(0.2880*exp(-0.2897*d1)+0.5000*exp(-0.2807*d1)+0.1690*exp(-0.2417*d1)+0.0430*exp(-0.2342*d1)); 


%% Ajuste Opcional
fo = fitoptions('Method','NonlinearLeastSquares','StartPoint',[0,0,0]);        
exeqn = fittype('a + b*exp(-u*x)','options',fo);
%d = 2.7*0.1*d;
[f,goff] = fit(d,T,exeqn); %% curva de ajuste com valores em f
csw = coeffvalues(f); %extrai os coeficientes de f
r2 = extractfield(goff,'rsquare'); %coeficiente de determinação do ajuste
E = csw(1) + csw(2)*exp(-csw(3)*d1);
[~,Ict] = min(abs(E - 0.5));
CSRct = d1(Ict);
%figure
%plot(d,T,'*k',d1,E,'b')

%% Parámetros de Ajuste de la Ecuación de Transmisión
disp('Parámetros de la Ecuación de Ajuste')
a = round(x(1),3); b = round(x(2),3); v = round(x(3),3);r = round(x(4),3);
%a = 3.394; b = 0.66;   v = 0.711;   r = 0.855;
%a = 7.893; b = 0.594; v = 0.506; r =0.565;
Coeficientes = table(a,b,v,r);
disp(Coeficientes)
fprintf('Fval = %1.3e           \n',fval');

pe = errperf(E,T1,'mspe');
%% Capa Semirreductora de la Curva de Transmisión
[~,Ict] = min(abs(T1 - 0.5));
CSRct = d1(Ict);
disp('Capa Semirreductora de la Curva de Transmisión')
fprintf('CSRct(cm^2/g) = %1.3f           \n',CSRct');

%% Vector Energía
E = Eo:dE:Ef;
%% Coeficientes másicos de atenuación
% um = 10.^(c(1) + c(2)*log10(E) + c(3)*log10(E).^2 + c(4)*log10(E).^3 + c(5)*log10(E).^4 + c(6)*log10(E).^5); %% um para cualquier energía
% um0 = 10.^(c(1) + c(2)*log10(Ef) + c(3)*log10(Ef)^2 + c(4)*log10(Ef)^3 + c(5)*log10(Ef)^4 + c(6)*log10(Ef)^5); %% para la energía máxima del haz
% dUmdE = -10.^((1711038796208681*log(E).^2)./(281474976710656*log(10).^2) - (7582987874194015*log(E).^3)./(1125899906842624*log(10).^3) + (1770029823850551*log(E).^4)./(562949953421312*log(10).^4) - (4472050037836217*log(E).^5)./(9007199254740992*log(10).^5) - (5700642108543685*log(E))./(1125899906842624*log(10)) + 2529650956514345./562949953421312).*log(10).*(5700642108543685./(1125899906842624*E*log(10)) - (1711038796208681.*log(E))./(140737488355328.*E.*log(10).^2) + (22748963622582045.*log(E).^2)./(1125899906842624.*E.*log(10).^3) - (1770029823850551.*log(E).^3)./(140737488355328.*E.*log(10).^4) + (22360250189181085.*log(E).^4)./(9007199254740992.*E.*log(10).^5));
% 
% % Espectro de Energia del Haz de Rayos X
% Fb = (r*(sqrt(pi)*(a*b)^2)/gamma(v)).*(((um - um0)/(a-b)).^(v-0.5)).*exp(-0.5*(a+b).*(um - um0)).*besseli(v-0.5,(0.5*(a-b)*(um-um0)),1).*(0.5*(a-b).*(um - um0)).*(-dUmdE); 
% Fc = (1-r)*(0.2880*KronD(E,57.98)+0.5*KronD(E,59.32)+0.1690*KronD(E,67.20)+0.0430*KronD(E,69.10));

um = 10.^(c(1) + c(2)*log10(E) + c(3)*log10(E).^2 + c(4)*log10(E).^3 + c(5)*log10(E).^4 + c(6)*log10(E).^5); %% um para cualquier energía
um0 = 10.^(c(1) + c(2)*log10(Ef) + c(3)*log10(Ef)^2 + c(4)*log10(Ef)^3 + c(5)*log10(Ef)^4 + c(6)*log10(Ef)^5); %% para la energía máxima del haz
dUmdE = -10.^((1711038796208681*log(E).^2)./(281474976710656*log(10).^2) - (7582987874194015*log(E).^3)./(1125899906842624*log(10).^3) + (1770029823850551*log(E).^4)./(562949953421312*log(10).^4) - (4472050037836217*log(E).^5)./(9007199254740992*log(10).^5) - (5700642108543685*log(E))./(1125899906842624*log(10)) + 2529650956514345./562949953421312).*log(10).*(5700642108543685./(1125899906842624*E*log(10)) - (1711038796208681.*log(E))./(140737488355328.*E.*log(10).^2) + (22748963622582045.*log(E).^2)./(1125899906842624.*E.*log(10).^3) - (1770029823850551.*log(E).^3)./(140737488355328.*E.*log(10).^4) + (22360250189181085.*log(E).^4)./(9007199254740992.*E.*log(10).^5));

%% Espectro de Energia del Haz de Rayos X
Fb = (r*(sqrt(pi)*(a*b)^2)/gamma(v)).*(((um - um0)/(a-b)).^(v-0.5)).*exp(-0.5*(a+b).*(um - um0)).*besseli(v-0.5,(0.5*(a-b)*(um-um0)),1).*(0.5*(a-b).*(um - um0)).*(-dUmdE); 
Fc = (1-r)*(0.2880*KronD(E,58)+0.5*KronD(E,59.5)+0.1690*KronD(E,67.0)+0.0430*KronD(E,69.0));
F = Fb + Fc;

%F = (1-r)*(0.2880*KronD(E,57.98)+0.5000*KronD(E,59.32)+0.1690*KronD(E,67.20)+0.0430*KronD(E,69.10)); 
F = F/max(F); %% Normalización del espectro
F(isnan(F))=0; %sustituir NaN por cero
F = F';
E = E';

if Ef == 80
% Capa Semirreductora del Espectro (80kV)
K0 = sum(396.2*dE*F.*exp(-um'*0));
K2 = sum(396.2*dE*F.*exp(-um'*0.74));
K1 = sum(396.2*dE*F.*exp(-um'*0.58));
CSR = (0.58*log(2*K2/K0) - 0.74*log(2*K1/K0))/log(K2./K1);

elseif Ef == 120
% Capa Semirreductora del Espectro (120kV)
K0 = sum(629.2*dE*F.*exp(-um'*0));
K2 = sum(629.2*dE*F.*exp(-um'*1.63));
K1 = sum(629.2*dE*F.*exp(-um'*1.35));
CSR = (1.35*log(2*K2/K0) - 1.63*log(2*K1/K0))/log(K2./K1);
end
disp('Capa Semirreductora del Espectro')
fprintf('CSResp(cm^2/g) = %1.3f           \n',CSR');

disp('Error relativo')
Er = abs(100*(CSRct - CSR)/CSRct);
fprintf('Erel(%%) = %1.3f           \n',Er');

disp('Error relativo entre curvas')
fprintf('Erelcur(%%) = %1.2f           \n',pe');
end
%rng default
%% Gráfica da Curva de Transmissão
Transm = figure('Renderer', 'painters', 'Position', [10 10 650 600]);
plot(d,T,'*k',d1,T1,'k')
% xlabel('Thickness (g/cm^2)','fontsize',10)
% ylabel('Normalized Transmission','fontsize',10)
% legend('Experimental data','Fitted curve')
% print(Transm,nomect,'-djpeg','-r300') % Salvando imagem JPEG com 300 DPI
% 
% Espectro = figure('Renderer', 'painters', 'Position', [10 10 650 600]);
% plot(E,F,'k')
% xlabel('Energy (kV)','fontsize',10)
% ylabel('Normalized Energy Spectrum','fontsize',10)

xlabel('Thickness (g/cm^2)','fontsize',10)
ylabel('Transmission Curve','fontsize',10)
legend('Experimental data','Fit curve')
print(Transm,nomect,'-djpeg','-r300') % Salvando imagem JPEG com 300 DPI

Espectro = figure('Renderer', 'painters', 'Position', [10 10 650 600]);
plot(E,F,'k')
xlabel('Energy (kV)','fontsize',10)
ylabel('Energy spectrum','fontsize',10)

print(Espectro,nomesp,'-djpeg','-r300') % Salvando imagem JPEG com 300 DPI

%% Tiempo de cómputo
t = toc(timerval);
disp('Total Calculation Time')
fprintf('t = %d min e %0.3f s\n',floor(t/60),rem(t,60));%tempo de cálculo




