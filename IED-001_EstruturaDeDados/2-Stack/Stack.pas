program Stack;
type
    vetor = array[1..10] of integer;
    pilha = record
        topo: integer;
        vetor: vetor;
end;
var
    max, num: integer;
    p: pilha;
    
    procedure Init(var p_stack: pilha);
    begin
        p_stack.topo := 0;
    end;
    
    function IsEmpty(p_stack: pilha): boolean;
    begin
        if p_stack.topo = 0 then IsEmpty := true else IsEmpty := false;
    end;
    
    function IsFull(p_stack: pilha; n: integer): boolean;
    begin
        if p_stack.topo = n then IsFull := true else IsFull := false;
    end;
    
    procedure Pop(var p_stack: pilha);
    begin
        p_stack.topo := p_stack.topo - 1;
    end;
    
    procedure Push(var p_stack: pilha; x: integer);
    begin
        p_stack.topo := p_stack.topo + 1;
        p_stack.vetor[p_stack.topo] := x;
    end;
    
    procedure PositiveCount(p_stack: pilha);
    var
        count: integer;
    begin
        count := 0;
        while not IsEmpty(p_stack) do
        begin
            if p_stack.vetor[p_stack.topo] > 0 then
                count := count + 1;
                
            Pop(p_stack);
        end;
        writeln('Números positivos na pilha: ', count);
    end;
    
    function FuncPositiveCount(p_stack: pilha): integer;
    var
        count: integer;
    begin
        count := 0;
        while not IsEmpty(p_stack) do
        begin
            if p_stack.vetor[p_stack.topo] > 0 then
                count := count + 1;
                
            Pop(p_stack);
        end;
        FuncPositiveCount := count;
    end;
begin
  max := 10;
  Init(p);
  
  writeln;
  writeln('Digite 10 números para encher uma pilha: ');
  while not IsFull(p, max) do
  begin
    write(p.topo + 1, 'º elemento: ');
    readln(num);
    Push(p, num);
  end;
  
  writeln;
  PositiveCount(p);
  
  writeln;
  writeln('Números positivos na pilha por função: ', FuncPositiveCount(p));
  
  writeln;
  writeln('Saída da pilha: ');
  while not IsEmpty(p) do
  begin
    writeln(p.vetor[p.topo]);
    Pop(p);
  end;
end.

