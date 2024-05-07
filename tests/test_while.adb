with Ada.Text_IO ; use Ada.Text_IO ;
procedure test_while_procedure is
-- VARIABLES
I : integer;
-- PROCEDURE PRINCIPALE
begin
  I := 0;
  while I<5 loop
    I := I + 1;
  end loop;
end test_while_procedure ; eof
