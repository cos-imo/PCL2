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
        f := f * g ;
        g := g +1 ;
    end loop ;
    put(f);
    return 0 ;
end facto ;

--VARIABLES
n : integer := 5 ;

--MAIN
begin
    facto(n) ;
end main; eof
