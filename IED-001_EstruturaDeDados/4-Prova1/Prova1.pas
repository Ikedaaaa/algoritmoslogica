program Prova1;
type
    endnodo = ^nodo;
    nodo = record
        info: integer;
        prox: endnodo;
    end;
    
    vetor = array[1..10] of integer;
    pilha = record
        topo: integer;
        vet: vetor;
    end;
    
    procedure Init(var p: pilha);
    begin
        p.topo := 0;
    end;
    
    function IsEmpty(p: pilha): boolean;
    begin
        if p.topo = 0 then IsEmpty := True else IsEmpty := False;
    end;
    
    function IsFull(p: pilha; max: integer): boolean;
    begin
        if p.topo = max then IsFull := True else IsFull := False;
    end;
    
    procedure Push(var p: pilha; n: integer);
    begin
        p.topo := p.topo + 1;
        p.vet[p.topo] := n;
    end;
    
    procedure Pop(var p: pilha);
    begin
        p.topo := p.topo - 1;
    end;
var
    p: endnodo;
    num: integer;
    stack: pilha;
    StackMax: integer;
begin
    Init(stack);
    StackMax := 10;
    
    writeln('Digite 10 números para preencher uma pilha: ');
    while not IsFull(stack, StackMax) do
    begin
        write(stack.topo + 1, 'º: ');
        readln(num);
        Push(stack, num);
    end;
    
    writeln;
    writeln('Esvaziando pilha:');
    while not IsEmpty(stack) do
    begin
        writeln(stack.topo, 'º: ', stack.vet[stack.topo]);
        Pop(stack);
    end;
end.