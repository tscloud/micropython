{% args sensor %}
<html>
<body>
<table>
  <tr>
    <th>value</th>
    <th>timestamp</th>
  </tr>
  <tr>
    <td>{{sensor['temp']}}</td>
    <td>11:00</td>
  </tr>
  <tr>
    <td>{{sensor['humidity']}}</td>
    <td>09:00</td>
  </tr>
  <tr>
    <td>{{sensor['pressure']}}</td>
    <td>09:00</td>
  </tr>
</table>

</body>

</html>