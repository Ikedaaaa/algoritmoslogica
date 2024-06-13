program PilhaFilaLinkedListABB;
    const max = 5;
    
    type //Pilha
        vet = array[1..5] of integer;
        pilha = record
            topo: integer;
            vetor: vet;
    end;
    
    type //fila (também utiliza o vet)
        fila = record
            vetor: vet;
            ini: integer;
            fim: integer;
    end;
    
    type //Lista Encadeada
        endnodo: ^nodo_ll;
        nodo_ll = record
            info: integer;
            prox: endnodo;
    end;
    
    type // Arvore Binária
        arvore = ^nodo_abb;
        nodo_abb = record
            dir: arvore;
            info: integer;
            esq: arvore;
    end;
    
    procedure Init(var stack: pilha);
    begin
        stack.topo := 0;
    end;
    
    function IsEmpty(stack: pilha): boolean;
    begin
        IsEmpty := (stack.topo = 0);
    end;
    
    function IsFull(stack: pilha): boolean;
    begin
        IsFull := (stack.topo = max);
    end;
    
    procedure Pop(var stack: pilha);
    begin
        stack.topo := stack.topo - 1;
    end;
    
    procedure Push(n:integer; var stack: pilha);
    begin
        stack.topo := stack.topo + 1;
        stack.vetor[stack.topo] := n;
    end;
    
    procedure fcriar(var line: fila);
    begin
        line.ini := 1;
        line.fim := 0;
    end;
    
    function fvazia(line: fila): boolean;
    begin
        fvazia := (line.fim < line.ini);
    end;
    
    function fcheia(line: fila): boolean;
    begin
        fcheia := (line.fim = max);
    end;
    
    procedure Enqueue(n: integer; var line: fila);
    begin
        line.fim := line.fim + 1;
        line.vetor[line.fim] := n;
    end;
    
    procedure Dequeue(var line: fila);
    begin
        line.ini := line.ini + 1;
    end;
    
    procedure CreateLinkedListFromStackAndLine(stack: pilha; line: fila; var p: endnodo);
    var q, r;
    begin
        if not IsEmpty(stack) then
        begin
            new(p);
            p^.info := stack.vetor[stack.topo];
            p^.prox := nil;
            Pop(stack);
            q := p;
        end;
        
        while not IsEmpty(stack) do
        begin
            new(r);
            r^.info := stack.vetor[stack.topo];
            r^.prox := nil;
            q^.prox := r;
            q := r;
            Pop(stack);
        end;
        
        while not fvazia(line) do
        begin
            new(r);
            r^.info := line.vetor[line.ini];
            r^.prox := nil;
            q^.prox := r;
            q := r;
            Dequeue(line);
        end;
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
    
    procedure CriaNodo(n: integer; var raiz: arvore);
    var t: arvore;
    begin
        new(t);
        t^.info := n;
        t^.esq := nil;
        t^.dir := nil;
        
        if raiz = nil then
            raiz := t
        else begin
            if n <= raiz^.info then
                raiz^.esq := t
            else
                raiz^.dir := t
        end;
    end;
    
    function BuscaNilNode(n: integer; raiz: arvore): arvore;
    begin
        if raiz = nil then
            BuscaNilNode := raiz
        else begin
            if n <= raiz^.info then
            begin
                if raiz^.esq = nil then
                    BuscaNilNode := raiz
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.esq);
            end else
            begin
                if raiz^.dir = nil then
                    BuscaNilNode := raiz
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.dir);
            end;
        end;
    end;
    
    procedure CreateABBFromLineAndStack(stack: pilha; line: fila; var raiz: arvore);
    var q, r: arvore;
    begin
        if not fvazia(line) then
        begin
            CriaNodo(line.vetor[line.ini], raiz);
            Dequeue(line);
            q := raiz;
        end;
        
        while not fvazia(line) do
        begin
            r := BuscaNilNode(line.vetor[line.ini], q);
            CriaNodo(line.vetor[line.ini], r);
            Dequeue(line);
        end;
        
        while not IsEmpty(stack) do
        begin
            r := BuscaNilNode(stack.vetor[stack.topo], q);
            CriaNodo(stack.vetor[stack.topo], r);
            Pop(stack);
        end;
    end;
    
    function CountNodes(raiz: arvore): integer;
    var count: integer;
    begin
        count := 0;
        if raiz <> nil then
        begin
            count := 1;
            count := count + CountNodes(raiz^.esq);
            count := count + CountNodes(raiz^.dir);
        end;
        CountNodes := count;
    end;
    
    function CountEvenNumbers(raiz: arvore): integer;
    var count: integer;
    begin
        count := 0;
        if raiz <> nil then
        begin
            if raiz^.info mod 2 = 0 then
                count := 1;
            count := count + CountEvenNumbers(raiz^.esq);
            count := count + CountEvenNumbers(raiz^.dir);
        end;
        CountEvenNumbers := count;
    end;
    
    function CountLeaves(raiz: arvore): integer;
    var count: integer;
    begin
        count := 0;
        if raiz <> nil then
        begin
            if (raiz^.esq = nil) and (raiz^.dir = nil) then
                count := 1;
            count := count + CountLeaves(raiz^.esq);
            count := count + CountLeaves(raiz^.dir);
        end;
        CountLeaves := count;
    end;
    
    function Busca(n: integer; raiz: arvore): boolean;
    begin
        if raiz = nil then
            Busca := False
        else begin
            if raiz^.info = n then
                Busca := True
            else if n < raiz^.info then
                Busca := Busca(n, raiz^.esq)
            else
                Busca := Busca(n, raiz^.dir);
        end;
    end;
    
    var
    root: arvore;
    ll: endnodo;
    pilhavar: pilha;
    filavar: fila;
    num: integer;
