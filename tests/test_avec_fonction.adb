with Ada.Text_IO ; use Ada.Text_IO ;

procedure main is


--FONCTION
function facto(n:integer) return integer is 

f : integer ;
g : integer ;
i : integer ;

begin 
f := 1 ;
g := 1 ;

for i in 1_n loop
f := g * i ;
g := f ;
end loop ;
put(f);
return 0 ;
end facto ;

--VARIABLES
n : integer ;

--MAIN
begin
n := 5 ;
facto(5) ;

end main; eof
