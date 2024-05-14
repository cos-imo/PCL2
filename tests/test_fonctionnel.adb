with Ada.Text_IO ; use Ada.Text_IO ;

procedure facto is 

--VARIABLES
n : integer := 5 ;
f : integer := 1 ;
g : integer := 1 ;
i : integer ;

--MAIN 
begin 
for i in 1_n loop
f := g * i ;
g := f ;
end loop ;
put(f);
end facto ; eof
