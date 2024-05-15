-- Test de base qui doit fonctionner
with Ada.Text_IO ; use Ada.Text_IO ;
procedure main is

function fonct(a: integer; b: integer) return Integer is c : Integer ;
begin
c := a+b ;
return c ;
end fonct ;

d : integer;
e : integer;
f : integer;

begin

d := 2;
e := 3;
fonct(d,e) ;

end main ; eof

