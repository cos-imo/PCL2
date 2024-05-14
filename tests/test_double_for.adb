;le test ne passe pas encore, il faut penser à remettre les registre du compteur de la première boucle a jour, ou utliser un autre registre, car lorsque la deuxième boucle est finie, le registre de la première boucle est à 5, et donc la première boucle ne se finit pas. boucle s'effectue, ca modiifel es compteur de la premiere

with Ada.Text_IO ; use Ada.Text_IO ;
procedure test_for_procedure is
-- VARIABLES
test_for_var : integer ;
i : integer;
k : integer;
-- PROCEDURE PRINCIPALE
begin
  test_for_var := 0;
  for i in 2_5 loop
    for k in 1_5 loop
        test_for_var := test_for_var + 1;
    end loop;
  end loop;
end test_for_procedure ; eof
