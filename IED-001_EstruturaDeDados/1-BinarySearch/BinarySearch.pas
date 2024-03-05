program BuscaBinaria;
var
    list: array[1..20] of integer;
    i, j, aux, search, SearchedValueIdx: integer;
    ListHasOnlyUniqueValues: integer;
    
    function BinarySearchUniqueValues(ArrayToSearch: array of integer; ValueToSearch: integer): integer;
    var
        InitialIndex, FinalIndex, MiddleIndex: integer;
    begin
        BinarySearchUniqueValues := -1;
        InitialIndex := Low(ArrayToSearch);
        FinalIndex := High(ArrayToSearch);
        
        repeat
            MiddleIndex := (InitialIndex + FinalIndex) div 2;
            if ValueToSearch = ArrayToSearch[MiddleIndex] then
            begin
                BinarySearchUniqueValues := MiddleIndex;
                InitialIndex := FinalIndex + 1;
            end else
            if ValueToSearch < ArrayToSearch[MiddleIndex] then
                FinalIndex := MiddleIndex - 1
            else
                InitialIndex := MiddleIndex + 1;
                
        until (InitialIndex > FinalIndex);
    end;
    
    function BinarySearchNotUniqueValues(ArrayToSearch: array of integer; ValueToSearch: integer): integer;
    var
        InitialIndex, FinalIndex, MiddleIndex: integer;
    begin
        BinarySearchNotUniqueValues := -1;
        InitialIndex := Low(ArrayToSearch);
        FinalIndex := High(ArrayToSearch);
        
        repeat
            MiddleIndex := (InitialIndex + FinalIndex) div 2;
            if ValueToSearch = ArrayToSearch[MiddleIndex] then
            begin
                BinarySearchNotUniqueValues := MiddleIndex;
                FinalIndex := MiddleIndex - 1;
            end else
            if ValueToSearch < ArrayToSearch[MiddleIndex] then
                FinalIndex := MiddleIndex - 1
            else
                InitialIndex := MiddleIndex + 1;
                
        until (InitialIndex > FinalIndex);
    end;
    
    function BinarySearch(ArrayToSearch: array of integer; ValueToSearch: integer; HasOnlyUniqueValues: Boolean): integer;
    var
        InitialIndex, FinalIndex, MiddleIndex: integer;
    begin
        BinarySearch := -1;
        InitialIndex := Low(ArrayToSearch);
        FinalIndex := High(ArrayToSearch);
        
        repeat
            MiddleIndex := (InitialIndex + FinalIndex) div 2;
            if ValueToSearch = ArrayToSearch[MiddleIndex] then
            begin
                BinarySearch := MiddleIndex;
                if HasOnlyUniqueValues then
                    InitialIndex := FinalIndex + 1
                else
                    FinalIndex := MiddleIndex - 1;
            end else
            if ValueToSearch < ArrayToSearch[MiddleIndex] then
                FinalIndex := MiddleIndex - 1
            else
                InitialIndex := MiddleIndex + 1;
                
        until (InitialIndex > FinalIndex);
    end;

begin
    writeln('Enter 20 natural numbers to fill an array');
    for i := 1 to 20 do
    begin
        write(i,'º: ');
        read(list[i]);
    end;
  
    writeln;
  
    //bubble sort
    for i := 1 to 19 do
    begin
        for j := (i + 1) to 20 do
        begin
            if list[i] > list[j] then
            begin
                aux := list[i];
                list[i] := list[j];
                list[j] := aux;
            end;
        end;
    end;
    
    writeln('Sorted array:');
    for i := 1 to 20 do
    begin
        writeln('Element ',i,' (idx:',i-1,'): ', list[i]);
    end;
    
    writeln('Is the list composed only of unique elements or does it have duplicates? (Type 1 if the list has only unique elements, or type 0 in case there are duplicates)');
    readln(ListHasOnlyUniqueValues);
    
    write('Enter a number to search (type -1 to end the program): ');
    readln(search);
    while search > -1 do
    begin
        SearchedValueIdx := BinarySearch(list, search, ListHasOnlyUniqueValues = 1);
            
        if SearchedValueIdx > -1 then
            writeln('Value: ', search, ' found on position: ', SearchedValueIdx)
        else
            writeln('Value not found');
        
        writeln;
        write('Enter a number to search (type -1 to end the program): ');
        readln(search);
    end;
    
    write('Program finished');
end.