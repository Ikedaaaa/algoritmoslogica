program Line;
type
    vet = array[1..5] of integer;
    fila = record
        vetor: vet;
        inic: integer;
        fim: integer;
    end;
    
    procedure InitLine(var line: fila);
    begin
        line.fim := 0;
        line.inic := 1;
    end;
    
    function IsEmpty(line: fila): boolean;
    begin
        IsEmpty := line.inic > line.fim;
    end;
    
    function IsFull(line: fila; max: integer): boolean;
    begin
        IsFull := (line.fim = max); //and (line.fim > line.inic);
    end;
    
    procedure Enqueue(var line: fila; n: integer);
    begin
        line.fim := line.fim + 1;
        line.vetor[line.fim] := n;
    end;
    
    procedure Dequeue(var line: fila);
    begin
        line.inic := line.inic + 1;
    end;
    
    procedure PrintLine(line: fila);
    var aux: integer;
    begin
        aux := 1;
        writeln('Elementos da fila:');
        while not IsEmpty(line) do
        begin
            writeln(aux, '°: ', line.vetor[line.inic]);
            Dequeue(line);
            aux := aux + 1;
        end;
    end;
    
    procedure PrintLineDequeueing(var line: fila);
    begin
        writeln;
        writeln('Impressão da fila enquanto ela é esvaziada:');
        while not IsEmpty(line) do
        begin
            writeln;
            PrintLine(line);
            Dequeue(line);
        end;
    end;
var
    f: fila;
    num, max, aux: integer;
begin
    InitLine(f);
    aux := 1;
    max := 5;
    
    //Para o estudo de Estrutura de Dados, a fila é iniciada com
    //idx inic := 1;
    //idx fim := 0;
    //Feito dessa forma para que a indicação de IsEmpty possa ser line.inic > line.fim;
    //Para cada elemento inserido, simplesmente o idx fim sobe uma posição até que atinja o max de elementos no vetor da fila
    //Para remover elementos, o inic sobe uma posição até passar o fim.
    //O vetor não seria reordenado para "a fila andar", pois, segundo o professor, isso seria manipulação de vetor
    //Como o foco é estudar a Estrutura de Dados Fila, não é necessário estudar manipulação de vetor pois não é o foco
    //Quando a fila estiver cheia e depois for esvaziada, o programa será encerrado, pois o vator da fila não será reordenado
    
    writeln('Digite números para preencher uma fila:');
    while not IsFull(f, max) do
    begin
        write(aux, '°: ');
        readln(num);
        Enqueue(f, num);
        aux := aux + 1;
    end;
    
    PrintLineDequeueing(f);
end.