<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>WikiRace</title>
    <!-- <link rel="icon" href="/staticIco/pic/favicon.png" type="image/x-icon"> -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>    
    % import os ; raceJS = os.path.getsize("assets/race.js") ; raceCSS = os.path.getsize("assets/race.css")
    <script type='text/javascript' src='/static/race.js?filever={{raceJS}}'></script>  
    <link rel="stylesheet" type="text/css" href="/static/race.css?filever={{raceCSS}}">
  </head>
  <body>
    <h1>Wiki Race</h1>
    <div style="margin: 10px 5%">
      <input type="text" id="searchbox">
      <div id="autocomplete" class="autocomplete-items"></div>
    </div>
  </body>
</html>

