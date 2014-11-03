%#template for the form for a new task
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="GET">
Task Name: <input type="text" size="100" maxlength="100" name="task">

<input type="submit" name="save" value="save">



<input type="hidden" name="itemid" value="{{itemid}}">
<input type="hidden" name="tbleid" value={{tbleid}}>

{{tbleid}}

</form>
