with Ada.Text_IO ; use Ada.Text_IO ;
procedure test_if_procedure is
-- VARIABLES
test_if_var : integer ;
-- PROCEDURE PRINCIPALE
begin
  test_if_var := 2;
  if test_if_var > 1 then
    test_if_var := 0;
  end if;
end test_if_procedure ; eof
