%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Delete the task with ID = {{no}}</p>
<form action="/delete/{{no}}" method="get">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">

<br/>
<input type="hidden" name="table" value="{{table}}">
<input type="submit" name="save" value="save">
</form>
