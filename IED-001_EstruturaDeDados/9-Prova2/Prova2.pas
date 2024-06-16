program Prova2;

type
    vetor = array[1..10] of integer;
    pilha = record
        vet: vetor;
        topo: integer;
    end;
    
    endnodo = ^nodo;
    nodo = record
        info: integer;
        prox: endnodo;
    end;
    
    arvore = ^nodo_abb;
    nodo_abb = record
        dir: arvore;
        info: integer;
        esq: arvore;
    end;
    
    //Auxiliar methods
    procedure Init(var stack: pilha);
    begin
        stack.topo := 0;
    end;
    
    function IsEmpty(stack: pilha): boolean;
    begin
        IsEmpty := (stack.topo = 0);
    end;
    
    function IsFull(stack: pilha; max: integer): boolean;
    begin
        IsFull := (stack.topo = max);
    end;
    
    procedure Push(n: integer; var stack: pilha);
    begin
        stack.topo := stack.topo + 1;
        stack.vet[stack.topo] := n;
    end;
    
    procedure Pop(var stack: pilha);
    begin
        stack.topo := stack.topo - 1;
    end;
    
    procedure ImprimePilha(stack: pilha);
    begin
        WriteLn;
        WriteLn('Imprimindo a pilha (desempilhando):');
        while not IsEmpty(stack) do
        begin
            WriteLn(stack.topo, 'º: ', stack.vet[stack.topo]);
            Pop(stack);
        end;
    end;
    
    procedure PrintList(ll: endnodo);
    var i: integer;
    begin
        if ll <> nil then
        begin
            i := 1;
            WriteLn(sLineBreak,'**** Imprimindo a lista ****');
            while ll <> nil do
            begin
                WriteLn(i,'º elemento: ', ll^.info);
                ll := ll^.prox;
                i := i + 1;
            end;
        end else
            WriteLn('**** LISTA ESTÁ VAZIA!!!! ****');
    end;
    
    procedure CriaNodo(num: integer; var root: arvore);
    var t: arvore;
    begin
        new(t);
        t^.info := num;
        t^.esq := nil;
        t^.dir := nil;
        
        if root = nil then
            root := t
        else begin
            if num <= root^.info then
                root^.esq := t
            else
                root^.dir := t;
        end;
    end;
    
    function BuscaNilNode(num: integer; root: arvore): arvore;
    begin
        if root = nil then
            BuscaNilNode := root
        else begin
            if num <= root^.info then
            begin
                if root^.esq = nil then
                    BuscaNilNode := root
                else
                    BuscaNilNode := BuscaNilNode(num, root^.esq);
            end else
            begin
                if root^.dir = nil then
                    BuscaNilNode := root
                else
                    BuscaNilNode := BuscaNilNode(num, root^.dir);
            end;
        end;
    end;
    
    function Busca(num: integer; root: arvore): boolean;
    begin
        if root = nil then
            Busca := False
        else begin
            if root^.info = num then
                Busca := True
            else if num <= root^.info then
                Busca := Busca(num, root^.esq)
            else
                Busca := Busca(num, root^.dir);
        end;
    end;
    //End of auxiliar methods
    
    //Test Questions
    procedure CriaPilha(vet: vetor; var stack: pilha); //Questão 1
    var i: integer;
    begin
        i := 1;
        Init(stack);
        
        while not IsFull(stack, 10) do
        begin
            Push(vet[i], stack);
            i := i + 1;
        end;
    end;
    
    function Fibonacci(num: integer): integer; //Questão 2
    begin
        if (num = 1) or (num = 2) then
            Fibonacci := 1
        else
            Fibonacci := Fibonacci(num-2) + Fibonacci(num-1);
    end;
    
    procedure FillList(vet: vetor; var ll: endnodo); //Questão 3
    var q, r: endnodo; i: integer;
    begin
        i := 1;
        if ll = nil then
        begin
            new(ll);
            ll^.info := vet[i];
            ll^.prox := nil;
            i := i + 1;
        end;
        
        q := ll;
        while q^.prox <> nil do
            q := q^.prox;
        
        while i <= 10 do
        begin
            new(r);
            r^.info := vet[i];
            r^.prox := nil;
            q^.prox := r;
            q := r;
            i := i + 1;
        end;
    end;
    
    function ContaFolhas(abb: arvore): integer; //Questão 4
    var count: integer;
    begin
        count := 0;
        if abb <> nil then
        begin
            if (abb^.esq = nil) and (abb^.dir = nil) then
                count := 1;
            count := count + ContaFolhas(abb^.esq);
            count := count + ContaFolhas(abb^.dir);
        end;
        ContaFolhas := count;
    end;
var
    p: pilha;
    v: vetor;
    lista1, lista2: endnodo; //Uma lista terá elementos e a outra estará vazia
    raiz, node: arvore;
    n: integer;
begin
    lista1 := nil;
    lista2 := nil;
    raiz := nil;
    
    WriteLn;
    WriteLn('Digite 10 números para preencher um array:');
    for n := Low(v) to High(v) do
    begin
        Write(n,'º: ');
        ReadLn(v[n]);
    end;
    
    //Cria pilha a partir dos elementos do vetor
    CriaPilha(v, p);
    ImprimePilha(p);
    
    //Retorna o n-ésimo número da sequência de Fibonacci
    WriteLn;
    WriteLn('Digite um número n para ver qual é o n-ésimo número da sequência de Fibonacci (Digite 0 para sair)');
    Write('n: ');
    ReadLn(n);
    while n >= 1 do
    begin
        WriteLn(n,'º número da sequência de Fibonacci: ', Fibonacci(n), sLineBreak);
        Write('n: ');
        ReadLn(n);
    end;
    
    //Creating list and making it fill with array elements 5 times, to test the empty list creation,
    //and filling a list that already has items
    for n := 1 to 5 do
        FillList(v, lista1);
    
    //Filling an empty list only once
    PrintList(lista2); // Just to test the "The List is empty" message
    FillList(v, lista2);
    
    //Printing both lists
    PrintList(lista1);
    PrintList(lista2);
    
    //Creating Binary Tree from array
    for n := Low(v) to High(v) do
    begin
        if n = 1 then
        begin
            CriaNodo(v[n], raiz);
        end else
        begin
            node := BuscaNilNode(v[n], raiz);
            CriaNodo(v[n], node);
        end;
    end;
    
    //How many leaves in Binary Tree
    WriteLn;
    WriteLn('Quantidade de Folhas na ABB: ', ContaFolhas(raiz));
    
    //Checking if element from array is present in Binary Tree by Search
    WriteLn(sLineBreak, 'Digite um número para pesquisar se existe na Árvore Binária (Digite 0 para encerrar o programa)');
    Write(sLineBreak, 'Pesquisa: ');
    ReadLn(n);
    while n <> 0 do
    begin
        if Busca(n, raiz) then
            WriteLn('Número encontrado!')
        else
            WriteLn('Número não encontrado!');
        
        Write(sLineBreak, 'Pesquisa: ');
        ReadLn(n);
    end;
    WriteLn('Fim do programa!')
end.