%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID </p>
<form action="/edit" method="get">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>


<input type="hidden" name="itemid" value="{{itemid}}">
<input type="hidden" name="tbleid" value={{tbleid}}>
<input type="submit" name="save" value="save">
</form>
