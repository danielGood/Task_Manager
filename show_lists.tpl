
%def print_list(list, table, tablename):


<div class="list">
<h3 class="listHeadings">{{tablename[0]}}</h3>
%itemid =0
%for row in list:
    %i=0
    %id=1

    <div class="row">
    %for col in row:
        %if i==1:
            <div class="task">{{col}}</div>
        %end
        %if i==3:
            %itemid=col

        %end

        %i = i+1
    %end
<div class="rbuttons">
     <div class="edit">
<form action="/edit" method="GET">
<input type="image" src="/left_arrow" height ="30"  width="20" name="passtable" value="Edit Task">
<input type="hidden" name="tbleid" value={{table}}>
<input type="hidden" name="itemid" value={{itemid}}>
</form>
</div>
<div class="delete">
<form action="/delete" method="GET">
<input type="image" src="/red_x" height ="30"  width="30" name="passtable" value="Delete Task">
<input type="hidden" name="tbleid" value={{table}}>
<input type="hidden" name="itemid" value={{itemid}}>
</form>
</div>
</div>
    </div>

%id=id+1
%end

<form class ="add" action="/new" method="GET">
<input type="image" src="/plus" height ="30"  width="30" name="passtable" value="Add Task">
<input type="hidden" name="tbleid" value="{{table}}">
<input type="hidden" name="itemid" value={{itemid}}>
</form>
</div>



%end

<%




def print_tables():
   for table in tblist:
       mylist = tables[table]

       print_list(mylist, table, tbnames[table[0]-1])


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



