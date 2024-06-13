program Recursividade;
    function Fatorial(n: integer): integer;
    begin
        if n = 0 then
            Fatorial := 1
        else
            Fatorial := n * Fatorial(n - 1);
    end;
    var num: integer;
begin
    Write('Digite um número para calcular o fatorial: ');
    ReadLn(num);
    WriteLn(sLineBreak, num, '! = ', Fatorial(num));
end.