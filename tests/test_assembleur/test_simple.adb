with Ada.Text_IO ; use Ada.Text_IO ;

procedure main is 

--FONCTIONS

function premier(p: integer) return integer is
i : integer := 1 ;
b : integer :=0 ;
mod : integer ;
begin
while i<p loop
mod = p rem i ;
if mod == 0 then b = 1 ;
end if ;
end loop ;
return b ;
end premier ;

--VARIABLES 
max : integer := 20 ;
pb : integer := 0 ;
maxprem : integer := 1 ;

--MAIN
begin
for i in 1_max loop
pb = premier(i);
if pb == 1 then maxprem = i ; end if ;
end loop ; 

put(maxprem) ;

end main ; eof






