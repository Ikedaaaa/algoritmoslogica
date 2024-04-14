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

    function StackCount(p: pilha): integer;
    var n: integer;
    begin
        n := 0;
        while not IsEmpty(p) do
        begin
            n := n + 1;
            Pop(p);
        end;
        StackCount := n;
    end;
    
    function OptimizedStackCount(p: pilha): integer;
    begin
        OptimizedStackCount := p.topo;
    end;

    procedure FillListFromStack(var p: endnodo; p_pilha: pilha);
    var q, r: endnodo;
    begin
        if not IsEmpty(p_pilha) then
        begin
            new(p);
            p^.info := p_pilha.vet[p_pilha.topo];
            p^.prox := nil;
            q := p;
            Pop(p_pilha);
        end;
        
        while not IsEmpty(p_pilha) do
        begin
            new(r);
            r^.info := p_pilha.vet[p_pilha.topo];
            r^.prox := nil;
            q^.prox := r;
            q := r;
            Pop(p_pilha);
        end;
    end;
    
    procedure PrintList(p: endnodo);
    var idx: integer;
    begin
        idx := 1;
        writeln('Itens da lista:');
        while p <> nil do
        begin
            writeln(idx, 'º: ', p^.info);
            idx := idx + 1;
            p := p^.prox;
        end;
    end;
    
    function ContaNegativos(p: endnodo): integer;
    var count: integer;
    begin
        count := 0;
        while p <> nil do
        begin
            if p^.info < 0 then
                count := count + 1;
            p := p^.prox;
        end;
        ContaNegativos := count;
    end;
var
    p: endnodo;
    num: integer;
    stack: pilha;
    StackMax: integer;
begin
    Init(stack);
    StackMax := 10;
    p := nil;
    
    writeln('Digite 10 números para preencher uma pilha: ');
    while not IsFull(stack, StackMax) do
    begin
        write(stack.topo + 1, 'º: ');
        readln(num);
        Push(stack, num);
    end;

    writeln;
    writeln('A pilha contém:');
    writeln('StackCount: ', StackCount(stack));
    writeln('OptimizedStackCount: ', OptimizedStackCount(stack));

    FillListFromStack(p, stack);
    
    writeln;
    writeln('Números negativos na lista: ', ContaNegativos(p));
    
    writeln;
    PrintList(p);
    
    writeln;
    writeln('Esvaziando pilha:');
    while not IsEmpty(stack) do
    begin
        writeln(stack.topo, 'º: ', stack.vet[stack.topo]);
        Pop(stack);
    end;
end.