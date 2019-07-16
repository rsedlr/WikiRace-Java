<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>WikiRace</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    % import os ; raceJS = os.path.getsize("assets/race.js") ; raceCSS = os.path.getsize("assets/race.css")
    <link rel="stylesheet" type="text/css" href="/static/race.css?filever={{raceCSS}}">
  </head>
  <body>
    <div id="main">
      <h1>Wiki Race</h1>
      <div class="row searchRow">
        <div class="searchDiv col-12 col-sm-6">
          <h4>Start page:</h4>
          <input type="text" id="startBox">
          <div id="startBox-autocomplete" class="autocomplete"></div>
        </div>
        <div class="searchDiv col-12 col-sm-6">
          <h4>End page:</h4>
          <input type="text" id="endBox">
          <div id="endBox-autocomplete" class="autocomplete"></div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <button onclick="search()">Find shortest route</button>
        </div>
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8=" crossorigin="anonymous"></script>    
    <!-- <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>     -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script type='text/javascript' src='/static/race.js?filever={{raceJS}}'></script>  
  </body>
</html>