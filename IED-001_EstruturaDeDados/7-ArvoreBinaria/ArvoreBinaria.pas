program ArvoreBinaria;
    type
        arvore = ^nodo;
        nodo = record
            dir: arvore;
            info: integer;
            esq: arvore;
    end;
    
    {function BuscaNilNodeNW(n: integer; raiz: arvore): arvore; //Thought it would work, but doesn't (NW = Not Working)
    begin
        if raiz = nil then
            BuscaNilNode := raiz
        else begin
            if n <= raiz^.info then
            begin
                if raiz^.esq = nil then
                    BuscaNilNode := raiz^.esq
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.esq);
            end else
            begin
                if raiz^.dir = nil then
                    BuscaNilNode := raiz^.dir
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.dir);
            end;
        end;
    end;}
    
    {function BuscaNilAnotherWayNW(n: integer; raiz: arvore): arvore; //Doesn't work  (NW = Not Working)
    begin
        if raiz = nil then
            BuscaNilAnotherWay := raiz
        else begin
            if n <= raiz^.info then
                BuscaNilAnotherWay := BuscaNilAnotherWay(n, raiz^.esq);
            else
                BuscaNilAnotherWay := BuscaNilAnotherWay(n, raiz^.dir);
        end;
    end;}
    
    procedure CriaNodo(n: integer; var node: arvore);
    var t: arvore;
    begin
        new(t);
        t^.info := n;
        t^.esq := nil;
        t^.dir := nil;
        
        if node = nil then
            node := t
        else begin
            if n <= node^.info then
                node^.esq := t
            else
                node^.dir := t;
        end;
    end;
    
    function BuscaNilNode(n: integer; raiz: arvore): arvore;
    begin
        if raiz = nil then
            BuscaNilNode := raiz
        else begin
            if n > raiz^.info then
            begin
                if raiz^.dir = nil then
                    BuscaNilNode := raiz
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.dir);
            end else
            begin
                if raiz^.esq = nil then
                    BuscaNilNode := raiz
                else
                    BuscaNilNode := BuscaNilNode(n, raiz^.esq);
            end;
        end;
    end;
    
    function Busca(n: integer; raiz: arvore): boolean;
    begin
        if raiz = nil then
            Busca := False
        else begin
            if n = raiz^.info then
                Busca := True
            else if n < raiz^.info then
                Busca := Busca(n, raiz^.esq)
            else
                Busca := Busca(n, raiz^.dir);
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
    
    var
        r, q, root: arvore;
        num: integer;
begin
    WriteLn;
    WriteLn('  *______________________________________*');
    WriteLn('  *                                      *');
    WriteLn('  * Digite um número para inserir na ABB *');
    WriteLn('  * Ou digite 0 para parar de inserir    *');
    WriteLn('  *______________________________________*');
    WriteLn;
    Write('Digite um número para criar a raiz da ABB: ');
    ReadLn(num);
    
    root := nil;
    if num <> 0 then
    begin
        CriaNodo(num, root);
        WriteLn('Raiz Criada!!!');
        Write(sLineBreak, 'Digite outro número para inserir na ABB: ');
        ReadLn(num);
        q := root;
    end;
    
    while num <> 0 do
    begin
        r := BuscaNilNode(num, q);
        CriaNodo(num, r);
        Write(sLineBreak, 'Digite outro número para inserir na ABB: ');
        ReadLn(num);
    end;
    
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