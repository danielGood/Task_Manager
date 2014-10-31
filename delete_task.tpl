%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item

<form action="/delete" method="get">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">

<br/>
<input type="hidden" name="table" value="{{table}}">
<input type="submit" name="save" value="save">
<input type="hidden" name="tbleid" value={{tbleid}}>
</form>
