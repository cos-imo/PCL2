with Ada.Text_IO ; use Ada.Text_IO ;
procedure test_for_procedure is
-- VARIABLES
test_for_var : integer ;
i : integer;
-- PROCEDURE PRINCIPALE
begin
  test_for_var := 0;
  for i in 2_5 loop
    test_for_var := test_for_var + 1;
  end loop;
end test_for_procedure ; eof
