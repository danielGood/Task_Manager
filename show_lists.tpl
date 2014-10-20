<h1>ToDo List</h1>                        {{date}}
<h5>todo list</h5>

<table>


%id = 1
%for row in rows:

    <tr>
    %for col in row:
        <td>{{col}}</td>

    %end
    <td>
        <form action="/edit/{{id}}" method="GET">
        <input type="submit" name="passtable" value="Edit Task">
        <input type="hidden" name="table" value="todo">
        </form>
        </td><td>
          <form action="/delete/{{id}}" method="GET">
        <input type="submit" name="passtable" value="Delete Task">
        <input type="hidden" name="table" value="todo">
        </form>
        </td>

    </tr>
    %id +=1
%end
</table>
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="todo">
</form>

<h5>daytodo list</h5>
<table>
%id = 1
%for row in rows2:

    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    <td>
        <form action="/edit/{{id}}" method="GET">
        <input type="submit" name="passtable" value="Edit Task">
        <input type="hidden" name="table" value="daytodo">
        </form>
        </td><td>
        <form action="/delete/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Delete Task">
          <input type="hidden" name="table" value="daytodo">
          </form>
        </td>

    </tr>
    %id +=1
%end
</table>
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="daytodo">
</form>
<h5>weektodo list</h5>
<table>
%id = 1
%for row in week:

    <tr>
    %for col in row:
        <td>{{col}}</td>

    %end
    <td>
        <form action="/edit/{{id}}" method="GET">
        <input type="submit" name="passtable" value="Edit Task">
        <input type="hidden" name="table" value="weektodo">
        </form>
        </td><td>
<form action="/delete/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Delete Task">
          <input type="hidden" name="table" value="weektodo">
          </form>

        </td>
    </tr>

    %id +=1
%end
</table>
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="weektodo">
</form>
<h5>monthtodo list</h5>
<table>
%id = 1
%for row in month:

    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
          <td>
          <form action="/edit/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Edit Task">
          <input type="hidden" name="table" value="monthtodo">
          </form>
          </td><td>
<form action="/delete/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Delete Task">
          <input type="hidden" name="table" value="monthtodo">
          </form>
        </td>


    </tr>
    %id +=1
%end
</table>
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="monthtodo">
</form>

<h5>overall list</h5>
<table>
%id = 1
%for row in overall:

    <tr>
    %for col in row:
        <td>{{col}}</td>

    %end
          <td>
          <form action="/edit/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Edit Task">
          <input type="hidden" name="table" value="overalltodo">
          </form>
          </td><td>
          <form action="/delete/{{id}}" method="GET">
          <input type="submit" name="passtable" value="Delete Task">
          <input type="hidden" name="table" value="overalltodo">
          </form>

        </td>


    </tr>
    %id +=1
%end

</table>
<form action="/new" method="GET">
<input type="submit" name="passtable" value="Add Task">
<input type="hidden" name="table" value="overalltodo">
</form>
