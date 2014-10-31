
%def print_list(list, table):

%tbleid =0
%for row in list:
    %i=0
    %id=1

    <div >
    %for col in row:
        %if i==1:
            <div class="task">{{col}}</div>
        %end
        %if i==4:
            %tbleid=col
        %end

        %i = i+1
    %end

     <div class="edit">
<form action="/edit" method="GET">
<input type="submit" name="passtable" value="Edit Task">
<input type="hidden" name="table" value={{table}}>
<input type="hidden" name="tbleid" value={{tbleid}}>
</form>
</div>
<div class="delete">
<form action="/delete" method="GET">
<input type="submit" name="passtable" value="Delete Task">
<input type="hidden" name="table" value={{table}}>
<input type="hidden" name="tbleid" value={{tbleid}}>
</form>
</div>
    </div>

%id=id+1
%end
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="{{table}}">
<input type="hidden" name="tbleid" value={{tbleid}}>
</form>

%end

<%




def print_tables():
   for table in tblist:
       mylist = tables[table]
       print_list(mylist, table)


   end
end
%>








<html>
<head>
<link rel="stylesheet" type="text/css" href="/ref_style" media="all" />

</head>

<body>


%print_tables()
<form action="/new_table" method="GET">
<input type="submit" name="passtable" value="Add Table">

</form>
</body>



</html>



