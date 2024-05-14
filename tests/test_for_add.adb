with Ada.Text_IO ; use Ada.Text_IO ;
procedure test_for_procedure is
-- VARIABLES
test_for_var : integer ;
i : integer;
-- PROCEDURE PRINCIPALE
begin
  test_for_var := 0;
  for i in 2_6 loop
    test_for_var := test_for_var + 1;
  end loop;
  put(test_for_var);
end test_for_procedure ; eof