begin
    ll := nil;
    root := nil;
    Init(pilhavar);
    fcriar(filavar);
    
    
    Write('Digite um número para inserir na pilha: ');
    ReadLn(num);
    while not IsFull(pilhavar) do
    begin
        Push(num, pilhavar);
        
        Write(sLineBreak, 'Digite outro número para inserir na pilha: ');
        ReadLn(num);
    end;
    
    WriteLn(sLineBreak);
    Write('Digite um número para inserir na fila: ');
    ReadLn(num);
    while not fcheia(filavar) do
    begin
        Enqueue(num, filavar);
        
        Write(sLineBreak, 'Digite outro número para inserir na fila: ');
        ReadLn(num);
    end;
    
    CreateLinkedListFromStackAndLine(pilhavar, filavar, ll);
    CreateABBFromLineAndStack(pilhavar, filavar, root);
    
    WriteLn;
    WriteLn('Quantidade de nodos na ABB: ', CountNodes(root));
    
    WriteLn;
    WriteLn('Quantidade de números pares na ABB: ', CountEvenNumbers(root));
    
    WriteLn;
    WriteLn('Quantidade de folhas na ABB: ', CountLeaves(root));
    
    WriteLn;
    WriteLn('  *_________________________________________*');
    WriteLn('  *                                         *');
    WriteLn('  * Digite um números para pesquisar na ABB *');
    WriteLn('  * Ou digite 0 para encerrar o programa    *');
    WriteLn('  *_________________________________________*');
    WriteLn;
    Write('Número a ser buscado: ');
    ReadLn(num);
    while num <> 0 do
    begin
        if Busca(num, root) then
            WriteLn('Número encontrado!', sLineBreak)
        else
            WriteLn('Número não encontrado!', sLineBreak);
        Write('Número a ser buscado: ');
        ReadLn(num);
    end;
    
    WriteLn;
    WriteLn('  *______________________________________*');
    WriteLn('  *                                      *');
    WriteLn('  *            FIM DE PROGRAMA           *');
    WriteLn('  *______________________________________*');
end.