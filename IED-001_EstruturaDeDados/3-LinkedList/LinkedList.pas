program LinkedList;
type
    endnodo = ^nodo;
    nodo = record
        info: integer;
        prox: endnodo;
    end;
    
    procedure InsereInicio(var p: endnodo; n: integer);
    var q: endnodo;
    begin
        new(q);
        q^.info := n;
        q^.prox := nil;
        
        if p = nil then
            p := q
        else begin
            q^.prox := p;
            p := q;
        end;
    end;
    
    procedure InsereFim(var p: endnodo; n: integer);
    var
        q, r: endnodo;
    begin
        new(r);
        r^.info := n;
        r^.prox := nil;
        
        if p = nil then
            p := r
        else begin
            q := p;
            while q^.prox <> nil do
                q := q^.prox;
            q^.prox := r;
        end;
    end;
    
    function count(p: endnodo): integer;
    var n: integer; q: endnodo;
    begin
        n := 0;
        if p <> nil then
        begin
            q := p;
            repeat
                n := n + 1;
                q := q^.prox;
            until (q = nil);
        end;
        count := n;
    end;
    
    procedure PrintList(p: endnodo);
    var q: endnodo; count: integer;
    begin
        if p <> nil then
        begin
            q := p;
            count := 1;
            repeat
                writeln(count,'º Elemento: ', q^.info);
                q := q^.prox;
                count := count + 1;
            until (q = nil);
        end;
    end;
    
    function EvenNumbers(p: endnodo): integer;
    var count: integer;
    begin
        count := 0;
        while p <> nil do
        begin
            if p^.info mod 2 = 0 then
                count := count + 1;
            p := p^.prox;
        end;
        EvenNumbers := count;
    end;
    
    function OddNumbers(p: endnodo): integer;
    var count: integer;
    begin
        count := 0;
        while p <> nil do
        begin
            if p^.info mod 2 <> 0 then
                count := count + 1;
            p := p^.prox;
        end;
        OddNumbers := count;
    end;
    
    function IncludeEndAndSum(var p: endnodo; n: integer): integer;
    var q, r: endnodo; sum: integer;
    begin
        new(r);
        r^.info := n;
        r^.prox := nil;
        sum := n;
        
        if p = nil then
            p := r
        else begin
            q := p;
            while q^.prox <> nil do
            begin
                sum := sum + q^.info;
                q := q^.prox;
            end;
            sum := sum + q^.info;
            q^.prox := r;
        end;
        IncludeEndAndSum := sum;
    end;

    procedure IncludeAfterEven(var p: endnodo; n: integer);
    var q, r: endnodo; foundeven: boolean;
    begin
        new(r);
        r^.info := n;
        r^.prox := nil;
        foundeven := false;
        
        if p = nil then
            p := r
        else begin
            q := p;
            while (q^.prox <> nil) and not foundeven do
            begin
                if q^.info mod 2 = 0 then
                    foundeven := true
                else
                    q := q^.prox;
            end;
            if foundeven then
                r^.prox := q^.prox;
                
            q^.prox := r;
        end;
    end;
var
    p: endnodo;
    num, l: integer;
begin
    p := nil;
    
    writeln('Digite um número ** DIFERENTE DE 0 ** para inserir na lista: ');
    readln(num);
    if num <> 0 then
    begin
        InsereFim(p, num); //InsereInicio e InsereFim sabem se virar e inserir um elemento quando a lista está vazia
    end;
    
    writeln;
    writeln('Digite um número para inserir na lista (digite 0 para parar de inserir): ');
    readln(num);
    while num <> 0 do
    begin
        writeln;
        writeln('Digite 0 - Inserir no começo da lista. Outro número - inserir no fim: ');
        readln(l);
        if l = 0 then
            InsereInicio(p, num)
        else
            InsereFim(p, num);
            
        writeln;
        writeln('Digite um número para inserir na lista (digite 0 para parar de inserir): ');
        readln(num);
    end;
    
    writeln;
    writeln('Digite um número para inserir na lista e somar todos os elementos: ');
    readln(num);
    writeln('Soma dos elementos da lista: ', IncludeEndAndSum(p, num));

    writeln;
    writeln('Digite um número para inserir na lista após o primeiro par, caso não possua elementos pares, será inserido no final: ');
    readln(num);
    IncludeAfterEven(p, num);
    
    writeln;
    writeln('Quantidade de elementos da lista: ', count(p));
    
    writeln;
    writeln('Quantidade de elementos pares da lista: ', EvenNumbers(p));
    
    writeln;
    writeln('Quantidade de elementos ímpares da lista: ', OddNumbers(p));
    
    writeln;
    PrintList(p);
end.