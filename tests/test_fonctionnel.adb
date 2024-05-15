with Ada.Text_IO ; use Ada.Text_IO ;

procedure facto is 

--VARIABLES
n : integer := 6;
f : integer ;
g : integer ;
i : integer ;


--MAIN 
begin 
f := 1 ;
g := 1 ;

for i in 1_n loop
    f := f * g ;
    g := g + 1 ;
end loop ;
put(f);
end facto ; eof
