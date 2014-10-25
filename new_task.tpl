%#template for the form for a new task
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="GET">
Task Name: <input type="text" size="100" maxlength="100" name="task">
Optional:
Task Deadline: <input type="text" pattern="\d{1,2}/\d{1,2}/\d{4}"  name="deadline">
Task Starttime:<input type="text" pattern="\d{1,2}/\d{1,2}/\d{4}" name="starttime">
Task Priority : <input type="number" min="1" max="10" name="priority">
<input type="submit" name="save" value="save">
<input type="hidden" name="table" value="{{table}}">
</form>
