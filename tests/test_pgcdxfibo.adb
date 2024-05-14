with Ada.Text_IO ; use Ada.Text_IO ;

procedure main is 

--FONCTIONS

function pgcd(a: Integer; b: Integer) return Integer is 
r : integer ;
begin 
while b/=0 loop 
r = a rem b ;
a = b ;
b = r ;
end loop ;
return a ;
end pgcd ;

function fibo(p: Integer) return Integer is 
pl : interger ;
pm : integer ;
plq : integer ;
pmq : integer ;
q : integer ;
begin 
if p<=1 
then return p ;
else 
pl= p-1 ; 
pm = p-2 ;
plq = fibo(pl) ;
pmq = fibo(pmq) ;
q = plq + pmq ;
return q ;
end if ;
end fibo ;

--VARIABLES
i : integer ;
j : integer ;
pgcdij : integer ;
fiboij : integer ;

--MAIN 
begin
for i in 1_10 loop
for j in 1_10 loop
pgcdij = pgcd(i,j);
fiboij = fibo(pgcdij);
put(pgcdij);
put(fiboij);
end loop ;
end loop ;

end main ; eof


