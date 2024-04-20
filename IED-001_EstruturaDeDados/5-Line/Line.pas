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
        IsEmpty := line.fim = 0;
    end;
    
    function IsFull(line: fila; max: integer): boolean;
    begin
        IsFull := (line.fim = max);
    end;
    
    procedure Enqueue(var line: fila; n: integer);
    begin
        line.fim := line.fim + 1;
        line.vetor[line.fim] := n;
    end;
    
    procedure Dequeue(var line: fila);
    var n: integer;
    begin
        if not IsEmpty(line) then
        begin
            n := 1;
            line.fim := line.fim - 1;
            while (n <= line.fim) do
            begin
                line.vetor[n] := line.vetor[n+1];
                n := n + 1;
            end;
        end else
            writeln('Line is already empty!');
    end;
    
    procedure PrintLine(line: fila);
    var aux: integer;
    begin
        aux := 1;
        writeln('Line Elements:');
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
        writeln('Line printed while all elements are removed:');
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
    
    writeln('Enter 5 numbers to fill a Line:');
    while not IsFull(f, max) do
    begin
        write(aux, '°: ');
        readln(num);
        Enqueue(f, num);
        aux := aux + 1;
    end;
    
    writeln;
    PrintLine(f);
    
    writeln;
    writeln('Type' + sLineBreak + '1 - Insert in Line;' + sLineBreak + '2 - Remove from Line;' + sLineBreak + 'Another number - Exit:');
    readln(num);
    while (num = 1) or (num = 2) do
    begin
        if num = 1 then
        begin
            if not IsFull(f, max) then
            begin
                write('Type the number to insert in the line: ');
                readln(num);
                Enqueue(f, num);
                writeln('Line after the element was inserted:');
                PrintLine(f);
            end else
                writeln('The line is already full!');
        end else
        begin
            Dequeue(f);
            writeln('Line after the element was removed:');
            PrintLine(f);
        end;
    
        writeln;
        writeln('Digite' + sLineBreak + '1 - Inserir na Fila;' + sLineBreak + '2 - Remover da Fila' + sLineBreak + 'Outro número - Sair:');
        readln(num);
    end;
    
    PrintLineDequeueing(f);
end.