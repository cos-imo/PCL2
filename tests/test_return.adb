with Ada.Text_IO ; use Ada.Text_IO ;
procedure main is 

function Func (Var : Integer) return Integer
is Var : Integer
begin
  Var := 0;
   return Var;
end Func;

begin 
Func(1);
end main ;

eof
