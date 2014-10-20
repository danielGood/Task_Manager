%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>

<br>
Task Deadline: <input type="date" name="deadline" value="{{deadline[0]}}" pattern="\d{1,2}/\d{1,2}/\d{4}">
Task Starttime:<input type="date" name="starttime" value="{{starttime}}">
Task Priority : <input type="range" min="1" max="10" name="priority" value="{{priority}}">
<br/>
<input type="hidden" name="table" value="{{table}}">
<input type="submit" name="save" value="save">
</form>
